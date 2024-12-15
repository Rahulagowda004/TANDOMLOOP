#Problem-3: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]

def pyramid(number):
    if number % 2 == 0:
        for i in range(1,number):
            print(2*i-1,end=" ")
    else:
        for i in range(1,number+1):
            print(2*i-1,end=" ")
            
if __name__ == "__main__":
    try:
        number = int(input("enter the number:"))
        pyramid(number)
    except Exception as e:
        print("enter a valid number")
