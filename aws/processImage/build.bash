#!/bin/bash
rm -r function
rm processImage.zip
mkdir function
cp lambda_function.py function
cp comprehend.py function
cp textract.py function

pip install \
    --platform manylinux2014_x86_64 \
    --target=function \
    --implementation cp \
    --python 3.9 \
    --only-binary=:all: --upgrade \
    Pillow
cd function

zip -r ../processImage.zip .
cd ..
rm -r function
