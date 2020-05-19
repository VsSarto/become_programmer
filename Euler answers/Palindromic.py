<<<<<<< HEAD:Euler answers/Palindromic.py
#Largest palindrome
=======
#palindrome 
>>>>>>> 3e37dbce0fd7b189617a9011d75a238a33567091:projects/Project Euler/Palindromic.py
number = 0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        a = list(str(i*j))
        b=a[:]
        b.reverse()
        if(a==b and (i*j) > number):
            number = i*j

print(number)
