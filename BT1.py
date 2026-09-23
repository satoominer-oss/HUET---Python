tup = [['1', '1', 7, 1, 3],['2', '2', 5, 4, 6],['3', '3', 5, 8, 9], ['4', '4', 8, 5, 9], ['5', '5', 8, 6, 7]]
#Nhap so hoc sinh
n = len(tup)

#Nhap danh sach hs    
print("Danh Sách: ",tup)

#Loc danh sach diem khong hop le
i=0
test = True
while i != (len(tup)):
    list = tup[i]
    test = True
    while test==True:
        j = 1
        while j < (len(list)-1):
            j +=1
            x = list[j]
            if not(0 <= int(x) <= 10):
                tup.pop(i)
                test = False
                list = []
                j += 10
                break
            elif (j==(len(list)-1)):
                i += 1
                test = False
                break

#diem trung binh
list = []
i = 0
test = True
for i in range(len(tup)):
    dtb=0
    list = tup[i]
    j = 2
    for j in range(2, len(list)):
        dtb += list[j]
    dtb = dtb/3
    list.append(round(dtb,3)) #lam tron bien toi 3 gia tri thap phan
    tup[i] = list

#Xep Loai
for i in range(len(tup)):
    list = tup[i]
    if list[-1] >=9:
        list.append("Xuất Sắc")
        tup[i] = list
    elif list[-1] >= 8:
        list.append("Giỏi")
        tup[i] = list
    elif list[-1] >=6.5:
        list.append("Khá")
        tup[i] = list 
    elif list[-1] >= 5:
        list.append("Trung Bình")
        tup[i] = list
    else:
        list.append("Yếu")
        tup[i] = list

#in ra ket qua
print(f"Danh Sách Đầy Đủ: {tup}")

ratings = [row[-1] for row in tup]
xs = ratings.count("Xuất Sắc")
g = ratings.count("Giỏi")
k = ratings.count("Khá")
tb = ratings.count("Trung Bình")
y = ratings.count("Yếu")
print("------------------------------------------")
print(f"Có Tổng Cộng {xs} Học Sinh Xuất Sắc")
print(f"Có Tổng Cộng {g} Học Sinh Giỏi")
print(f"Có Tổng Cộng {k} Học Sinh Khá")
print(f"Có Tổng Cộng {tb} Học Sinh Trung Bình")
print(f"Có Tổng Cộng {y} Học Sinh Yếu")
print("------------------------------------------")

print("Học Sinh Yếu Gồm: ")
for i in range(len(tup)):
    list = tup[i]
    if list[-1] == "Yếu":
        print(f"Sinh Viên : '{list[0]}' Với Điểm {list[2:5]}")
        print(f"Số Điểm cần bù là: {10 - list[-2]}")
print("---------------------------------------")
max = 0
posmax = 0 #vi tri cua nguoi co diem tb cao nhat
for i in range(len(tup)):
    list = tup[i]
    if max < list[-2]:
        max = list[-2]
        posmax = i
        maxname = list[0]
print(f"Sinh Viên có điểm cao nhất: '{maxname}'")
print(f"Với điểm: {max}")
print(f"Thông Tin Sinh Viên : {tup[posmax]}")
