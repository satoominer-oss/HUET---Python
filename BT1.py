tup = [['A1', 'TTHA', 7, 1, 3],['A2', 'HNY', 5, 4, 6],['C3', 'VLDK', 5, 8, 9], ['A4', 'CVHL', 8, 5, 9], ['B5', 'VLTK', 8, 6, 7]]
n = len(tup)
   
print("Danh Sách: ",tup)

tup[:] = [
    row for row in tup
    if all(0 <= int(x) <= 10 for x in row[2:-1])
]

list = []
i = 0
for i in range(len(tup)):
    dtb=0
    list = tup[i]
    j = 2
    for j in range(2, len(list)):
        dtb += list[j]
    dtb = dtb/3
    list.append(round(dtb,1))
    tup[i] = list

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
        print(f"Sinh Viên : '{list[1]}' Với Điểm {list[2:5]} và điểm trung bình là {list[-2]}")
        print(f"Số Điểm cần bù là: {10 - list[-2]}")
print("---------------------------------------")
max = 0
posmax = 0
for i in range(len(tup)):
    list = tup[i]
    if max < list[-2]:
        max = list[-2]
        posmax = i
        maxname = list[1]
print(f"Sinh Viên có điểm cao nhất: '{maxname}'")
print(f"Với điểm: {max}")
print(f"Thông Tin Sinh Viên : {tup[posmax]}")
