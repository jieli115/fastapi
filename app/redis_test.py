import redis

# 连接Docker容器里的Redis
r = redis.Redis(
    host="127.0.0.1",    # 本地IP，对应Docker端口映射
    port=6379,           # 映射的本地端口
    password="",  # 你的Redis密码
    decode_responses=True  # 自动转字符串，避免乱码
)

try:
    # 测试连接+读写
    r.ping()  # 测试连通性
    r.set("local_test", "Docker Redis验证成功", ex=3600)
    print("✅ Redis连接成功，测试值：", r.get("local_test"))
except Exception as e:
    print("❌ Redis连接失败：", e)