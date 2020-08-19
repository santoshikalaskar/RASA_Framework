## happy path 1 (/tmp/tmpkvym3uol/a75470b09c6447a0b168d78fd07b4128_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: bot_challenge: amazing -->
    - utter_happy   <!-- predicted: utter_iamabot -->


## happy path 2 (/tmp/tmpkvym3uol/a75470b09c6447a0b168d78fd07b4128_conversation_tests.md)
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: bot_challenge: amazing -->
    - utter_happy   <!-- predicted: utter_iamabot -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1 (/tmp/tmpkvym3uol/a75470b09c6447a0b168d78fd07b4128_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_goodbye -->
* affirm: yes   <!-- predicted: ask_again: yes -->
    - utter_happy   <!-- predicted: utter_again -->


## sad path 2 (/tmp/tmpkvym3uol/a75470b09c6447a0b168d78fd07b4128_conversation_tests.md)
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: utter_goodbye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_goodbye -->
* deny: not really   <!-- predicted: confusing_Ques_registration: not really -->
    - utter_goodbye   <!-- predicted: utter_confusing_Ques_registration -->


## sad path 3 (/tmp/tmpkvym3uol/a75470b09c6447a0b168d78fd07b4128_conversation_tests.md)
* greet: hi
    - utter_greet
* mood_unhappy: very terrible   <!-- predicted: confusing_Ques_syllabus: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_confusing_Ques_syllabus -->
    - utter_did_that_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_confusing_Ques_syllabus -->
* deny: no
    - utter_goodbye


