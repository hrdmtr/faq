import random
import time

from dotenv import load_dotenv
from chatbot_engine import chat
from langchain.memory import ChatMessageHistory

import gradio as gr
import os



with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    def respond(message, chat_history):
        history = ChatMessageHistory()
        
        for [user_message, ai_message] in chat_history:
            history.add_user_message(user_message)
            history.add_ai_message(ai_message)
            
        
        print(len(history.messages))
        if len(history.messages) ==0:
            message = message + "日本語でお願いします"
        
        bot_message = random.choice(["hhhhhhhhhhhhh?", "超元気ですか", "質問あります？"])
        bot_message = chat(message=message, history=history)
        
        print(chat_history)
        
        chat_history.append((message, bot_message))
        time.sleep(1)
        return "", chat_history
    
    

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    load_dotenv()
    
    app_env = os.getenv("APP_ENV","production")
    
    if app_env == "production":
        username = os.getenv("GRADIO_USERNAME")
        password = os.getenv("GRADIO_PASSWORD")
        auth = (username, password)
    else:
        auth = None
    
    demo.launch(auth=auth)
