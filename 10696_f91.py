
def f91(n):
    if n>100:
        return n-10
    
    return 91


while True:
    n = int(input())
    if n==0:
        break
    
    print('f91(%d) = %d' %(n,f91(n)))