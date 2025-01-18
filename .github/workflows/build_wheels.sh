#!/usr/bin/env bash

set -e

python -m pip install -U pip
pip install cibuildwheel
# CIBW_ARCHS="x86_64" CIBW_BUILD="cp3{9,1?}-manylinux*" python -m cibuildwheel --output-dir wheelhouse
CIBW_ARCHS="x86_64" CIBW_BUILD="cp313-manylinux*" python -m cibuildwheel --output-dir wheelhouse
