import streamlit as st
from langraph_backend import chatbot
from langchain_core.messages import HumanMessage

if 'message_list' not in st.session_state:
    st.session_state['message_list'] = []

CONFIG = {'configurable' : {'thread_id' : "thread-1"}}

for message in st.session_state['message_list']:
    if message['role'] == 'user':
        with st.chat_message('user'):
            st.text(message['message'])
    else:
        with st.chat_message('assistant'):
            st.text(message['message'])


user_query = st.chat_input('type here')

if user_query:
    st.session_state['message_list'].append({'role' : 'user', 'message' : user_query})
    with st.chat_message('user'):
        st.text(user_query)

    response = chatbot.invoke({'messages' : [HumanMessage(content=user_query)]},config=CONFIG)
    print(response)
    ai_message = response["messages"][-1].content
    st.session_state['message_list'].append({'role' : 'ai', 'message' : ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)

print(st.session_state)
