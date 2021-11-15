def mysplit(strng):
    if strng.strip() == "":
        return []
    return strng.strip().split(' ')

# Strip fjerner whitespaces, både foran og bagved det givet input
     

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
