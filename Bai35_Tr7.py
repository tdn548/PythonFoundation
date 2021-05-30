def ToanChan(n):
    while n > 0:
        so = n % 10
        n=n//10
        if so % 2 != 0: # neu la so le thi ngung
            return False
    return True
def ToanLe(n):
    while n > 0:
        so = n % 10
        n=n//10
        if so % 2 == 0: # neu la so chan thi ngung
            return False
    return True
print("Bai 35: ")
n = int(input("Nhap so nguyen duong: "))
if ToanLe(n)==True:
    print(n,'chứa toàn số lẻ')
elif ToanChan(n)==True:
    print(f'{n} chứa toàn số chẵn')
else:
    print(f'{n} chứa cả số chẵn và số lẻ')
