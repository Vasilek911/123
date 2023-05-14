def summ(a):
    return ((a*3)//10+(a*3)%10)==((a*4)//10+(a*4)%10)==((a*2)//10+(a*2)%10)

b=int(input())
c=int(input())
for i in range(b,c+1):
    if summ(i):
        print(i)
