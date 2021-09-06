
def main():
    #escribe tu código abajo de esta línea
    N = int(input("Enter triangle height: "))
    espacio = " "
    star = "*"
    conEspacio = N - 1
    conStar = N - conEspacio 
    
    for x in range(0,N):
        print(espacio * conEspacio + star*conStar)  
        conEspacio -= 1
        conStar += 1


if __name__=='__main__':
    main()
