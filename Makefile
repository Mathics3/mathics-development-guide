PIP ?= pip3
RM  ?= rm

#: Default target - same as "develop"
all: developer-docs

.PHONY: developer-docs

#: Build developer guide
developer-docs:
	$(MAKE) -C docs html


#: Install necessary Python modules
setup:
	pip install -r requirements.txt

#: Rebuild docs from scratch
rebuild:
	$(MAKE) -C rebuild
