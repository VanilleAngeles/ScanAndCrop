#!/bin/bash
#
for x in "$@"
do
	python3 /home/patrick/.local/share/nemo/scripts/crop.py "$x"
done
