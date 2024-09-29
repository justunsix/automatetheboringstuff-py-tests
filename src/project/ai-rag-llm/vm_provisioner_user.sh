#!/bin/bash
set -e

# Add command to .bashrc to change directory on login
if ! grep -q "cd /vagrant" /home/vagrant/.bashrc; then
  echo 'cd /vagrant' >> /home/vagrant/.bashrc
fi

cd /vagrant/ollama-repo-changes

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Set environment variables for pip to use the pytmp directory
# due to /tmp being small on VM
export TMPDIR=$(pwd)/pytmp/
export PIP_CACHE_DIR=$(pwd)/pytmp/cache

# Create the directories if they don't exist
mkdir -p $TMPDIR $PIP_CACHE_DIR

# Install the requirements
pip install --cache-dir $PIP_CACHE_DIR -r requirements.txt

# Add command to .bashrc to activate the virtual environment on login
echo "source /vagrant/ollama-repo-changes/.venv/bin/activate" >> /home/vagrant/.bashrc

echo -e "-- environment setup complete"
