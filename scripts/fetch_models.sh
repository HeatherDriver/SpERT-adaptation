#!/usr/bin/env bash
spert_path="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; cd ../spert ; pwd -P )"

mkdir -p $spert_path/data
mkdir -p $spert_path/data/models

wget -r -nH --cut-dirs=100 --reject "index.html*" --no-parent http://lavis.cs.hs-rm.de/storage/spert/public/models/scierc/ -P $spert_path/data/models/scierc