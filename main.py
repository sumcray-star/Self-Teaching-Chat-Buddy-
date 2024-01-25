
# https://youtu.be/CkkjXTER2KE?si=nfWZyLjCAFb6F2r4 Link mei dekh leh 

import json
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:  # Load the previous data in dict form 
    with open(file_path, 'r')as file:        #Create a file for read only
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict): #Save the knowledge we give 
    with open(file_path, 'w') as file:   # same file 
        json.dump(data, file, indent=2)  #put data back into json

def find_best_match(user_question: str, questions: list[str]) -> str | None:  #Find best match from question give str or none
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6 ) # Accuaracy 
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None :  # Give Answer Output 
    for q in knowledge_base["questions: "]:
        if q["question"] ==question:
            return q["answer"]
    return None
    


def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        user_input: str = input("You: ")
        if user_input.lower() =='quit':
            break
        
        # search for best match
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions: "]])

        #print the answer 
        if best_match:
            answer: str= get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print("Bot: I don't know the answer. Can you teach me? ")
            new_answer: str = input("Type the answer or 'skip'to skip: ")

            if new_answer.lower() != 'skip':
                knowledge_base["questions: "].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print("Bot: Thank you! I learn something new :) ")

# Run THe Code 
if __name__ == '__main__':
    chat_bot()
