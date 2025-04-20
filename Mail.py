class MailMessage:
    def __init__(self, sender, recipient, content):
        self.sender = sender
        self.recipient = recipient
        self.content = content

    def __str__(self):
        return f"From: {self.sender}\nTo: {self.recipient}\n\n{self.content}"


class MailServer:
    def __init__(self, name):
        self.name = name
        self.inbox = []

    def receive_mail(self, message):
        self.inbox.append(message)

    def send_mail(self):
        if self.inbox:
            return self.inbox.pop(0)
        return None


class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user

    def receive_mail(self):
        message = self.server.send_mail()
        if message and message.recipient == self.user:
            return message
        return None

    def send_mail(self, recipient_server, recipient_user, message_content):
        if recipient_server not in MailSystem.servers:
            print(f"Cannot send mail to {recipient_server}: Server does not exist.")
            return

        message = MailMessage(self.user, recipient_user, message_content)
        MailSystem.servers[recipient_server].receive_mail(message)
        print(f"Mail sent to {recipient_user} on {recipient_server}.")


class MailSystem:
    servers = {}

    @classmethod
    def add_server(cls, server):
        cls.servers[server.name] = server


if __name__ == "__main__":

    server1 = MailServer("Server1")
    server2 = MailServer("Server2")

    MailSystem.add_server(server1)
    MailSystem.add_server(server2)

    client1 = MailClient(server1, "user1@example.com")
    client2 = MailClient(server2, "user2@example.com")

    client1.send_mail("Server2", "user2@example.com", "Hello, User 2!")
    for _ in range(2):
        received_message = client2.receive_mail()
        if received_message:
            print("Received message:")
            print(received_message)
        else:
            print("No new messages.")


