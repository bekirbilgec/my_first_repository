import random
uppers = [chr(random.randint(65,90)) for i in range(2)]
lowers = [chr(random.randint(97,122)) for i in range(2)]
numbers = [chr(random.randint(48,57)) for i in range(2)]
ozel_karakters = chr(random.randint(33,47)) + chr(random.randint(58,64)) 
password = "".join(uppers)+"".join(lowers)+"".join(numbers)+ozel_karakters
def rastgele(password):
    templist = list(password)
    random.shuffle(templist)
    return "".join(templist)
while True:
    
    new_passowrd =print(rastgele(password))

    sifre = input("Lütfen gördüğünüz passwordu girin:")
    if sifre == "q" or sifre == "Q":
        print("Sifre girmeden çıktınız!!!")
        break
    elif new_passowrd == sifre:
        print("Başarılı bir şekilde sistemem giriş yaptınız...")
        break
    elif new_passowrd != sifre:
        print("Girdiğiniz şifre resimdeki şifre ile aynı değil,tekrar deneyiniz ...!")       