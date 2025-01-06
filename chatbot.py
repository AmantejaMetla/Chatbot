import openai
import os
from pattern_matching import load_responses, get_response

# Load dataset responses
responses = load_responses("dialogs.txt")

# OpenAI API Key setup
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set this in your environment

def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        if "quota" in str(e).lower():
            return "I'm currently unable to answer due to quota limits. Please try again later."
        return f"Error: {e}"


def chatbot_response(user_input):
    # Try getting a response from the dataset first
    response = get_response(user_input, responses)

    # If no match, fallback to OpenAI API
    if response == "I'm sorry, I didn't understand that.":
        try:
            response = ask_openai(user_input)
        except Exception as e:
            response = "I'm sorry, I can't process your request at the moment."

    return response

