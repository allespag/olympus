from pathlib import Path
from random import choice

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

app = FastAPI()

STATIC_FOLDER_NAME = "static"
STATIC_FOLDER = Path(f"./{STATIC_FOLDER_NAME}")

app.mount(
    f"/{STATIC_FOLDER_NAME}",
    StaticFiles(directory=STATIC_FOLDER_NAME),
    name=STATIC_FOLDER_NAME,
)


templates = Jinja2Templates(directory="templates")


COLORS = ["#146173", "#96332D", "#CBAE57", "#72752D"]


class Tag(BaseModel):
    name: str
    audio: str
    content: str
    color: str = Field(default_factory=lambda: choice(COLORS))


# Temporary
a = Tag(name="acteur", audio="act_g_4.mp3", content="PLACEHOLDER")
b = Tag(
    name="nourri",
    audio="Dem_ev_2.mp3",
    content="Que peut-on désirer de mieux qu'un peuple bien nourri ?",
)
TAGS = {
    a.name: a,
    b.name: b,
}


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="base.html",
        context={"tags": TAGS},
    )


@app.get("/tag/{tag_name}")
async def tag(resquest: Request, tag_name: str):
    return templates.TemplateResponse(
        request=resquest, name="tag.html", context={"tags": TAGS, "tag": TAGS[tag_name]}
    )


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(STATIC_FOLDER / "images" / "favicon.ico")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8036, reload=True)
