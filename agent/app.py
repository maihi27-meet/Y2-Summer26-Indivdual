import os

#from sympy import python
from anthropic import Anthropic
from dotenv import load_dotenv


load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is dotan you are a chef chat who halp kids learn about cooking and baking you teach them recipe and kitchen haks and you are very polite and anser in a nice way. always finish your messege with a joke"
    history = []

    while True:
        print(f"[{len(history) // 2 + 1}] You: ", end="")
        user_input = input('>> ')
        if user_input.lower() == "reset":
        history = []
        print("Conversation history cleared!")
            continue
        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()

#It's like a long-distance friend or one from another school. Every time we meet and tell stories about what happened, we have to remind them again: Yes, I'm in this group. Yes, Roni is the one I don't like. / I already told you about Noa...
#The ai will forget its previous answers the ai only remembers what the user said not what it answered 

#The program wont get the API key so the app wont start because it can't authenticate

#Typing exit won't close the program and The program keeps running and even sends exit to the ai

 #I thought there was a bug in the code, but it was actually my API key. After fixing the key, the program worked