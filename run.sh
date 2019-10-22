#!/bin/bash
# Source our enviornment
source ./bin/activate

# Check to build
python setup.py build_ext --inplace

# Actually run the code
python main.py

# Deactivate the source
deactivate
