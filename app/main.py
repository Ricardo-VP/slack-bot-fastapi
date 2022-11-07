from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import slack

from .config.env_manager import get_settings

env_manager = get_settings()

app = FastAPI(title='Slack Bot - API')
client = slack.WebClient(env_manager.SLACK_TOKEN)

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
