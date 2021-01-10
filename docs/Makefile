# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
PYTHON        ?= python
SOURCEDIR     = .
BUILDDIR      = _build

TABLES := $(wildcard docs/translation-tables/*-table.rst)


#: Build the html documentation
all: $(TABLES)
	$(MAKE) html

#: Wipe and rebuild the html documentation
rebuild:
	$(MAKE) clean && $(MAKE)

#: Show help
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: all help Makefile clean

clean:
	@rm -fr _build/* || true;
	@[ -n "$(TABLES)" ] && rm $(TABLES) || true

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%:
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

docs/translation-tables/full-unicode-conversion-table.rst:
	$(PYTHON) ../admin-tools/generate-tables.py
