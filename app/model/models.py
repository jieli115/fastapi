ALI_TONGYI_API_KEY_OS_VAR_NAME = "DASHSCOPE_API_KEY"
ALI_TONGYI_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
ALI_TONGYI_MAX_MODEL = "qwen-max-latest"
ALI_TONGYI_PLUS_MODEL = "qwen-plus"
ALI_TONGYI_TURBO_MODEL = "qwen-turbo"
ALI_TONGYI_DEEPSEEK_R1 = "deepseek-r1"
ALI_TONGYI_DEEPSEEK_V3 = "deepseek-v3"
ALI_TONGYI_EMBEDDING_MODEL = "text-embedding-v3"
import os

def get_ali_tongyi_api_key():
    return os.getenv(ALI_TONGYI_API_KEY_OS_VAR_NAME, "DASHSCOPE_API_KEY")
# print(os.getenv(ALI_TONGYI_API_KEY_OS_VAR_NAME))