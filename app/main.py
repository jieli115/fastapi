from fastapi import FastAPI

#创建fastapi实例
app =FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World xxx"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}