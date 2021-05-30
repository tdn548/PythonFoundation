#--Bai 31
def tinhtongtich(n):
    tong=0
    tich=1
    while n>0:
        so=n%10
        tong=tong+so
        tich=tich*so
        n=n//10
    return tong,tich

#bai32
def timsolonnhat(n):
    A=0
    while n>0:
        so=n%10
        if so>A:
            A=so
        n=n//10
    return A
#---ctrinh chinh
n=int(input('nhao so nguyen n:'))
tong,tich=tinhtongtich(n)

print("tong=%d,tich=%d"%(tong,tich))

print('với n= %d, Bài 32: '%n,timsolonnhat(n))
