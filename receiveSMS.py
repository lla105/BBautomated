import subprocess
import time

def get_all_messages():
    script = """
    tell application "Messages"
        set messageList to {}
        repeat with i from 1 to count of text chats
            set chat to item i of text chats
            set messageText to ""
            repeat with j from 1 to count of messages of chat
                set aMessage to item j of messages of chat
                set messageText to messageText & content of aMessage & "\\n"
            end repeat
            set messageList to messageList & messageText
        end repeat
        return messageList
    end tell
    """
    result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    return result.stdout.strip()

# Example usage
if __name__ == "__main__":
    all_messages = get_all_messages()
    print("Messages:\n", all_messages)
