
class Message():
    
    def __init__(self, sender, recipient) -> None:
        self.sender = sender
        self.recipient = recipient
        self.message = []

    def get_sender(self):
        return self.sender

    def get_recipient(self):
        return self.recipient

    def __str__(self):
        str_message = f"From: {self.sender}\nTo: {self.recipient}\n"
        str_message += "\n".join(self.message)
        return str_message

    def appendMessage(self, text):
        self.message.append(text)


m1 = Message("Rudolf", "Santa")

m1.appendMessage("Hello, where is my food?")
print(m1)

print()

senders_name = input("Senders name: ")
recipients_name = input("Recipients name: ")
content = input("Content of the message: ")

m2 = Message(senders_name, recipients_name)
m2.appendMessage(content)

print()
print(m2)
