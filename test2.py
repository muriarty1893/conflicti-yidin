def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if(y == 0):
        print("Bölen 0 olamaz 2. değişkeni değiştirin") #koşul eklendi
        y = input("Yeni değişken")
        y = int(y)
        return x / y
    else:
        return x / y

print("Yapmak istediğiniz işlemi seçin:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")

choice = input("Seçiminizi yapın (1/2/3/4): ")

num1 = float(input("Birinci sayıyı girin: "))
num2 = float(input("İkinci sayıyı girin: "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")

elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")

elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")

elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")

else:
    print("Geçersiz giriş")
