from collections import Counter

from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates/")
app = FastAPI()


def count_words(text: str) -> list[tuple[str, int]]:
    "core api logic: count word occurrences is a string"
    words = text.strip().split(" ")
    return Counter(words).most_common()


@app.get("/")
def form_get(request: Request):
    return templates.TemplateResponse(
        "index.html",
        context={"request": request},
    )


@app.post("/")
def form_post(request: Request, text_input: str = Form(...)):
    result = count_words(text_input)
    return templates.TemplateResponse(
        "index.html", context={"request": request, "result": result}
    )
