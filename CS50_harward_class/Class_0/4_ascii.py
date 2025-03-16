# ASCII characters:
# 32 - 47: " !*+'-"
# 48 - 57: [0-9]
# 58 - 64: [?:@]
# 65 - 90: [A-Z]
# 91 - 96: [[\^`]]
# 97 - 122: [a-z]

ascii_list = []
for i in range(65,91):
    ascii_list.append(chr(i))
for i in range(97, 123):
    ascii_list.append(chr(i))

print(ascii_list)