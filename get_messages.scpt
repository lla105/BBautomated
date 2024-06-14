tell application "Messages"
    set messageList to {}
    repeat with i from 1 to count of chats
        set chat to item i of chats
        set messageText to ""
        set lastDate to (current date) - 10 * seconds -- last 10 seconds
        repeat with j from 1 to count of messages of chat
            set aMessage to item j of messages of chat
            if date sent of aMessage > lastDate then
                set messageText to messageText & content of aMessage & "\n"
            end if
        end repeat
        if messageText is not "" then
            set messageList to messageList & messageText
        end if
    end repeat
    return messageList
end tell
