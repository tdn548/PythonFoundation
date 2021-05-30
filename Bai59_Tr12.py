S=input ('Nhập chuỗi: ')
print('Bài 59 A:')
print('upper:',S.upper())
print('lower:',S.lower())
print('title:',S.title())
print('capitalize:',S.capitalize())
print('swapcase:',S.swapcase())

print('Bài 59 B:')
ch=input ('Nhập ký tự: ')
print('Cách 1: Dùng 2 lệnh for và if:')
dem=0
for kytu in S:
    if kytu==ch:
        dem+=1
print('Có %d ký tự %s trong chuỗi %s' %(dem, ch, S))

print('Các 2: Dùng count')
print('Có %d ký tự %s trong chuỗi %s' %(S.count(ch), ch, S))

print ('Cau C:')
kytu = kyso = 0
for i in S:
    if i.isalpha():
        kytu+=1
    elif i.isdigit():
        kyso+=1
print('Có %d ký tự và %d ký số trong chuỗi \'%s\'' %(kytu,kyso,S))

print ('Cau D:')
kytuHoa=kytuThuong=kyso=khac=0
for i in S:
    if i.isupper():
        kytuHoa += 1
    elif i.islower():
        kytuThuong += 1
    elif i.isdigit():
        kyso += 1
khac=len(S)-(kytuHoa + kytuThuong + kyso)
print('Trong chuỗi \'%s\' có:' %(S))
print('     + Ký tự in hoa    = %d' %kytuHoa)
print('     + Ký tự in thường = %d' %kytuThuong)
print('     + Ký số           = %d' %kyso)
print('     + Ký tự khác      = %d' %khac)


print('Cau E:')
vowels = "AEIOU"
consonant= 'BCDEFGHJKLMNPQRSTVWXYZ'
nguyenam=phuam=0
ketqua=''
for i in S:
    if i.upper() in vowels:
        nguyenam += 1
        ketqua += i + ' '
print('Có %d nguyên âm: %s' %(nguyenam, ketqua))

ketqua=''
for i in S:
    if i.upper() in consonant:
        phuam += 1
        ketqua += i + ' '
print('Có %d phu âm: %s' %(nguyenam, ketqua))

