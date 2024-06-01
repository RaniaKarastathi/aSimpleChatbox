import re
import random
import tkinter as tk
from tkinter import scrolledtext

patterns_responses = {
    r'hello|hi|hey': ['Hello!What is your question?', 'Hi there!What is your question?', 'Hey!What is your question?'],
    r'quit|exit': ['Goodbye!', 'Bye!', 'Take care!'],
    r'^(What|How)\s(is)\s(your)\s(name\?)': ['I am a chatbot designed to answer your questions!'],
    r'What is the best vacation destination?': ['The best holiday destination depends on your interests and preferences. Some prefer beaches and sun, so a tropical destination such as Bali or Mauritius may be an ideal choice. Others are interested in cultural experience, so a European city such as Paris or Florence may be more suitable. Additionally, for natural experiences and adventure, a trip to a national park such as the Grand Canyon or New Zealand΄s Captive Park may be unforgettable. Ultimately, the best destination is one that will give you the experience you΄re looking for and create memories that will last a lifetime.'],
    r'How are you (doing|feeling)?' : ['I am fine thanks for asking'],
    r'Tell me about the Eiffel Tower' : ['The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. It is named after the engineer Gustave Eiffel, whose company designed and built the tower from 1887 to 1889'],
    r'Tell me a joke' : ['Things are not always #000000 and #FFFFFF','Why do Java programmers have to wear glasses? Because they do not C#'],
}


def respond(input_text):
    for pattern, responses in patterns_responses.items():
        match = re.search(pattern, input_text, re.IGNORECASE)
        if match:
            response = random.choice(responses)
            if '{0}' in response:
                return response.replace('{0}', match.group(0))
            else:
                return response
    return "I'm not sure how to respond to that."

def send_message():
    user_input = input_box.get("1.0", 'end-1c')
    if user_input.lower() in ['quit', 'exit']:
        response_text.insert(tk.END, "Bot: " + respond(user_input) + "\n")
        response_text.insert(tk.END, "You: " + user_input + "\n")
        root.after(2000, root.quit) 
    else:
        response_text.insert(tk.END, "You: " + user_input + "\n")
        response_text.insert(tk.END, "Bot: " + respond(user_input) + "\n")
    input_box.delete("1.0", tk.END)

root = tk.Tk()
root.title("Chatbot")
root.configure(bg="#edd5d5")  # Set background color
response_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15, bg="#ffffff", fg="#057366", font=("Arial", 10))
response_text.grid(row=0, column=0, padx=10, pady=10)

input_box = tk.Text(root, wrap=tk.WORD, width=50, height=3, bg="#ffffff", fg="#057366", font=("Arial", 10))
input_box.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message, bg="#e17ff0", fg="#ffffff", font=("Arial", 10), relief=tk.FLAT)
send_button.grid(row=2, column=0, padx=10, pady=10, sticky="e")

response_text.insert(tk.END, "Bot: Welcome! Feel free to ask me anything.\n")

root.mainloop()
