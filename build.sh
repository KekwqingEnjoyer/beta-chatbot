set -o errexit

pip install --upgrade pip
pip install PyYAML==6.0 --use-pep517
pip install -r requirements.txt --use-pep517