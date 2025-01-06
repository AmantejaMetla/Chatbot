def load_responses(file_path):
    responses = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if ':' in line:
                user_input, bot_response = line.strip().split(':', 1)
                responses[user_input.lower()] = bot_response.strip()
    return responses

def get_response(user_input, responses):
    # Match user input against the dataset
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I didn't understand that.")

