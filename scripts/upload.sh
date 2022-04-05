#!/bin/bash
paths=`ls data/*.json`

for path in $paths; do
    python scripts/upload.py --path $path
done
