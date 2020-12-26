.PHONY: developer-docs

#: Build developer guide
developer-docs:
	$(MAKE) -C docs html
