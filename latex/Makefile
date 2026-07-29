MAIN = curriculum
PDFLATEX = pdflatex
BUILD = build

.PHONY: all clean

all:
	mkdir -p $(BUILD)
	$(PDFLATEX) -output-directory=$(BUILD) $(MAIN).tex
	$(PDFLATEX) -output-directory=$(BUILD) $(MAIN).tex
	cp $(BUILD)/$(MAIN).pdf .
	make clean
	clear

clean:
	rm -rf $(BUILD)
	rm -f $(MAIN).aux
	rm -f $(MAIN).log
	rm -f $(MAIN).out
	rm -f $(MAIN).synctex.gz
	rm -f $(MAIN).synctex
	rm -f $(MAIN).fls
	rm -f $(MAIN).fdb_latexmk