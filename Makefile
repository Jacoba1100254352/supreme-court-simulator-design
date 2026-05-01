MAIN_SOURCES := $(shell find src/main/java -name '*.java')
TEST_SOURCES := $(shell find src/test/java -name '*.java')
JAVA_RELEASE ?= 21
JAVA_PROPS ?= -Dconstitutionalreview.javaRelease=$(JAVA_RELEASE)

.PHONY: build run campaign paper paper-clean test ci clean

build:
	mkdir -p out/main
	javac --release $(JAVA_RELEASE) -d out/main $(MAIN_SOURCES)

run: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main $(ARGS)

campaign: build
	java $(JAVA_PROPS) -cp out/main constitutionalreview.Main --campaign v0 --runs 80 --cases 64 --seed 20260501 --output-dir reports $(ARGS)

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
