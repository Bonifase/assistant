import json
import random

import torch

from bot_utils import bag_of_words, tokenize
from models import NeuralNetFeed

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
with open("bot/data/intents.json", "r") as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNetFeed(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


def shopping_assistant(sentence):
    bot_name = "AssistantBot"
    print("Let's chat!")
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]
    probabilities = torch.softmax(output, dim=1)
    probability = probabilities[0][predicted.item()]
    if probability > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                print(f'{bot_name}: {random.choice(intent["responses"])}')
    else:
        print(f"{bot_name}: I do not understand...")


while True:
    sentence = input("You: ")
    if sentence == "Quit":
        break
    shopping_assistant(sentence)
