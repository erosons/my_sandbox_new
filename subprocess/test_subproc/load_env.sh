#!/bin/bash

# Run the Python script to generate the environment variables file
python3 Engineering/subprocess/test_subproc/convert_yaml_2_env.py

# Source the generated environment variables file
source env_variables.sh
source ~/.zshrc
# Check if variables are set
echo "variable1: $variable1"
echo "variable2: $variable2"
echo "variable3: $variable3"