# Create an mprocs.yaml file from a Makefile to run targets in mprocs, yaml is output to the same directory as the Makefile
# - Makefile specified by the path in the first argument e.g. python makefile-to-mprocs.py path/to/Makefile
# - Each line with a target in the Makefile has a colon followed by a comment with two hashmarks (##)
#   - Follows template from https://victoria.dev/blog/how-to-create-a-self-documenting-makefile/
# Use case:
# Created to help use mprocs to perform repetitive or long running processes in Makefiles

import re
import sys
import os

makefile_path = sys.argv[1]
# Get the directory of the makefile
makefile_dir = os.path.dirname(makefile_path)
# Join the directory with output mprocs.yaml
mprocs_path = os.path.join(makefile_dir, 'mprocs.yaml')

# extra modules below need to be installed
try:
    import yaml
except ModuleNotFoundError:
    print(
        "You need to install the yaml module. (https://pypi.org/project/PyYAML/)",
        file=sys.stderr,
    )
    print(
        "If you have pip (normally installed with python), run this command in a terminal (cmd): pip install PyYAML",
        file=sys.stderr,
    )
    sys.exit()

def makefile_to_mprocs(makefile_path):
    with open(makefile_path, 'r') as f:
        lines = f.readlines()
      
    # match words separated by dashes or spaces followed by a colon, space, and two hashmarks
    targets = [re.match(r'^[\w\s-]+:.*##', line).group().split(':')[0].strip() for line in lines if re.match(r'^[\w\s-]+:.*##', line)]

    mprocs = {
        'procs': {target: {'shell': f'make {target}', 'autostart': False} for target in targets}
    }

    with open(mprocs_path, 'w') as f:
        f.write(yaml.dump(mprocs))

makefile_to_mprocs(makefile_path)
