def emoji_convertor(msg):
    emoji = {
    ":)":"\U0001F600",
    ":(":"\U0001F62A",
    ":*":"\U0001F618",
    "mask":"\U0001F637",
    "hug":"\U0001F917"
    }
    output=''
    words= msg.split(' ')
    print(words)
    for ch in words:
        output+= emoji.get(ch, ch)+" "
    return output

msg = input("Enter message: ")
# result = emoji_convertor(msg)
# print(result)
print(emoji_convertor(msg))

# emoji = {
#     ":)":"\U0001F600",
#     ":(":"\U0001F62A",
#     ":*":"\U0001F618",
#     "mask":"\U0001F637",
#     "hug":"\U0001F917"
# }
# output=''
# msg = input(">: ")
# words= msg.split(' ')
# print(words)
# for ch in words:
#      output+= emoji.get(ch, ch)+" "
# print(output)

