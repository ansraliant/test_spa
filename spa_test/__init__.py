"""CheckFront is web front-end for CodeCheck service"""

import os

import aiofiles
from fastapi import FastAPI
from fastapi.logger import logger
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from spa_test.resources import api_rt

_app = FastAPI()

_app.mount(
    "/static", StaticFiles(directory=f"dist/static"), name="static"
)


_app.include_router(api_rt, prefix="/api")


async def send_index() -> bytes:
    """Return the main page"""
    async with aiofiles.open(
        os.path.join("dist", "index.html"), mode="r"
    ) as index_f:
        return await index_f.read()


@_app.get("/", response_class=HTMLResponse)
async def index() -> HTMLResponse:
    """Register Vue Application"""
    return HTMLResponse(content=await send_index())


@_app.get("/{path:path}")
async def fallback(path) -> HTMLResponse:
    """
    Fallback URI. This gives both flexibility and responsibility
    of Routing to Vue.JS application side
    """
    logger.debug(f"Sinking path: {path}")
    # Will bring user to SPA. You may want to show 404 later
    # for the paths irrelevant
    return await index()


app = _app
