#!/bin/bash

BLUR=0x2
if [[ $# -eq 1 ]]; then
    BLUR=$1
fi

mkdir -p data/orig/resized
mkdir -p data/orig/blured
mkdir -p data/pokemons

for file in ./data/orig/*.png; do
    filename=`basename $file`
    filename="${filename%.*}"
    convert -resize 256x256 $file ./data/orig/resized/$filename.jpg
    convert ./data/orig/resized/$filename.jpg -blur $BLUR ./data/orig/blured/$filename.jpg
    convert +append ./data/orig/resized/$filename.jpg ./data/orig/blured/$filename.jpg ./data/pokemons/$filename.jpg
done

rm -rf ./data/orig/resized ./data/orig/blured
