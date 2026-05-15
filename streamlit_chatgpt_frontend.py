import streamlit as st
from langraph_backend import chatbot
from langchain_core.messages import HumanMessage
import random
################################## function ####################################

def generate_thread_id():
    inte = random.randint(0,255)
    resp = f"Random_thread_id - {inte}"
    return resp

def reset_new_chat():
    new_thread = generate_thread_id()
    st.session_state['thread_id'] = new_thread
    st.session_state['chat_threads'].append(new_thread)
    st.session_state['message_list'] = []
    
def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    return chatbot.get_state(config={'configurable' : {'thread_id' : thread_id}}).values['messages']

################################## function ####################################
if 'message_list' not in st.session_state:
    st.session_state['message_list'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []

add_thread(st.session_state['thread_id'])


####################################### sidebar ###################################

st.sidebar.title("Streamlit ChatModel")
if st.sidebar.button("New Chat"):
    reset_new_chat()

st.sidebar.title("My Conversation History")

if st.session_state['thread_id']:
    for thread in st.session_state['chat_threads'][::-1]:
        if st.sidebar.button(thread):
            st.session_state['thread_id'] = thread
            messages = load_conversation(thread)
            temp_list = []
            for message in messages:
                if isinstance(message,HumanMessage):
                    temp_list.append({'role' : 'user', 'message' : message.content})
                else:
                    temp_list.append({'role' : 'ai', 'message' : message.content})
            st.session_state['message_list'] = temp_list

####################################### sidebar ###################################
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
                config={'configurable' : {'thread_id' :st.session_state['thread_id']}},
                stream_mode='messages'
                )
            )
    st.session_state['message_list'].append({'role' : 'ai', 'message' : ai_message})

print(st.session_state)

