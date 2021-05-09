import spacy

NLP = spacy.load("en_core_web_sm")

CHATBOT_STATES = {
    "begin": "chatbot open",
    "end": "saving states, chatbot closed"
}

CONDITIONAL_STATEMENTS = {
    ["if x then y"],
}
THRESHOLD_SIMILARITY = 0.75

def chatbot():
    value = input("what do you want to do? (begin/end): ")

    if value in CHATBOT_STATES.keys():
        if value == "begin":
            print(CHATBOT_STATES[value])
            print("lets begin")

            

        elif value == "end":
             print(CHATBOT_STATES[value])
        else:
            print("cannot parse entered value, terminating")

if __name__ == "__main__":
    chatbot()