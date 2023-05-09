import esp

def handle_response(message) -> str:
    processed_message = message.lower()

    if processed_message == 'hello':
        return 'Hey there'
    
    if processed_message == 'next':
        return esp.get_next_schedules()
    
    if processed_message[:6] == 'search':
        return esp.search_areas(processed_message[7:])
    
    return 'Sorry, I cannot understand your message'