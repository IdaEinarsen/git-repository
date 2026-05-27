# 8.11 Archived Messages

# Function 8.10
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

# Using a slice notation to store the original list 
show_messages(send_messages[:], sent_messages)
show_sent_messages(sent_messages)


print("\nOriginal list:")
print(send_messages)

print("\nSent messages:")
print(sent_messages)