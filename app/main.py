from fastapi import FastAPI, HTTPException
import sys
import os
from fastapi.responses import HTMLResponse

# 添加当前目录到系统路径
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
if current_dir not in sys.path:
    sys.path.append(current_dir)
# 导入 Agent 类
from agent import Agent
# 初始化 Agent
agent = Agent()
app = FastAPI()
@app.get("/", response_class=HTMLResponse)
async def root():
    # 从外部文件读取 HTML 内容
    html_file_path = os.path.join(current_dir, "templates", "chat.html")
    try:
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        return HTMLResponse(html_content)
    except Exception as e:
        return HTMLResponse(f"读取 HTML 文件时出错：{str(e)}")


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/chat")
async def chat(input: str):
    try:
        # 调用 agent.chat_chain 函数生成故事
        result = agent.chat_chain(input)
        return {"result": result.content}
    except Exception as e:
        return {"error": str(e)}
