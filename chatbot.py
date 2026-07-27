from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

model = init_chat_model(
    model="mistral-small-2506",
    temperature="0.9"
)

# Storing the prompts and response in order to maintain a chat memory
messages = []

print("--------- Welcome! Enter '0' to exit ---------")
while True:
    prompt = input("You: ")
    messages.append(prompt)
    if(prompt == "0"):
        break
    response = model.invoke(messages)
    messages.append(response.content)
    print(f"AI: {response.content}")

# Printing the messages and response when pressed 0
print(messages)