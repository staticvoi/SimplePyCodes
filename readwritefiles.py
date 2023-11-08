# modes of file
# r- read exception if no file found
# w- write create new file if not present and overwrite into it if present
# r+ - read and write
# w+ read and write create new file if not present and overwrite into it if present
# a- append with the original content



# f = open("C:\\Users\\10676874\\Documents\\Basic Python Code of CodeBasics\\readwritefiles.txt","w")
# f.write("I am learning")
# f.close()

# it overwrites this line to prevous line to avoid that use append
# f = open("C:\\Users\\10676874\\Documents\\Basic Python Code of CodeBasics\\readwritefiles.txt","w")
# f.write("I am cooking")
# f.close()

# f = open("C:\\Users\\10676874\\Documents\\Basic Python Code of CodeBasics\\readwritefiles.txt","a")
# f.write("\nI am cooking")
# f.close()

# read a file
# f = open("C:\\Users\\10676874\\Documents\\Basic Python Code of CodeBasics\\readwritefiles.txt","r")
# print(f.read())
# f.close()


# print every line 
# f = open("C:\\Users\\10676874\\Documents\\Basic Python Code of CodeBasics\\readwritefiles.txt","r")
# for line in f:
#     print(line)
# f.close()

# print every word
# f = open("C:\\Users\\10676874\\Documents\\Basic Python Code of CodeBasics\\readwritefiles.txt","r")
# for line in f:
#     word = line.split(' ') #split gives list/array of words
#     print(word)
#     # print(str(word))
#     print(len(word))
# f.close()


# store word count in a new file

f = open("C:\\Users\\10676874\\Documents\\Basic Python Code of CodeBasics\\readwritefiles.txt","r")
f_out = open("C:\\Users\\10676874\\Documents\\Basic Python Code of CodeBasics\\readwritefiles1.txt","w")
for line in f:
    word = line.split(' ') 
    f_out.write("word count "+str(len(word))+line)
f.close()
f_out.close()


# with statemnet doesnt req f.close() as it automatically cloese
with open("C:\\Users\\10676874\\Documents\\Basic Python Code of CodeBasics\\readwritefiles.txt","r") as f:
    print(f.read())

print(f.closed) #true
