#Basic:
# import streamlit as st
# st.title("🧠 Local AI Study Assistant")
# st.write("Welcome! Ask me anything and I will try to help you.")





#Intermediate:
# import streamlit as st
# import ollama

# # Set the title of the Streamlit application
# st.title("🤖 Local AI Chatbot")

# # Display a short description
# st.write("Ask a question and get an answer from the local Ollama AI model.")

# # Create a text box for the user
# prompt = st.text_input("Enter your question:")

# # Create a button
# if st.button("Ask AI"):

#     # Check whether the user entered a question
#     if prompt.strip() == "":
#         st.warning("Please enter a question.")

#     else:
#         try:
#             # Send the question to the Ollama model
#             response = ollama.chat(
#                 model="gemma3:4b",
#                 messages=[
#                     {
#                         "role": "user",
#                         "content": prompt
#                     }
#                 ]
#             )

#             # Get the AI response
#             answer = response["message"]["content"]

#             # Display the answer
#             st.subheader("AI Response")
#             st.write(answer)

#         except Exception as e:
#             # Display an error if Ollama cannot be reached
#             st.error("Unable to connect to Ollama.")
#             st.write("Error:", e)






#Improved:
import streamlit as st
import ollama

# Page configuration
st.set_page_config(
    page_title="Local AI Study Assistant",
    page_icon="🧠",
    layout="centered"
)

# Title
st.title("🧠 Local AI Study Assistant")

st.caption("Powered by Gemma 3 4B • Running locally with Ollama")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask your study question...")

if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ollama.chat(
                model="gemma3:4b",
                messages=st.session_state.messages
            )

            answer = response["message"]["content"]

            st.markdown(answer)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    st.write("**Model:** Gemma 3 4B")
    st.write("**Runtime:** Ollama")
    st.write("**Interface:** Streamlit")
    st.write("**Mode:** Local AI")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()