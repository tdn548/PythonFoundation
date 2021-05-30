import math

#print("bài 18 ")

#print("bài 19 \n")
# a, b, c = input("nhap 3 so bat ki: ").split()
# a = eval(a)
# b = eval(b)
# c = eval(c)
#
# delta = b**2 - 4*a*c
# if delta < 0:
#     print("phuong trinh vo nghiem")
# elif delta ==0:
#     x1 = x2 = -b/2*2
#     print("nghiệm kép: {}".format(x1))
# else:
#     x1 = (-b + math.sqrt(delta)) / (2*a)
#     x2 = (-b - math.sqrt(delta)) / (2*a)
#     print(" x1 = {} và x2 = {}".format(x1,x2))

print("Bài 20")
xA, yA = input("nhap toa do A: ").split()
xB, yB = input("nhap toa do B: ").split()
xC, yC = input("nhap toa do C: ").split()
xP, yP = input("nhap toa do P: ").split()

xA = eval(xA)
yA = eval(yA)
xB = eval(xB)
yB = eval(yB)
xC = eval(xC)
yC = eval(yC)
xP = eval(xP)
yP = eval(yP)

z1 = (xB-xA) * (yP-yA) - (yB-yA)*(xP-xA)
z2 = (xC-xB) * (yP-yB) - (yC-yB)*(xP-xB)
z3 = (xA-xC) * (yP-yC) - (yA-yC)*(xP-xC)

if z1 > 0 & z2 > 0 & z3 > 0:
    print("Diem P nam trong tam giac ABC")
else:
    print("Diem P nam ngoai")



