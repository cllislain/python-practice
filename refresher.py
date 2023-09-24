# def primeNumber(number):
#     if (number == 0 or number == 1):
#         return False
#     for i in range(2, number):
#         if (number % i) == 0:
#             return False
#     else:
#         return True
        
# while True:
#     prime = int(input("Enter number: "))
#     for i in range(2, prime + 1):
#         if(primeNumber(i)):
#             print("Prime number: " + str(i))

while True:
    primeNumbers = []      
    prime = int(input("Enter number: "))
    if prime < 0:
        print("Negative integer")
        break
    for number in range(2, prime + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                 primeNumbers.append(number)
                  
    print("Prime numbers: " + str(primeNumbers)[1:-1])
    print("\n")

# prime = int(input("Enter number: "))
# for number in range(2, prime + 1):
#     if number > 1:
#         for i in range(2, number):
#             if (number % i) == 0:
#                 break
#         else:
#             print("Prime numbers: " + number)


# prime = int(input("Enter number: "))
# if prime < 0:
#     print("Negative Integer")
    
# for number in range(2, prime + 1):
#     if number > 1:
#         for i in range(2, number):
#             break;
# else:
#     print(number)
            
