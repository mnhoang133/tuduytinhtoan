print('I`m a student')

x = 1 / 7
print(f"{x:.5f}")

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))

tong = a + b

print("Tổng của hai số là:", tong)

# Bài tập 4: Nhập tên file, đọc và in nội dung nếu có, báo lỗi nếu không tồn tại
filename = input("Nhập tên file: ")
try:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print("Nội dung file:")
        print(content)
except FileNotFoundError:
    print("Lỗi: File không tồn tại.")
