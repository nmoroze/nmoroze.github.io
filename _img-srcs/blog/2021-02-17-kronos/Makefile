DRAWIO ?= /Applications/draw.io.app/Contents/MacOS/draw.io

OUTDIR := ../../../assets/img/blog/2021-02-17-kronos

DIAGRAMS := $(wildcard *.drawio)
FIGS := $(patsubst %.drawio,$(OUTDIR)/%.png,$(DIAGRAMS))

all: $(FIGS)

$(OUTDIR)/%.png: %.drawio
	$(DRAWIO) $< -x -f png -o $@ --crop --transparent
