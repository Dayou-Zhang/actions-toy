#!/usr/bin/env bash

set -e

sudo apt -qq install \
    libblas-dev \
    gfortran

python -m pip install -U pip
pip install .
