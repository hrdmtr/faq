import random
import time
from dotenv import load_dotenv
from chatbot_engine import chat
import gradio as gr
import os

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type='messages')
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def respond(message, chat_history):
        # chat_historyが空であれば、日本語での応答を促すメッセージを追加
        if not chat_history:
            message = message + " 日本語でお願いします"
        
        # bot_messageに応答を生成
        bot_message = chat(message=message, history=chat_history)
        
        # デバッグ出力: 応答が生成される前後のchat_historyを確認
        print("Debug: chat_history before append =", chat_history)
        
        # ユーザーとボットのメッセージを辞書形式で履歴に追加
        chat_history.append({"role": "user", "content": message})
        chat_history.append({"role": "assistant", "content": bot_message})
        
        print("Debug: chat_history after append =", chat_history)
        
        # 空のメッセージボックスと更新された履歴を返す
        return "", chat_history

    # メッセージの送信時にrespond関数を呼び出す
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    load_dotenv()
    
    app_env = os.getenv("APP_ENV", "production")
    
    if app_env == "production":
        username = os.getenv("GRADIO_USERNAME", "mh")
        password = os.getenv("GRADIO_PASSWORD", "mh")
        auth = (username, password)
    else:
        auth = None
    
    demo.launch(auth=auth)
