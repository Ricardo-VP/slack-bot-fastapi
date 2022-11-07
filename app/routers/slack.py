###
# Libraries
###

from fastapi import APIRouter
import slack

from ..models.slack import SlackMessage
from ..config.env_manager import get_settings

###
# Config
###

router = APIRouter()
env_manager = get_settings()

client = slack.WebClient(env_manager.SLACK_TOKEN)

###
# Routes
###


@router.get('/user/{email}')
async def get_user(email: str) -> dict:
    user = client.users_lookupByEmail(email=email).data

    return {
        'message': 'success',
        'user': user['user']
    }


@router.post('/msg/{user_email}')
async def send_message_to_user(user_email: str, message: SlackMessage) -> dict:
    user = client.users_lookupByEmail(email=user_email).data['user']
    user_name = user['real_name']

    client.chat_postMessage(
        channel=user['id'],
        text=f'Hi, {user_name}. {message.text}'
    )

    return {
        'message': 'success',
    }
