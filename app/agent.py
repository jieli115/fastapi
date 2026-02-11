import sys
import os

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
if current_dir not in sys.path:
    sys.path.append(current_dir)
from langchain_openai import ChatOpenAI
from langchain_core.runnables.history import RunnableWithMessageHistory

# from langchain.memory import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from model import models


class Agent:
    def __init__(self):
        self.api_key = models.get_ali_tongyi_api_key()

    def chat_chain(self, input: str):
        self.llm = ChatOpenAI(
            api_key=self.api_key,
            base_url=models.ALI_TONGYI_URL,
            model=models.ALI_TONGYI_MAX_MODEL,
            max_tokens=1000,
            temperature=0,
        )
        self.template = ChatPromptTemplate(
            [
                ("system", "你是一个财经助手，你要根据用户的问题，用中文回答财经相关问题。"),
                ("human", "{input}"),
            ]
        )
        self.chain = self.template | self.llm
        return self.chain.invoke({"input": input})


agent = Agent()
print(agent.chat_chain("讲一个关于deepseek公司的故事").content)
