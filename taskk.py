def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye!"
    elif "name" in user_input:
        return "I'm a simple chatbot!"
    else:
        return "Sorry, I didn't understand that."

def run_chatbot():
    print("Chatbot: Hi! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break

run_chatbot()