#set removes duplicates but doesnt preserve original order but dict.fromkeys() will preserve order

i = [2, 2, 3, 3, 3, 4, 1, 3, 5, 4, 6]
print(list(dict.fromkeys(i)))
#output will be [2, 3, 4, 1, 5, 6]
