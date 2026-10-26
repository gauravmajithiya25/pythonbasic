def generator(number):
    li= []
    for i in  range(2,number + 1, 2):
         li.append(i)
    return li
print(generator(20))
