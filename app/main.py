from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .config.env_manager import get_settings
from .routers import slack

env_manager = get_settings()

app = FastAPI(title='Slack Bot - API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
async def root():
    return {"message": "Slack Bot - API"}

app.include_router(
    slack.router,
    prefix='/slack',
    tags=['slack']
)
