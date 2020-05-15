#Largest palindrome productnumber = 0
number = 0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        a = list(str(i*j))
        b=a[:]
        b.reverse()
        if(a==b and (i*j) > number):
            number = i*j

print(number)
