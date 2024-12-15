#Problem-2: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]

def odd_number(number):
    for i in range(1,number+1):
        print(2*i-1)
        
if __name__ == "__main__":
    try:
        number = int(input("enter the number:"))
        odd_number(number)
    except Exception as e:
        print("enter a valid number")
