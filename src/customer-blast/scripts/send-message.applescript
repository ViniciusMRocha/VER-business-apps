on run {phoneNumber, textMessage}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set receiver to buddy phoneNumber of targetService
        send textMessage to receiver
    end tell
end run


