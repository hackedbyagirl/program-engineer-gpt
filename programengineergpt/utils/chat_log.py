import datetime

def create_chat_log(chat_file):
    # Get current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Create a file to store the chat log
    with open(chat_file, "w") as file:
        file.write(f"Chat Log: {current_time}")

def append_user_chat_message(chat_file, message):
    # Get current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    with open(chat_file, 'a') as file:
        # Check if the role is 'user' before writing to the file
        file.write(f"USER <{current_time}>: {message}")
        #file.write(f"USER <{current_time}>: {message.get('content', '')}\n")