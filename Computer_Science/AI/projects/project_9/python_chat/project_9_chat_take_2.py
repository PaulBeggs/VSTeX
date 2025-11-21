from ollama import chat
import time
import random
import re # Imported for easy text parsing

# Simple starting list
starting_weapons = ["Rusty Iron Sword", "Old Wooden Club"]

class Chatbot:
    def __init__(self, role: str):
        self.message_history = [{'role': 'assistant', 'content': f"{role}"}]

    def talk(self, msg: str, inventory: dict) -> str:
        self.message_history.append({"role": "user", "content": msg, "inventory": inventory})
        start = time.time()
        response = chat(
            model="gemma3:1b",
            messages=self.message_history
        )
        duration = time.time() - start
        print(f"{duration:.2f}s to reply")
        assistant_reply = response.message.content
        self.message_history.append({"role": "assistant", "content": assistant_reply})
        return assistant_reply

def main():
    print("Welcome to ")

if __name__ == '__main__':
    main()