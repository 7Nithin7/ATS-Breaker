# ATS-Breaker

## Prerequisites:
1. Python 3.7.3 or above.
2. Poetry.

## Steps to Install :

1. Open cmd and go to the directory you want to install.
```cmd
git clone https://github.com/7Nithin7/ATS-Breaker.git
```
2. Go inside the repository.
```cmd
pip install poetry
```
3. Create virtual environment using poetry and install packages.
```cmd
poetry shell
poetry install
```
4. Download spacy's english pipeline.
```cmd
python -m spacy download en_core_web_sm
```
5. Running the application.
```cmd
python app.py
```


