from os import system
system("cls")
class bankomat:
    __password="7777"
    __popitka=0
    __balans=3000000
    balance=0
    new_pas=0
    def __init__(self):
        self.lang=int(input("Tilni tanlang 1. O'zbek  2.Rus\t\t"))
        if self.lang==1:
            system("cls")
            parol=input("Parolni kiriting: ")
            bankomat.__popitka+=1
            while bankomat.__password!=parol and bankomat.__popitka!=3:
                print(f"Parol xato kiritildi! Qolgan urinishlar soni:={3-bankomat.__popitka}")
                bankomat.__popitka+=1
                parol=input("Parolni kiriting: ")
            if bankomat.__password==parol:
                system("cls")
                self.kirish()
            else:
                system("cls")
                print("\n\n\n\t\t\tSizning kartangiz bloklandi. Karta bankomatda qoladi")
        else:
            print("Dobro Pojalovat!")
    def kirish(self):
        print("""Quyidagilardan birini tanlang:\n\n
1.Sms - xabarnoma\t\t\t\t2.Naqt pul yechish\n
3.Balans         \t\t\t\t4.Karta hisobini to'ldirish\n
                \t5.Parolni o'zgartirish\n""")
        natija=input("Kiriting: ")
        match natija:
            case "1":
                self.sms()
            case "2":
                self.naqt()
            case "3":
                self.balans()
            case "4":
                self.update_balans()
            case "5":
                self.change_password()
    def qaytish(self):
        answer=input("Hurmatli mijoz bankomatdan yana foydalanisizmi(Ha,Yo'q)? ")
        if answer.upper()=="HA":
            self.kirish()
        else:
            system("cls")
            print("Salomat bo'ling")
    def sms(self):
        system("cls")
        function=input("""Sms xabarnoma xizmatini .. .
                        1. Yoqish  
                        2. O'chirish """)
        if function=="1":
            raqam=input("Telefon raqamini kiriting: ")
            if raqam.isdigit()  and len(raqam)==12 and raqam.startswith("998"):
                print("Sms-xabarnoma xizmati muvaffaqiyatli ulandi")
            else:
                print("Xato raqam kiritildi")
        else:
            print("Xizmat o'chirildi")
        self.qaytish()
    def naqt(self):
        system("cls")
        ls=[100000,250000,400000,500000]
        print("""Qancha miqdorda pul yechmoqchisiz:\n\n
1.100 000\t\t\t\t2.250 000\n
3.400 000\t\t\t\t4.500 000\n
                \t5.Boshqa summa\n""")
        natija=input("Kiriting: ")
        if natija=="5":
            ls.append(int(input("Kerakli summani kiriting: ")))
        if bankomat.__balans>=ls[int(natija)-1]:
            bankomat.__balans-=ls[int(natija)-1]
            print(f"Marhamat {ls[int(natija)-1]} so'm miqdoridagi pulingizni oling")
            self.balans()
        else:
            print("Sizning balansizda yetarli mablag' mavjud emas")
            self.balans()
        self.qaytish()
    def balans(self):
        system("cls")
        print(f"Kartada qolgan mablag': {bankomat.__balans}")
        self.qaytish()
    def update_balans(self):
        system("cls")
        self.balance=input("Kartangizga qancha pul kiritasiz? ")
        bankomat.__balans=int(bankomat.__balans)+int(self.balance)
        print("Kartangizga pul muvafaqiyatli tarzda o'tkazildi")
        self.qaytish()
    def change_password(self):
        system("cls")
        self.pas=input("Kartangzini kodini ozgartirasizmi (Ha,Yo'q): ")
        if self.pas.upper()=="HA":
            parol=input("Parolni kiriting: ")
            if bankomat.__password==parol:
                system("cls")
                print("togri")
                self.new_pas=input("New passwordni kiritng: ")
                bankomat.__password=self.new_pas
                print("Plastik kartangizni kodi muvafaqiyatli tarzda uzgradi")
                self.qaytish()
            else:
                system("cls")
                print("\n\n\n\t\t\tplastik kartangizni kodini xato kiritdingiz keyinroq qaytadan urinib kuring")
        if self.pas.upper()=="YOQ":
            print("Plastik kartangizni kodi uzgarmadi")
bkm=bankomat()
            