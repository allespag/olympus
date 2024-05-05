import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from olympus.tags import TagCollection
from olympus.utils import get_project_root

app = FastAPI()

STATIC_FOLDER_NAME = "static"
STATIC_FOLDER = get_project_root() / STATIC_FOLDER_NAME

app.mount(
    f"/{STATIC_FOLDER_NAME}",
    StaticFiles(directory=STATIC_FOLDER),
    name=STATIC_FOLDER_NAME,
)

templates = Jinja2Templates(directory=get_project_root() / "templates")


TAGS = TagCollection.from_json(STATIC_FOLDER / "data" / "tags.json")


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
        request=resquest,
        name="tag.html",
        context={"tags": TAGS, "tag": TAGS[tag_name]},
    )


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(STATIC_FOLDER / "images" / "favicon.ico")


@app.exception_handler(404)
async def not_found_exception(_, __):
    return RedirectResponse("/")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8036, reload=True)
