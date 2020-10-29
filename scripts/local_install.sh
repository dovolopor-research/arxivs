#!/usr/bin/env bash

pip uninstall arxivs -y

python setup.py clean
python setup.py install
