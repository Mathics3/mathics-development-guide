.PHONY: all png

all: png
	make -C ../..

#: Build PNG graphics
png: evaluate-format-pipeline.png

evaluate-format-pipeline.png: evaluate-format-pipeline.svg
	cat $< | inkscape -p --export-type=png  > $@
