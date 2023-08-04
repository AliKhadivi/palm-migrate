# from langchain.chat_models import ChatOpenAI
from config import PALM_API_KEY
import os
# import openai
from utils import parse_code_string
import pprint
import google.generativeai as palm

palm.configure(api_key = os.getenv("PALM_API_KEY"))

class AI:
    def __init__(self, model="models/text-bison-001", temperature=0.1, max_tokens=10000):
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.model_name = model
        # try:
        #     _ = ChatOpenAI(model_name=model) # check to see if model is available to user
        # except Exception as e:
        #     print(e)
            # self.model_name = "gpt-3.5-turbo"
    
    def write_code(self, prompt):
        # message=[{"role": "user", "content": str(prompt)}] 
        # response = openai.ChatCompletion.create(
        #     messages=message,
        #     stream=False,
        #     model=self.model_name,
        #     max_tokens=self.max_tokens,
        #     temperature=self.temperature
        # )
        print(self.model_name)
        print(self.temperature)
        print(self.max_tokens)
        response = palm.generate_text(
            model=self.model_name,
            prompt=prompt,
            temperature=self.temperature,
            # The maximum length of the response
            max_output_tokens=self.max_tokens,
        )
        if response.result.startswith("INSTRUCTIONS:"):
            return ("INSTRUCTIONS:","",response.result[14:])
        else:
            code_triples = parse_code_string(response.result)
            return code_triples

    def run(self, prompt):
        response = palm.generate_text(
            model=self.model_name,
            prompt=prompt,
            temperature=self.temperature,
            # The maximum length of the response
            max_output_tokens=self.max_tokens,
        )
         
        return response.result
        # message=[{"role": "user", "content": str(prompt)}] 
        # response = openai.ChatCompletion.create(
        #     messages=message,
        #     stream=True,
        #     model=self.model_name,
        #     max_tokens=self.max_tokens,
        #     temperature=self.temperature
        # )
        # chat = ""
        # for chunk in response:
        #     delta = chunk["choices"][0]["delta"]
        #     msg = delta.get("content", "")
        #     chat += msg
        # return chat
    