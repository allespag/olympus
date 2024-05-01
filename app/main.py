import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@app.get("/tag/{tag_name}")
async def tag(tag_name: str):
    return {"message": tag_name}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8036, reload=True)
