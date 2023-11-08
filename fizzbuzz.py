num = int(input("Enter number :"))

def fizzbuss(num):
    if num%3==0:
        return "Fizz"
    elif num%5==0:
        return "Buzz"
    elif num%3==0 and num%5==0:
        return "FizzBuzz"
    #else:
    #    return num5


print(fizzbuss(5))

