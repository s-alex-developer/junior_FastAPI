from fastapi import FastAPI

from routers.routers_api import router_api
from routers.routers_web import router_web

app = FastAPI()

app.include_router(router_api)
app.include_router(router_web)

