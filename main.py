from agent import Agent

if __name__ == "__main__":
    agent = Agent("bob", "a helpful assistant", "memory_index")
    while True:
        user_input = input(f"Hi, I'm {agent.name}, your personal AI assistant. What do you want to do? ")
        if user_input.lower() == 'exit':
            break
        
        # ... Implement interaction logic ...
        response = agent.respond(user_input)
        print(response)
