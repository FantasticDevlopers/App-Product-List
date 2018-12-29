#!/usr/bin/env bash
sudo apt-get install virtualenv

virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt

pip install braintree --upgrade
