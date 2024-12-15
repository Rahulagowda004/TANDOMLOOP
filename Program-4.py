#Problem-4: Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]

def multiples(number :list):
    result = dict()
    for i in number:
        count = 0
        for j in number:
            if j%i == 0:
                count += 1
        result.update({i:count})
    return result

if __name__ == "__main__":
    no = [1,2,3,4,5,6,7,8,9]
    try:
        print(multiples(no))
    except Exception as e:
        print("provide list of numbers")
        
