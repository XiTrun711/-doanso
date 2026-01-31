import random
global rd
def display_menu():
    print("Chọn mức độ khó của trò chơi:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    lv = int(input("Nhập mức độ khó:"))
    if lv == 1:
        return 5
        rd = random.randint(1,50)
    elif lv == 2:
        return 5
        rd = random.randint(1,80)
    elif lv == 3:
        return 7
        rd = random.randint(1,200)
    else:
        display_menu()

def number():
    a = int(input("Nhập vào số dự đoán:"))
    if a == rd:
        return True
    elif a < 1 and a > 100:
        print("Số bạn nhập không nằm trong phạm vi dự đoán")
        number()
    elif a > rd:
        print("Số bạn nhập lớn hơn số cần đoán")
        return False
    elif a < rd:
        print("Số bạn nhập nhỏ hơn số cần đoán")
        return False
    

while True:
    
    rd = random.randint(1,100)
    print(rd)
    turns = display_menu()
    checkwin = False
    for i in range(turns):
        check = number()
        if check == True:
            checkwin = True
            print("Bạn đã chiến thắng")
            break
    if checkwin == False:
        print("Bạn đã thua")
    guess = input("Có muốn chơi lại nữa hay không:")
    if guess == "N":
        break
   
