import streamlit as st
import random
import time
import llm_logic


# Streamed response emulator
def response_generator(prompt):
    response = llm_logic.generate_response(prompt)
    for word in response.split(): #animation of typing 
        yield word + " "
        time.sleep(0.05)

st.set_page_config(
    page_title="Professor AI - Your Educational Assistant",
    page_icon="👨‍🏫"
)

st.title("Professor AI")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})