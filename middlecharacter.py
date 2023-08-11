def getmiddlecharacters(word):
    index= len(word) // 2
    if len(word) % 2 == 0:
        return word[index - 1 : index + 1]
    else:
        return word[index]
result=getmiddlecharacters("computer")
print(result)