def soluong(n):
    tongsochan = 0
    tongsole=0
    while n > 0:
        so = n % 10
        if so % 2==0:
            tongsochan+=1
        else:
            tongsole+=1
        n=n//10
    return tongsole,tongsochan

n = int(input('Nhap so nguyen duong: '))
tongsochan,tongsole=soluong(n)
print('So luong so chan la %d, so luong so le la %d'%(tongsochan,tongsole))
