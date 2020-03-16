from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import random
import json


class JokeTelling(Action):
    def name(self):
        return 'action_retrive_joke'

    def run(self, dispatcher, tracker, domain):
        jokes = tracker.get_slot('jokes')

        json_data = open(r'new_jokes.json', encoding="utf-8", errors='ignore').read()
        json_data_1 = json_data.replace('\t', '')
        json_data_2 = json_data_1.replace('\n', '')
        data = json.loads(json_data_2)
        response = random.choice(data['{}'.format(jokes)])['joke_content']

        dispatcher.utter_message("I have something really funny for you:{}".format(response))