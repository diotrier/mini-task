angka = list(range(100, 0, -1))


# Function bilangan prima
def bil_Prima(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for num in angka:
    hasil = ""
    # Jangan print angka bilangan prima
    if bil_Prima(num):
        continue
    # ganti angka yang dapat dibagi dengan 3 dengan text Foo
    if num % 3 == 0:
        hasil += "Foo"
    # ganti angka yang dapat dibagi dengan 5 dengan text Bar
    if num % 5 == 0:
        hasil += "Bar"
    # print hasil
    if not hasil:
        hasil = num
    print(hasil, end=" ")
