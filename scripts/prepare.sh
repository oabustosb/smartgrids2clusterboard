#!/bin/bash
paths=`ls tmp_data/*.parquet`

for path in $paths; do
    echo $path
    python scripts/prepare.py --path $path
done
