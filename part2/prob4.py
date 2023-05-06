print("Enter numbers : ")
numlist=[]

n=int(input())
while n!=int(q) or n!=int(Q):
    if n%2==0:
        numlist.append(n)
    n=int(input())
print(numlist)