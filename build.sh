set -o errexit

pip install --upgrade pip
pip install -r requirements.txt --use-pep517
pip install PyYAML==6.0