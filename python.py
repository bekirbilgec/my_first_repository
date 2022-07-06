# exception handling

while True:
   

    try :
        number1 = int(input("birinci sayi giriniz:"))
        number2 = int(input("ikinci sayi giriniz:"))
        division = number1/number2
    
        
    except ZeroDivisionError:
        print("given wrong ") 

    else:
        print("given")

    finally :
        print("done") 
        break       