import os

#from sympy import python
from anthropic import Anthropic
from dotenv import load_dotenv


load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit, type /summary to see a conversation summary)')
    system_message = "Your name is dotan you are a chef chat who halp kids learn about cooking and baking you teach them recipe and kitchen hacks and you are very polite and anser in a nice way. always finish your messege with a suggestion to tell them a joke. you should try to respond not too long its mportant and always use emojis."
    history = []
    total_tokens = 0

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
        print('History so far:', history)

        if user_input.lower() == "/summary":
            summary_prompt = "Summarize this conversation clearly. Include the main topics discussed and important details."


        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history        )
        
        total_tokens += response.usage.input_tokens + response.usage.output_tokens
        
        print(response)
        reply = response.content[0].text
        print(f"[Tokens used — In: {response.usage.input_tokens} | Out: {response.usage.output_tokens} | Total: {response.usage.input_tokens + response.usage.output_tokens}]")
        print(f"Total tokens used this conversation: {total_tokens}")
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()

#It's like a long-distance friend or one from another school. Every time we meet and tell stories about what happened, we have to remind them again: Yes, I'm in this group. Yes, Roni is the one I don't like. / I already told you about Noa...
#The ai will forget its previous answers the ai only remembers what the user said not what it answered 

#The program wont get the API key so the app wont start because it can't authenticate

#Typing exit won't close the program and The program keeps running and even sends exit to the ai

 #I thought there was a bug in the code, but it was actually my API key. After 

 #usage.output_tokens: The number of tokens the ai uses to write the reply
 #usage.input_tokens: The number of tokens the ai reads from your message and the chat history

 #Low temperature ai gives the same or very similar answer each time high temperature ai gives different and more creative answers 
 #The ai needs the full history because it doesnt remember past messages 
 # After 3 turns, the history contains 6 messages - input- output for every turn
#its like going on vacation the longer you stay the more money you spend
#the ai wont get my new message because its not in the history so it only sees the old chat the input tokens will also be lower or wont exist
#the ai will forget what it answered before and the tokens will grow slower because old answers are not saved
#nothing will change this line is only for me to see the history

# i had 2 main bugs/errors first i had extra tab that was so hard to find but easy to fix second my credit balance is too low so its not working anymore so it was hard for me to do the last part the reflection whithout runing it so i ask friend to try it on theyr computer 
#its how that you talk to your self in your mind. 
#It will no longer act like Dotan, the chef chatbot
#Delete the line: "always finish your message with a joke" from system_message
#i erased the jokes part it will still help with cooking, but it will stop adding a joke at the end of every response.
#The chatbot will still work normally, but the /summary command will stop working.
# didnt had any bugs or errors in the code 