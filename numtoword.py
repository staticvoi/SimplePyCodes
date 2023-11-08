num = {
    "1":"one",
    "2":"two",
    "3":"three"
}
output=''
phone = input("phone: ")
for ch in phone:
     output+= num.get(ch, "none")+" "
print(output)