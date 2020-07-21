"""单词翻转"""
sentence = input("请输入英文句子：")
list01 = sentence.split(" ")
list01[::-1]
#for item in range(len(list01)-1,-1,-1):
#     list02.append(list01[item])
sentence_reverse = " ".join(list01[::-1])
print(sentence_reverse)
