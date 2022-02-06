.PHONY: all

all: evaluate-format-pipeline.png

evaluate-format-pipeline.png: evaluate-format-pipeline.svg
	cat $< | inkscape -p --export-type=png  > $@
