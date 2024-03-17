import nltk
from nltk.chat.util import Chat
botname = input("Name your bot: ")
pairs = [
    [
        r"hello|hi|hey",
        ["Hello! How can I help you?",
         "Hello! How are you doing today?"]
    ],
    [
        r"i am fine",
        ["Good to hear that. How can I help you?"]
    ],
    [
        r"which is the best computer language?",
        ["Python", "Java", "Dart"]
    ],
    [
        r"where do you live?",
        ["nowhere"]
    ],
    [
        r"what is your name?",
        [f"My name is {botname}."]
    ],
    [
        r"quit",
        ["Goodbye!"]
    ]
]
print(f"Welcome! It's me {botname}, your chatbot.")
chat = Chat(pairs)
while True:
    me = input("You: ")
    response = chat.respond(me)
    print(f"{botname}:", response)
    if me == "quit":
        break
