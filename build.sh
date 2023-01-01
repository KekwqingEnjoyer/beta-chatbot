set -o errexit

pip install --upgrade pip
pip install -U pip setuptools wheel
pip install PyYAML==3.13 --use-pep517
pip install -r requirements.txt --use-pep517