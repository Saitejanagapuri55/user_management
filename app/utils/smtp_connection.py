class SMTPClient:
    def __init__(self, server: str, port: int, username: str, password: str):
        self.server = server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str):
        print(f"Mock email sent to {recipient} with subject '{subject}'.")
