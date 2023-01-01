set -o errexit

pip install --upgrade pip
sudo apt install libpython3.10-dev
pip install PyYAML==6.0 --use-pep517
pip install -r requirements.txt --use-pep517