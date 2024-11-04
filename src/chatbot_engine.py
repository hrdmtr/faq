from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os

def chat(message: str, history=None) -> str:
    # historyがNoneなら空リストで初期化
    if history is None:
        history = []
    
    # OpenAIモデルのインスタンスを作成
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # ユーザーメッセージを履歴に追加
    history.append({"role": "user", "content": message})
    
    # OpenAIモデルにメッセージを送信して応答を取得
    response = llm.invoke([HumanMessage(content=message)])
    print("Debug: response =", response)
    print("Debug: response.content =", response.content)

    # ボットの応答を履歴に追加
    history.append({"role": "assistant", "content": response.content})
    
    # 応答内容を返す
    return response.content
