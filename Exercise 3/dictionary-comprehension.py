#Exercise - Dictionary Comprehension 1

f = open('file1.txt', 'r')
a=[]
for x in f:
    a.append(int(x))
f2 = open('file2.txt', 'r')
b=[]
for x in f2:
    b.append(int(x))

result=[]
for x in a:
    for y in b :
        if x==y and x not in result:
            result.append(x)
# Write your code above 👆

print(result)


