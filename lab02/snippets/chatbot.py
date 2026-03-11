import streamlit as st

st.title("Smart Bot ♿")

from transformers import pipeline

qwen = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct", max_new_tokens=100)

prompt = \
"""
<INSTRUCTION>
You are a helpful but sarcastic bot.
You provide short and concise answers.
You are not allowed to ask questions.
You do not hallucinate or provide false information.
</INSTRUCTION>

<QUESTION>
{question}
</QUESTION>

<ANSWER>
"""

def ask_bot(question):
    formatted_prompt = prompt.format(question=question)
    response = qwen(formatted_prompt, return_full_text=False)
    answer = response[0]["generated_text"].strip()

    return answer

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(
            message["content"]
        )  # st.markdown interprets and renders its input as markdown

# React to user input
if prompt := st.chat_input("Say something!"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = ask_bot(prompt)

    # Display bot's response in chat message container
    with st.chat_message("♿"):
        st.markdown(response)

    # Add bot's response to chat history
    st.session_state.messages.append({"role": "parrot", "content": response})




