from langchain.chat_models import init_chat_model 
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage 
from dotenv import load_dotenv 

load_dotenv() 

model = init_chat_model( model="mistral-small-2506", temperature="0.9" ) 

print("Choose your AI Mood.\n Press 1 for Angry mood.\n Press 2 for Funny mood.\n Press 3 for Sad mood.") 
ch = int(input("Enter your choice: ")) 
if(ch == 1): 
    mood = "You are an Angry AI agent. You respond aggressively and impatiently." 
elif(ch == 2): 
    mood = "You are a Funny AI agent. You respond with humor and joke." 
elif(ch == 3): 
    mood = "You are a Sad AI agent. You respond with with sad and sorrow." 
else: 
    print("Enter correct choice")

# Storing the prompts and response in order to maintain a chat memory 
messages = [ SystemMessage(content=mood) ] 

print("--------- Welcome! Enter '0' to exit ---------") 

while True: 
    prompt = input("You: ") 
    messages.append(HumanMessage(content=prompt)) 
    if(prompt == "0"): 
        break 
    response = model.invoke(messages) 
    messages.append(AIMessage(content=response.content)) 
    print(f"AI: {response.content}") 

# Printing the messages and response when pressed 0 
print(messages)