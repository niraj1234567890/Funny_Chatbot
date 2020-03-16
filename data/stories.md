## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
* mood_affirm
  - utter_goodbye

## sad path_1
* greet
  - utter_greet
* mood_unhappy
  - utter_ask_joke
* mood_affirm
  - utter_which_kind_joke
* inform{"jokes":"teacher"}
  - action_retrive_joke
  - utter_did_that_help
* mood_affirm
  - utter_happy
* goodbye
  - utter_goodbye
  
## sad path _2
* greet
  - utter_greet
* mood_unhappy
  - utter_ask_joke
* mood_deny
  - utter_ask_again
* mood_deny
  -utter_goodbye
  
## sad path_3
* greet
  - utter_greet
* mood_unhappy
  - utter_ask_joke
* mood_deny  
  - utter_ask_again
* mood_affirm
  - utter_which_kind_joke
* inform{"jokes":"teacher"}
  - action_retrive_joke
  - utter_did_that_help
* mood_affirm
  - utter_happy
* goodbye
  - utter_goodbye
  
## sad path_4
* greet
  - utter_greet
* mood_unhappy
  - utter_ask_joke
* mood_affirm
  - utter_which_kind_joke
* inform{"jokes":"husband_wife"}
  - action_retrive_joke
  - utter_did_that_help
* mood_affirm
  - utter_happy
* goodbye
  - utter_goodbye
  
## sad path_5
* greet
  - utter_greet
* mood_unhappy
  - utter_ask_joke
* mood_deny  
  - utter_ask_again
* mood_affirm
  - utter_which_kind_joke
* inform{"jokes":"husband_wife"}
  - action_retrive_joke
  - utter_did_that_help
* mood_affirm
  - utter_happy
* goodbye
  - utter_goodbye

## sad path_6
* greet
  - utter_greet
* mood_unhappy
  - utter_ask_joke
* mood_affirm
  - utter_which_kind_joke
* inform{"jokes":"father"}
  - action_retrive_joke
  - utter_did_that_help
* mood_affirm
  - utter_happy
* goodbye
  - utter_goodbye
  
## sad path_7
* greet
  - utter_greet
* mood_unhappy
  - utter_ask_joke
* mood_deny  
  - utter_ask_again
* mood_affirm
  - utter_which_kind_joke
* inform{"jokes":"father"}
  - action_retrive_joke
  - utter_did_that_help
* mood_affirm
  - utter_happy
* goodbye
  - utter_goodbye  
  
## strange user
* greet
  - utter_greet
* mood_sleepy
  - utter_good_night
* goodbye
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
