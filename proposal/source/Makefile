#
# File:   lecturenotes.mak
# Author: Adam Lewis
# Purpose:
# Build lectures notes for a single module
#
# Tools for building latex
LATEXMK = latexmk -f
RM = rm -f
.PHONY: all mostlyclean clean release

# Rules
%.pdf: %.tex
	$(LATEXMK) -pdf -M -MP -MF $*.d $*

# Targets
MODNAME1=quantum_tutorial
MODNAME2=
MODNAME3=
MODNAME4=

all: $(MODNAME1) 

release: all mostlyclean

$(MODNAME1): $(MODNAME1).pdf 

$(MODNAME1).pdf: $(MODNAME1).tex 

# Clean targets
mostlyclean:
	$(LATEXMK) -silent -c
	$(RM) *.bbl *.aux *.fls *.fdb_latexmk *.out *.log *.toc *.blg
	$(RM) *.run.xml *.synctex.gz *.nav *.snm
	$(RM) *.vrb
	$(RM) *.d 

clean: mostlyclean
	$(LATEXMK) -silent -C
	$(RM) *.pdf
# Include auto-genrated dependenies
-include *.d
