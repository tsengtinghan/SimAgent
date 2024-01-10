import openai
import os
from dotenv import load_dotenv
from memory import ShortTermMemory, LongTermMemory

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class Agent():
    def __init__(self, name, description):
        self.name = name
        self.description = description  
        self.memories = ShortTermMemory()
        self.goals = []
        self.actions = []


        

if __name__ == "__main__":
    agent = Agent("bob", "a helpful assistant")
    while True:
        UserNeed = input("hi, I'm {}, your personal ai assistant. What do you want to do? ".format(agent.name))
        if UserNeed.lower() == 'exit':
            break
        if len(agent.memories.memory):
            UserNeedWithMemory = UserNeed + "\nHere is the previous conversation, please read them before you reply with an answer\n".join(agent.memories.memory)
        else: UserNeedWithMemory = UserNeed
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "{}".format(UserNeedWithMemory)}
            ],
            temperature = 0,
        )
        print(response['choices'][0]['message']['content'])
        agent.memories.add("The User: " + UserNeed + "\nThe Assistant: " + response['choices'][0]['message']['content'] + "\n")
        print(UserNeedWithMemory)
    print(agent.memories.memory)
    