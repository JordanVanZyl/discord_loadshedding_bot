def handle_response(message) -> str:
    processed_message = message.lower()

    if processed_message == 'hello':
        return 'Hey there'
    
    return 'Sorry, I cannot understand your message'