set -o errexit

pip install --upgrade pip
pip install PyYAML==6.0
pip install -r requirements.txt --use-pep517