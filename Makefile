MAIN_SOURCES := $(shell find src/main/java -name '*.java')
TEST_SOURCES := $(shell find src/test/java -name '*.java')
JAVA_RELEASE ?= 21
JAVA_PROPS ?= -Dconstitutionalreview.javaRelease=$(JAVA_RELEASE)

.PHONY: build run campaign campaign-v0 campaign-v1 campaign-v2 manipulation-stress calibrate seed-robustness mechanism-ablation diagnostics paper paper-clean test ci clean

build:
	mkdir -p out/main
	javac --release $(JAVA_RELEASE) -d out/main $(MAIN_SOURCES)

run: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main $(ARGS)

campaign: campaign-v2

campaign-v2: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --campaign v2 --runs 80 --cases 64 --seed 20260501 --output-dir reports $(ARGS)

campaign-v1: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --campaign v1 --runs 80 --cases 64 --seed 20260501 --output-dir reports $(ARGS)

campaign-v0: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --campaign v0 --runs 80 --cases 64 --seed 20260501 --output-dir reports $(ARGS)

manipulation-stress: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --campaign manipulation-stress --runs 80 --cases 64 --seed 20260501 --output-dir reports $(ARGS)

calibrate: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --calibrate --runs 80 --cases 64 --seed 20260501 --output-dir reports $(ARGS)

seed-robustness: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --seed-robustness --runs 40 --cases 48 --seed 20260501 --output-dir reports $(ARGS)

mechanism-ablation: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --mechanism-ablation --runs 60 --cases 48 --seed 20260501 --output-dir reports $(ARGS)

diagnostics: calibrate seed-robustness mechanism-ablation manipulation-stress

paper:
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
	cp paper/build/main.pdf paper/main.pdf

paper-clean:
	cd paper && latexmk -C -outdir=build main.tex
	rm -rf paper/build

test: build
	mkdir -p out/test
	javac --release $(JAVA_RELEASE) -cp out/main -d out/test $(TEST_SOURCES)
	java $(JAVA_PROPS) -cp out/main:out/test constitutionalreview.SimulatorTests

ci: test campaign paper

clean:
	rm -rf out
