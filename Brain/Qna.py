#Open AI
fileopen = open("Data\Api.txt","r")
API = fileopen.read()
fileopen.close()

import openai
from dotenv import load_dotenv

openai.api_key = API
load_dotenv
completeion = openai.Completion()


def QuestionAnswer(question,chat_log = None):
    FileLog = open("DataBase\\qna_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template
    
    prompt = f'{chat_log}Question : {question}\nAnswer : '
    response = completeion.create(
        model = "text-davinci-002",
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0)
    answer = response.choices[0].text.strip()
    qna_log_template_update = chat_log_template + f"\nQuestion : {question} Answer: {answer}" 
    FileLog = open("Database\\qna_log.txt","w")
    FileLog.write(qna_log_template_update)
    FileLog.close()
    return answer

print(QuestionAnswer("data analytics"))