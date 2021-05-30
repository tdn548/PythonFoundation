print('Bài 27')
n=int(input("Nhập n:")) #  n>m >0
m=int(input("Nhập m:"))
i=1
count=0

while i<n:
    if n%i==0 and i<m:
        if count==0:
            print('Các ước số của %d nhỏ hơn %d: ' % (n, m), end=' ')
        print("%5d" %i,end="")
        count++
    i++
if count==0:
    print("Không có ước số nào của %d nhỏ hơn %d" %(n,m))
