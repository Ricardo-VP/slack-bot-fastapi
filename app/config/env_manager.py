import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    SLACK_TOKEN: str = os.getenv('SLACK_TOKEN') or None


def get_settings() -> Settings:
    return Settings()
