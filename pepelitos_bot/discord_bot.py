import json
import os

class discord_bot:
    def __init__(self):
        path = os.path.dirname(__file__)
        with open(path + r"\bot.config", "r") as file:
            config = json.load(file)
            self.key = config["api_key"]

    def sample(self):
        print("this is the execution of the sample function")
        return self.key