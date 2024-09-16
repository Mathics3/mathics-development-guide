PIP ?= pip3
RM  ?= rm

#: Default target - same as "develop"
all: developer-docs png

.PHONY: developer-docs clean

#: Build developer guide
developer-docs:
	admin-tools/generate-tables.py
	$(MAKE) -C docs html


#: Install necessary Python modules
setup:
	pip install -r requirements.txt

#: Rebuild docs from scratch
build rebuild:
	$(MAKE) -C docs $<

#: Wipe derivable files
clean:
	$(MAKE) -C docs $<

png:
	$(MAKE) -C docs/code-overview $@
