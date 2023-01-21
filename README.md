## INSTALATION

clone the repo: `git clone https://github.com/neumann-mlucas/word_counter_ui`

to install the python packages with pipenv you can just run: `pipenv install`
or with pip and venv:

```
python -m venv venv
./venv/Scripts/activate
pip install -r requiriments.txt
```

# RUNNING THE WEB SERVER

```
pipenv shell
uvicorn main:app --host 0.0.0.0 --port 8000
```

- unit tests
- pre-commit hocks
- docker file
- readme
- make textarea width dynamic
