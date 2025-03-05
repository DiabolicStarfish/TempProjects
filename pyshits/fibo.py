def fibo(n):

    #if invalid input
    if n < 0:
        print("Value input is invalid.")

    elif n==0:
        return 0
    
    elif n == 1 or n == 2:
        return 1
    
    else:
        return (fibo(n-1) + fibo(n-2))
    
if __name__=='__main__':
     flg = True
     while(flg):
        try:
            number = int(input("Enter a positive integer number: "))
            print(fibo(number))
            flg = False
        except:
            print("Input not a valid number.")
