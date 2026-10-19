import streamlit as st

st.title("Simple Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages=[]
    
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        
prompt=st.chat_input("Type your message.....")

if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.write(prompt)
        
    if "python" in prompt.lower():
        reply="python is a popular language for AI and data science."
    elif "streamlit" in prompt.lower():
        reply="Streamlit is a python framework for interactive web apps."
    else:
        reply=f"You said: '{prompt}'. I'm a demo chatbox!"
        
    st.session_state.messages.append({"role":"assistant","content":reply})
    with st.chat_message("assistant"):
        st.write(reply)
        
if st.button("Clear Chat"):
    st.session_state.messages=[]
    st.rerun()
    
# import json
# if st.session_state.messages:
#     chat_text="\n".join(
#         f"{m['role']}: {m['content']}"
#         for m in st.session_state.messages
#     )
#     st.download_button("Dowload chat",chat_text,"chat_history.txt","text/plain")
    
# if prompt:
#     with st.spinner("Assistant is typing...."):
#         import time
#         time.sleep(1)
#         reply="Your reply here....."
        
# import openai

# if prompt:
#     response=openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role":"user","content":prompt}]
#     )
#     reply=response.choices[0].message.content

