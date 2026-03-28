# from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv

from agent import get_agent

load_dotenv()


gpt_llm_model = ChatGroq(
    model="openai/gpt-oss-20b",
)

# gpt_llm_model = ChatOpenAI(
#     model = "openai/gpt-5-mini"
# )

agent = get_agent(gpt_llm_model)

s = input("")

result = agent.invoke({
    "messages":[
        {
            "role":"user",
            "content": s
        }
    ]
})

#print(result)
print(result["messages"][-1].content)