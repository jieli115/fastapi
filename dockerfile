FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN apt update && apt install -y gcc g++ && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple  \
    && apt remove -y gcc g++
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]