def TinhTongTich(n):
    tong = 0
    tich = 1
    while n>0: # n=5084
        so=n%10 # so=4, 8
        tong=tong+so # tong=4, 12
        tich=tich*so #tich=4, 32
        n=n//10 # n=508, 50
    return tong, tich
#-------------------
print('Bài 31')
n=int( input('Nhập số nguyên dương: '))
Tong, Tich = TinhTongTich(n)
print("Tổng = %d, Tích=%d" %(Tong, Tich) )
