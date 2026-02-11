ALI_TONGYI_API_KEY_OS_VAR_NAME = "DASHSCOPE_API_KEY"
ALI_TONGYI_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
ALI_TONGYI_MAX_MODEL = "qwen3-max"
ALI_TONGYI_PLUS_MODEL = "qwen-plus-2025-09-11"
ALI_TONGYI_TURBO_MODEL = "qwen-turbo-0919"
ALI_TONGYI_DEEPSEEK_R1 = "deepseek-r1"
ALI_TONGYI_DEEPSEEK_V3 = "deepseek-v3"
ALI_TONGYI_EMBEDDING_MODEL = "text-embedding-v3"

DEEPSEEK_API_KEY_OS_VAR_NAME = "Deepseek_Key"
DEEPSEEK_URL = "https://api.deepseek.com/v1"
DEEPSEEK_CHAT_MODEL = "deepseek-chat"
DEEPSEEK_REASONER_MODEL = "deepseek-reasoner"
import os


def get_ali_tongyi_api_key():
    return os.getenv(ALI_TONGYI_API_KEY_OS_VAR_NAME, "DASHSCOPE_API_KEY")


print(os.getenv(ALI_TONGYI_API_KEY_OS_VAR_NAME))
