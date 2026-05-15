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

    
    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk,metadata in chatbot.stream(
                {'messages' : [HumanMessage(content=user_query)]},
                config=CONFIG,
                stream_mode='messages'
                )
            )
    st.session_state['message_list'].append({'role' : 'ai', 'message' : ai_message})
        

