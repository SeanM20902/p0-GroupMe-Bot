import requests
import time
import json
import os
import random
from art import *
from dotenv import load_dotenv

load_dotenv()

BOT_ID = os.getenv("BOT_ID")
GROUP_ID = os.getenv("GROUP_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
LAST_MESSAGE_ID = None


def send_message(text, attachments=None):
    """Send a message to the group using the bot."""
    post_url = "https://api.groupme.com/v3/bots/post"
    data = {"bot_id": BOT_ID, "text": text, "attachments": attachments or []}
    response = requests.post(post_url, json=data)
    return response.status_code == 202


def get_group_messages(since_id=None):
    """Retrieve recent messages from the group."""
    params = {"token": ACCESS_TOKEN}
    if since_id:
        params["since_id"] = since_id

    get_url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    response = requests.get(get_url, params=params)
    if response.status_code == 200:

        # ----------- getting the last msg
        # doing [-1] to get the last message doesnt actually work; have to get by last created
        max_created = 0
        max_idx = 0
        for i, message in enumerate(response.json().get("response", {}).get("messages", [])):
            if message['created_at'] > max_created:
                max_created = message['created_at']
                max_idx = i
        last_message = response.json().get("response", {}).get("messages", [])[max_idx]

        # ----------- task 1
        # respond to my 'task 1' messages with 'task 1 response'
        # my user id is 87734062
        # only respond to the last message
        if last_message["sender_id"] == '87734062' and last_message["text"] == 'task 1':
            send_message("task 1 response")

        # ----------- task 2
        # bot user id is 883779; dont respond to self
        if last_message["sender_id"] != '883779':
            if last_message["text"] == 'good morning': send_message("good morning")
            elif last_message["text"] == 'good night': send_message("good night")

        # ----------- task 3
        # rock paper scissors simulator
        # user plays one of rock, paper, or scissors
        # bot responds with a random choice from those as well
        # prints back the winner based on user and bot choices
        options = ['rock', 'paper', 'scissors']
        # user goes
        user_choice = last_message["text"]
        if last_message["sender_id"] != '883779' and user_choice in options:
            # bot goes
            bot_choice = options[random.randint(0,2)]
            send_message(bot_choice)
            # who wins
            if bot_choice == user_choice:
                send_message("Tie!")
            elif bot_choice == 'rock' and user_choice == 'scissors':
                send_message("I win!")
            elif bot_choice == 'rock' and user_choice == 'paper':
                send_message("You win!")
            elif bot_choice == 'scissors' and user_choice == 'rock':
                send_message("You win!")
            elif bot_choice == 'scissors' and user_choice == 'paper':
                send_message("I win!")
            elif bot_choice == 'paper' and user_choice == 'rock':
                send_message("I win!")
            elif bot_choice == 'paper' and user_choice == 'scissors':
                send_message("You win!")

        # ----------- task 3 EC additional feature: text art
        # will print text art of string if it exists in the library and preceded by 'art: '
        if last_message["text"][:4] == 'art:':
            try:
                send_message(art(last_message["text"][5:]))
            except:
                send_message("no art for that ):")

        # this shows how to use the .get() method to get specifically the messages but there is more you can do (hint: sample.json)
        return response.json().get("response", {}).get("messages", [])
    return []


def process_message(message):
    """Process and respond to a message."""
    global LAST_MESSAGE_ID
    text = message["text"].lower()

    # i.e. responding to a specific message (note that this checks if "hello bot" is anywhere in the message, not just the beginning)
    # if "hello bot" in text:
    #     send_message("sup")

    LAST_MESSAGE_ID = message["id"]


def main():
    global LAST_MESSAGE_ID
    # this is an infinite loop that will try to read (potentially) new messages every 10 seconds, but you can change this to run only once or whatever you want
    while True:
        messages = get_group_messages(LAST_MESSAGE_ID)
        for message in reversed(messages):
            process_message(message)
        time.sleep(10)


if __name__ == "__main__":
    main()

