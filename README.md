## INSTALATION

clone the repo with: `git clone https://github.com/neumann-mlucas/word_counter_ui`

to install the python packages with pipenv you can just run: `pipenv install`

or with pip and venv:

```
python -m venv venv
source venv/bin/activate
pip install -r requiriments.txt
```

## RUNNING THE WEB SERVER

```
pipenv shell # or: source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 80
```

## DEPLOY WITH DOCKER

```
docker build -t word-counter-ui .
docker run -d --name wordcounter -p 80:80 word_counter_ui
```
