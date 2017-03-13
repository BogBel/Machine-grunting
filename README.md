# Machine-grunting

## Python instalation
sudo add-apt-repository ppa:fkrull/deadsnakes

sudo apt-get update

sudo apt-get install python3.5

## Env configuring

virtualenv -p /usr/bin/python3.5 .env/

source .env/bin/activate

python -m pip install --upgrade pip

pip install -r requirements.txt
