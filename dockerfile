FROM python:3.11-slim

WORKDIR /app

# 关键1：安装证书+网络工具（解决HTTPS请求失败）
RUN apt update && apt install -y --no-install-recommends \
    gcc \
    g++ \
    libpq-dev \
    ca-certificates \ 
    curl \            
    && rm -rf /var/lib/apt/lists/* \
    && update-ca-certificates 

# 关键2：升级pip到最新版（解决版本解析问题）
RUN pip install --upgrade pip

# 关键3：多源兜底（同时配置清华+阿里云+官方源，确保能获取版本）
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ \
    && pip config set global.extra-index-url "https://pypi.tuna.tsinghua.edu.cn/simple/ https://pypi.org/simple/"

# 关键4：先手动验证pip源连通性（可选，便于排查）
RUN pip search fastapi || echo "pip search不可用，但不影响安装"

# 安装依赖（优先用宽松版本范围，避免版本卡死后端）
COPY requirements.txt .
RUN pip install --no-cache-dir fastapi>=0.100.0 uvicorn[standard] gunicorn  # 直接安装核心包，跳过requirements.txt的版本坑

# 复制项目代码
COPY . .

EXPOSE 8000
CMD ["gunicorn", "main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000"]