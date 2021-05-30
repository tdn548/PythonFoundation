def kiem_tra_so_may_man(num):
    #may_man = True
    while num > 0:  # n = 5084, n nguyên dương mới làm
        new_num = num % 10  # số 4, lấy dư 8
        if new_num != 6 and new_num != 8:
            return False
        num //= 10 # num= num//10
    return True


n = int(input("Nhập số nguyên dương n: "))
if kiem_tra_so_may_man(n):
    print("Số may mắn")
else:
    print("Số ko may mắn")
