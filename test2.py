def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

#daha da gelişmiş bir branch
def divide(x, y):
    if(y == 0):
        print("bölen sayıyı 0 yapamazsınız (┬┬﹏┬┬) ") #koşul eklendi burası benim alanım
        print("2 kere düşün") # alan 2
        y = input("Yeni değişken")
        y = int(y)
    return x / y    
    
print("Yapmak istediğiniz işlemi seçin:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")
print("orrayt") #ekledim

choice = input("Seçiminizi yapın (1/2/3/4): ")

num1 = float(input("Birinci sayıyı girin: "))
num2 = float(input("İkinci sayıyı girin: "))

print("sayıları girdiniz") #ekledim

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")

elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")

elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")

elif choice == '4': # yorum satiri cacıki
    print(f"{num1} / {num2} = {divide(num1, num2)}")

else:
    print("yanlis") #değiştirdim
