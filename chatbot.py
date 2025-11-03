import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

load_dotenv()
model_name = os.getenv("MODEL", "gpt-3.5-turbo")
llm = init_chat_model(model_name, temperature=0)

# Placeholder eligibility check
def check_eligibility(details: str) -> str:
    return f"Eligibility check placeholder: would evaluate {details} and return eligibility status (mock)"

tools = [
    {"name": "EligibilityCheck", "func": check_eligibility, "description": "Check enrollment eligibility based on user details"}
]

agent = create_agent(llm, tools=tools, name="AgenticEnrollment")

if __name__ == '__main__':
    while True:
        q = input('You: ')
        if q.lower() in ['exit','quit']:
            break
        print('Bot:', agent.run(q))
