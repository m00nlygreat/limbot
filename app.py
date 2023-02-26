# import logging
# logging.basicConfig(level=logging.DEBUG)

# from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError

# slack_token = '' # Bot OAuth Token
# client = WebClient(token=slack_token)

# try:
#     response = client.chat_postMessage(
#         channel="C04RC8P298C", # Channel ID
#         text="안녕하세요. 저는 혜림봇입니다. 최적의 점심식사를 추천합니다."
#     )
# except SlackApiError as e:
#     assert e.response["error"]



import os
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    # token="xoxb-2960086376882-4845292845015-1cvnn83SwwdIR3Sg7JOahsmy",
    # signing_secret="b9c4c08e57b5d77dc5416cae38c469bb",
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
)


# Listens to incoming messages that contain "hello"
# To learn available listener method arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("안녕")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"안녕하세요! <@{message['user']}>님!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "눌러보세요"},
                    "action_id": "button_click",
                },
            }
        ],
        text=f"안녕하세요. <@{message['user']}>님!",
    )


@app.action("button_click")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}>님, 버튼을 누르셨군요!")


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))