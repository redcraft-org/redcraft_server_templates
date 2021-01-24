#!/bin/bash

rm -rf env
python3 -m venv env
source env/bin/activate
pip install wheel
pip install -r requirements.txt
