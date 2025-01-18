#!/usr/bin/env bash

set -e

version=$(grep -oP '__version__ = "\K([^"]+)' toy/_version.py)
gh release create $version wheelhouse/*
