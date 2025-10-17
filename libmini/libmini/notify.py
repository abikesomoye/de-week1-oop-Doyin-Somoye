# Simple Factory Pattern in the style of a notifier system

# Define the Notifier Interface
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, to: str, message: str) -> str:
        pass

# Concrete Notifiers
class EmailNotifier(Notifier):
    def send(self, to: str, message: str) -> str:
        return f"Email sent to {to}: {message}"

class SMSNotifier(Notifier):
    def send(self, to: str, message: str) -> str:
        return f"SMS sent to {to}: {message}"

# Notifier Factory
class NotifierFactory:
    @staticmethod
    def create(kind: str) -> Notifier:
        if kind == "email":
            return EmailNotifier()
        elif kind == "sms":
            return SMSNotifier()
        else:
            raise ValueError("Unsupported notifier type")
