MAIN_SOURCES := $(shell find src/main/java -name '*.java')
TEST_SOURCES := $(shell find src/test/java -name '*.java')
JAVA_RELEASE ?= 21
JAVA_PROPS ?= -Dconstitutionalreview.javaRelease=$(JAVA_RELEASE)
LEGISLATIVE_FAMILY_DIR ?= data/external/legislative
CALIBRATION_DATA_DIR ?= data/calibration
RAW_CALIBRATION_DIR ?= data/raw/calibration
PAPER_LEGISLATIVE_INPUT ?= data/external/legislative/simulation-campaign-v21-paper.csv
PAPER_ARGS ?= --legislative-input "$(PAPER_LEGISLATIVE_INPUT)"

.PHONY: build run campaign campaign-v0 campaign-v1 campaign-v2 manipulation-stress calibrate calibration-refresh raw-source-refresh seed-robustness mechanism-ablation parameter-sweep prior-uncertainty legislative-family-comparison validation-dashboards diagnostics paper paper-check paper-source-audit paper-figures paper-figure-files paper-artifacts-check paper-title-page paper-pdf-freshness-check paper-jlc-template-check paper-strict-check replication-package anonymous-submission-package replication-check paper-clean dist-clean test ci clean

build:
	mkdir -p out/main
	javac --release $(JAVA_RELEASE) -d out/main $(MAIN_SOURCES)

run: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main $(ARGS)

campaign: campaign-v2

campaign-v2: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --campaign v2 --runs 80 --cases 64 --seed 20260501 --output-dir reports $(PAPER_ARGS) $(ARGS)

campaign-v1: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --campaign v1 --runs 80 --cases 64 --seed 20260501 --output-dir reports $(PAPER_ARGS) $(ARGS)

campaign-v0: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --campaign v0 --runs 80 --cases 64 --seed 20260501 --output-dir reports $(PAPER_ARGS) $(ARGS)

manipulation-stress: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --campaign manipulation-stress --runs 80 --cases 64 --seed 20260501 --output-dir reports $(PAPER_ARGS) $(ARGS)

calibrate: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --calibrate --runs 80 --cases 64 --seed 20260501 --output-dir reports --calibration-data-dir "$(CALIBRATION_DATA_DIR)" $(PAPER_ARGS) $(ARGS)

calibration-refresh:
	python3 tools/refresh_calibration_sources.py --raw-dir "$(RAW_CALIBRATION_DIR)" --output-dir "$(CALIBRATION_DATA_DIR)" $(ARGS)

raw-source-refresh: calibration-refresh

seed-robustness: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --seed-robustness --runs 40 --cases 48 --seed 20260501 --output-dir reports $(PAPER_ARGS) $(ARGS)

mechanism-ablation: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --mechanism-ablation --runs 60 --cases 48 --seed 20260501 --output-dir reports $(PAPER_ARGS) $(ARGS)

parameter-sweep: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --parameter-sweep --runs 40 --cases 48 --seed 20260501 --output-dir reports $(PAPER_ARGS) $(ARGS)

prior-uncertainty: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --prior-uncertainty --prior-samples 32 --runs 24 --cases 48 --seed 20260501 --output-dir reports $(PAPER_ARGS) $(ARGS)

legislative-family-comparison: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --legislative-family-comparison --legislative-family-dir "$(LEGISLATIVE_FAMILY_DIR)" --runs 40 --cases 48 --seed 20260501 --output-dir reports $(ARGS)

validation-dashboards:
	python3 tools/build_validation_dashboards.py

diagnostics: calibrate seed-robustness mechanism-ablation parameter-sweep prior-uncertainty legislative-family-comparison manipulation-stress validation-dashboards

paper-figures:
	python3 tools/build_validation_dashboards.py
	python3 paper/scripts/generate_figures.py

paper-figure-files: paper-figures
	python3 paper/scripts/export_figures.py

paper-artifacts-check:
	python3 paper/scripts/verify_paper_artifacts.py

paper-pdf-freshness-check:
	python3 paper/scripts/check_pdf_freshness.py

paper-jlc-template-check:
	python3 paper/scripts/check_jlc_format.py --require-cambridge-class

paper-source-audit:
	python3 paper/scripts/check_source_audit.py

paper-check: paper-figures paper-artifacts-check paper-source-audit
	python3 paper/scripts/check_jlc_format.py

paper: paper-check paper-figure-files
	mkdir -p paper/build
	rm -f paper/build/main.aux paper/build/main.bbl paper/build/main.blg paper/build/main.fdb_latexmk paper/build/main.fls paper/build/main.out
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
	python3 paper/scripts/check_latex_log.py
	cp paper/build/main.pdf paper/main.pdf
	python3 paper/scripts/check_pdf_freshness.py

paper-title-page:
	mkdir -p paper/build
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build title-page.tex

paper-strict-check: paper paper-title-page paper-pdf-freshness-check
	python3 paper/scripts/check_jlc_format.py --strict-submission
	python3 paper/scripts/check_source_audit.py

replication-package: paper
	python3 tools/create_replication_package.py

anonymous-submission-package: paper
	python3 tools/create_anonymous_submission_package.py

replication-check: test campaign-v0 campaign-v1 campaign-v2 diagnostics paper-strict-check replication-package anonymous-submission-package
	python3 tools/check_replication_package.py

paper-clean:
	cd paper && latexmk -C -outdir=build main.tex
	rm -rf paper/build
	rm -rf paper/figure-exports/build

test: build
	mkdir -p out/test
	javac --release $(JAVA_RELEASE) -cp out/main -d out/test $(TEST_SOURCES)
	java $(JAVA_PROPS) -cp out/main:out/test constitutionalreview.SimulatorTests

ci: test campaign paper

clean:
	rm -rf out

dist-clean: clean paper-clean
	rm -rf dist
