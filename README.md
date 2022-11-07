# Slack Bot using Python and FastAPI 🐍 

## Requirements

- Python (I'm using Python 3.10)
- Slack
    - An workspace -> https://slack.com/get-started#/createnew
    - An slack app -> https://api.slack.com/apps
      - How to create one -> https://python.plainenglish.io/how-to-set-up-send-messages-with-a-slack-bot-in-python-f6b6bf06be72
- HTTP Client (I'm using Postman)

## How to run the app

- Install the requirements
```
python -m pip install -r requirements.txt
```

- Create an .env file and set the SLACK_TOKEN value
```
SLACK_TOKEN=Here paste your Bot User OAuth Token
```

- Run the app
```
python runner.py
```

## Test the app using the HTTP Client
![image](https://user-images.githubusercontent.com/71697096/200252556-74d6d743-db50-46f7-a57c-d89646d163c0.png)
