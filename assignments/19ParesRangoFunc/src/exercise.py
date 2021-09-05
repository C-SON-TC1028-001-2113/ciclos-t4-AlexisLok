
def main():
    n1 = int(input("Valor 1: "))
    n2 = int(input("Valor 2: "))

    if n1 < n2:
        if n1%2 != 0:
            n1 += 1
        else:
            pass
        for num in range(n1,n2+1,2):
                print (num)
    elif n1 > n2:
        if n2%2 != 0:
            n2 += 1
        else:
            pass
        for num in range(n2,n1+1,2):
            print (num)
    else:
        print("No hay pares")


        
    

if __name__=='__main__':
    main()
