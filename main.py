from zhipuai import ZhipuAI
# 申请APIKey
client = ZhipuAI(api_key="28548c62802530a1cda5dc968baf242f.PI4dDlt6sSQ6eYhk")
prompt = ""
# 循环语句 不断调用api做问答
while True:
    prompt = input("user:")
    # 创建一个client，用于对话
    response = client.chat.completions.create(
        model="glm-4",  # 调用的模型名称
        messages=[
            {"role": "user", "content": "你好"},
            {"role": "assistant", "content": "我是人工智能助手"},
            {"role": "user", "content": "你叫什么名字"},
            {"role": "assistant", "content": "我叫chatGLM"},
            {"role": "user", "content": prompt} # prompt是使用者对话内容
        ],
    )
    answer = response.choices[0].message
    print(dict(answer)["content"])