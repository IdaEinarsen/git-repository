# 8.10 Sending Messages



send_messages = ["are you there?", "im looking for george", "Kevin, do you like fries?"]
sent_messages = []

def show_messages(send_messages, sent_messages):
    while send_messages:
        current_message = send_messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    print("\nThe following messages have been sent:")
    for message in sent_messages:
        print(message)


show_messages(send_messages, sent_messages)
show_sent_messages(sent_messages)