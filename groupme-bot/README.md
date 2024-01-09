# smohs-p0 bot

## How to run
- Clone this repo and cd into this directory
- Create venv with `python3 -m venv venv`
- Activate the venv
 - For mac/linux: `source venv/bin/activate`
 - For windows: `venv\Scripts\activate`
 - To deactivate the venv: `deactivate` 
- Install dependencies with `pip install -r requirements.txt`
- Finally, to run the bot: `python3 bot.py`

## Responds to you
- The bot will respond to a message with the text "task 1" with "task 1 response"
- It will only do this for "task 1" messages you send

## Good morning / good night
- The bot will respond to messages with the text "good morning" or "good night" with "good morning" or
"good night", followed by the sender's name.
 - For example, if a user with the name "User" sends "good morning", the bot will respond with "good morning, User". It will do the same for "good night"

## Rock paper scissors simulator
- If the user sends "rock", "paper", or "scissors", the bot will respond with a random selection from the same options
- It then evaluates who won the game based on the choices and prints the result
 - For example, if a user messages "rock", and the bot messages "paper", the bot sends the message "I win!"
 - If the user messages "rock" and the bot messages "scissors", the bot sends the message "You win!"
 - If the user messages "rock" and the bot messages "rock", the bot sends the message "You win!"

## Text art generator
- If the user sends a message with "art:" at the beginning, the bot will send text art of the word that comes after "art:"
 - For example, if the user sends the message: "art: angry", the bot will respond with "ლ(ಠ益ಠ)ლ"
- If it does not have the relevant text art in its library, it will send the message "no art for that ):"
- Source: https://github.com/sepandhaghighi/art?tab=readme-ov-file#ascii-text
