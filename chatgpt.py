import streamlit as st
import openai

# Set your OpenAI GPT-3 API key here
openai.api_key = st.secrets['apikey']

# Streamlit app
def main():
    st.title("ChatGPT with Streamlit")

    # Sidebar to enter user input
    user_input = st.text_input("You:", "")

    if st.button("Ask"):
        # Generate a response using OpenAI GPT-3
        response = generate_response(user_input)
        
        # Display the response
        st.text("ChatGPT: {}".format(response))

def generate_response(user_input):
    # Use OpenAI GPT-3 to generate a response
    prompt = f"User: {user_input}\nChatGPT:"
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use the most powerful engine
        prompt=prompt,
        max_tokens=150,  # Adjust as needed
        n=1,
        stop=None,
        temperature=0.7,  # Adjust for creativity vs. accuracy
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    main()
