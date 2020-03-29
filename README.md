# Funny Conversational-Chatbot
It's a funny ML based conversational chatbot which tells some text jokes to the users when they feel sad. It is a very basic conversational bot but it will definitely help others to start building one.

## RASA components for developing a ML based chatbot

**RASA**, An opensource bot building framework, is used to build this bot.
RASA is divided into two major parts in terms of developing a chatbobt.
1. **RASA NLU** - It determines the intent of the user and also captures entities if there are any
2. **RASA CORE** - It works as a dailogue managment for bot and keep track of a conversation with the user.

### RASA NLU
1. nlu.md - consists training data for intent classification and entiity extraction
            
            ref:-https://rasa.com/docs/rasa/nlu/training-data-format/
            
### RASA CORE
1. stories.md - Rasa stories are a form of training data used to train the Rasa’s dialogue management models.
              - Rather than a bunch of if/else statements, it uses a machine learning model trained on example conversations                 to decide what to do next.
                
                ref:- https://rasa.com/docs/rasa/core/stories/
2. domain.yml - The Domain defines the universe in which your assistant operates. It specifies the intents, entities, slots,                 and actions your bot should know about. Optionally, it can also include responses for the things your bot                     can say.
                
                ref:- https://rasa.com/docs/rasa/core/domains/
### configuration
1. config.yml - consists configuration pipeline for the training of NLU and CORE
              - Choosing an NLU  and a CORE pipeline allows you to customize your model and finetune it on your dataset.
                
                nlu_config_reference:- https://rasa.com/docs/rasa/nlu/choosing-a-pipeline/
                core_config_reference:- https://rasa.com/docs/rasa/core/policies/

## How to use this chatbot on your computer
1. Clone or download this repo into your computer
2. make sure to have all the dependency in your computer
3. set  your working directory to this downloaded folder in termial
4. run this command:- **rasa run actions**
                    - this will start a port on 5055 which will handl custom actions
5. open another terminal and do the same as stated in step 3
6. run this comand:- **rasa shell --endpoints endpoints.yml**

**B00000M** Are ready to freshen up!!!!!!
Now you can talk to funny chatbot. This is old.
             

