from fastapi import FastAPI
import sys

import os
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
if current_dir not in sys.path:
    sys.path.append(current_dir)
import model.models as md
#创建fastapi实例
app =FastAPI()

api_key=md.get_ali_tongyi_api_key()
# api_key='xxx'
# api_key=os.getenv( "DASHSCOPE_API_KEY")

@app.get("/")
async def root():
    return {"message": f"Hello World wta,{api_key}"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}