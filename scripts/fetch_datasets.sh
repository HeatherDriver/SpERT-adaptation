#!/usr/bin/env bash
spert_path="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; cd .. ; pwd -P )"

mkdir -p $spert_path/data
mkdir -p $spert_path/data/datasets

wget -r -nH --cut-dirs=100 --reject "index.html*" --no-parent http://lavis.cs.hs-rm.de/storage/spert/public/datasets/scierc/ -P $spert_path/data/datasets/scierc