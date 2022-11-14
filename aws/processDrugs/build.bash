#!/bin/bash
rm -r function
rm processDrugs.zip
mkdir function
cp lambda_function.py function
cp util.py function

pip install \
    --platform manylinux2014_x86_64 \
    --target=function \
    --implementation cp \
    --python 3.9 \
    --only-binary=:all: --upgrade \
    requests
cd function

zip -r ../processDrugs.zip .
cd ..
rm -r function
cp *.zip tf