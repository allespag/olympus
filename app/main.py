import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


class Tag(BaseModel):
    name: str
    audio: str


# Temporary
a = Tag(name="acteur", audio="act_g_4.mp3")
b = Tag(name="nourris", audio="Dem_ev_2.mp3")
TAGS = {
    a.name: a,
    b.name: b,
}


@app.get("/")
async def root(request: Request):
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


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8036, reload=True)
