def emoji_converter(message):
    words = message.split(" ")

    emoji_dict = {
        ":)": "🙂",
        ":(": "🙁",
        ";)": "😉",
        ":P": "😛",
        ":D": "😃"
    }

    output = ""

    for word in words:
        output += emoji_dict.get(word, word) + " "

    return output


message = input("> ")
print(emoji_converter(message))
