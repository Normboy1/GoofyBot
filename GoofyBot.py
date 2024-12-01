from transformers import GPT2LMHeadModel, GPT2Tokenizer
import random
from gtts import gTTS
import os

# Load pre-trained model and tokenizer
model_name = "gpt2"  # You can use a larger model like 'gpt2-medium', 'gpt2-large', etc.
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
language = 'en'

# Set the chatbot's personality
greeting_responses = ["Hey there!", "Hello!", "Hi, how's it going?", "Hey, what's up?"]
farewell_responses = ["Goodbye!", "See you later!", "Take care!", "Bye! Hope to chat again soon!"]
default_responses = [
    "Hmm, interesting. Tell me more!",
    "I see! Could you elaborate?",
    "Wow, that's cool! I'm all ears.",
    "That's awesome! What else?"
]

# Function to generate a response
def generate_response(prompt):
    # Encode the prompt to get token IDs
    inputs = tokenizer.encode(prompt, return_tensors='pt')

    # Generate a response from the model
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2, pad_token_id=tokenizer.eos_token_id)

    # Decode the response from token IDs to text
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Clean the response a bit (remove the prompt part)
    return response[len(prompt):].strip()

# Function for handling chatbot conversation with personality
def chatbot_conversation():
    print("Chatbot: Hey there! I'm your friendly chatbot. What's up?")

    while True:
        user_input = input("You: ")

        # Handle exit condition
        if user_input.lower() in ['bye', 'exit', 'quit', 'goodbye']:
            print(f"Chatbot: {random.choice(farewell_responses)}")
            myobj = gTTS(text=random.choice(farewell_responses), lang=language, slow=False)
            myobj.save("response.mp3")
            os.system("start response.mp3")
            break
        
        # Handle greetings
        elif any(greeting.lower() in user_input.lower() for greeting in ["hi", "hello", "hey"]):
            response = random.choice(greeting_responses)
            print(f"Chatbot: {response}")
            myobj = gTTS(text=response, lang=language, slow=False)
            myobj.save("response.mp3")
            os.system("start response.mp3")
        
        # Respond with default response or personalized response
        else:
            response = generate_response(user_input)
            if response:
                print(f"Chatbot: {response}")
                myobj = gTTS(text=response, lang=language, slow=False)
                myobj.save("response.mp3")
                os.system("start response.mp3")
            else:
                response = random.choice(default_responses)
                print(f"Chatbot: {response}")
                myobj = gTTS(text=response, lang=language, slow=False)
                myobj.save("response.mp3")
                os.system("start response.mp3")

if __name__ == "__main__":
    chatbot_conversation()
