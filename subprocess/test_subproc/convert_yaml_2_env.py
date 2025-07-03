#!/usr/bin/env python3

from pathlib import Path
from ruamel.yaml import YAML

file_in = Path("Engineering/subprocess/test_subproc/config.yaml")

yaml = YAML()
env_data = yaml.load(file_in)["env_variables"]
env_output = "".join([f"{k}={v!r}\n" for k, v in env_data.items()])

# Save the output to a temporary file
with open("Engineering/subprocess/test_subproc/env_variables.sh", "w") as f:
    f.write(env_output)

