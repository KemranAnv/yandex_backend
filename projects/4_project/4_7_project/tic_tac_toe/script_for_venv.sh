#Script to create venv

python -m venv venv
# Creating virtual evvironment
# python - run interpreter Python
# -m venv - call module venv (-m : module)
# venv - name of the folder, where virtual environmen will be created

source venv/Scripts/activate
# Activating created virtual environment
# source - command to run script

python -m pip install --upgrade pip
# upgrading package pip
