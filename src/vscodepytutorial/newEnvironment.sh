python -m venv .venv 

# Activate the new environment
.venv\scripts\activate

# Don't use with Anaconda distributions because they include matplotlib already.

# Windows (may require elevation)
python -m pip install matplotlib

# Deactivate the environment
deactivate

