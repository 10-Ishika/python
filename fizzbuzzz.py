n=int(input("Enter the any number:"))
for i in range(1,n):
    if i%3==0:
        print("fizza")
    # if i%3==0 and i%5==0:
    #     print("Fizzbuzz")
    elif i%5==0:
        print("Buzz")
    # elif i%3==0 :
    #     print("fizz")
    elif i%3==0 and i %5==0:
        print("fizzbuzz")
    else:
        print(i)