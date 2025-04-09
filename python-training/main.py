# print:
print("Hello Uyen", "Hi")
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep=" % ", end=' ') #\n: xuong hang
print(6)
print("\tHello\t")

# Bien:
x = 5.6
print(type(x)) # kieu cua value: 5 --> int

x = 3
y = 4.5
print("x + y =", x + y)
print("x / y =", x / y) # 0.6666666666
print("x // y =", x // y) # in ra phần trước dấu ',' (0.0)

# Kieu data: int, float, str, bool, obj => trong python mọi thứ đều là OBJECT
x = 5 # x: là 1 đối tượng

# > < >= <= == !=: --> bool: True/False

# And, Or
    # AND: 0-FALSE; 1-TRUE
    # print(0 AND 1) -> 0

    # OR:
    # print(0 OR 1) -> 1

# string
s = "Hello string"
print(s * 3)
print(s.upper())
print(s.lower())
print(s.title()) # in hoa chữ cái đầu mồi từ
print(s.capitalize()) # in hoa chữ cái đầu tiên

age = 34 # int -> string
# i am 34
print(f"I am {age}") # ep int sang str
print("I am", age)
print("I am" + str(age))
print("I am {}".format(age)) # {} = format

# input: Lấy data từ user; luôn trả về 1 string
user_name = input("Enter your user: ")
print("User name:", user_name)

usd = float(input("usd: "))
print(usd * 24000)

# python built in functions

# if-else-elif
age = 18
if age >= 18:
    print("Duoc uong bia")
else:
    print("Uong nuoc ngot")


num = -4
if num > 0:
    print("so duong")
elif num == 0:
    print("so khong")
else:
    print("so am ")

# cách Debug

# List
li = ['sol', 1, 'banana', 2.454]
print(li[0])

li.append(5) # them
print(li)

li.insert(1, "vitri1") # chen
print(li)

del li[1] # xoa
print(li)

# vòng lặp for - while
for i in range(10):
    print("hello " + str(i))

li = ['so1', 'so2', 'so3', 'so4', 'so5', 'so6']
for i in li:
    print(i)

age = 1;
while age < 18:
    age = int(input("How old are you?")) # bat nhap lai den khi dung dieu kien


# danh sách list ,hoặc array
array = [1,2,3,4,5,6,7,8,9,10]
array2 = array[2:5]

for i in range(0, 5):
    print(array[i], end=" ")

for i in array:
    print(i)

for i in array[3:5]:
    print(i, end=" ")


for i in array[3:]:
    print(i)


array3 = [1,2,3,4,5,6,7,8,9,10]
print("so chia het cho 2: ")

for i in array:
    if i % 2 == 0:
        print(i, end=" ")

print()
# dictionary
user = { #obj
    'name': 'Uyen',
    'age': 18,
    'gioiTinh': 'Nu',
}

print(user['name'])

if 'age' not in user.keys():
    print("Khong co")
else:
    print("co")

if 12 not in user.values():
    print("Khong co")
else:
    print("co")


# Hàm
def tenHam(thamso1, thamso2):
    print(thamso1)
    print(thamso2)
    return thamso1 + " " + thamso2 # khi muốn trả về giá trị

# tenHam(1,2)

fullName = tenHam("Phuong", "Uyen")
print(fullName)


# Hàm có nhiều tham số
def tiemBanh(tenTiemBanh, *danhSachBanh):
    print("Tiệm bánh " + tenTiemBanh)
    for banh in danhSachBanh:
        print("- " + banh)

tiemBanh("Ngon Bakery", "Bánh mì", "Bánh kem", "Bánh quy")

# import trong pyhon cách thêm một modul
#from...import... as

# Class: tập hợp nhiều obj giống nhau

class sinhvien:
    def __init__(sv, ma, ten):
        sv.msv = ma;
        sv.ten = ten
    def inthongtin(sv):
        print("Ma sinh vien: " + sv.msv)
        print("Ten sinh vien: " + sv.ten)
sinhviena = sinhvien("705105144", "Uyen")
sinhviena.inthongtin()


















