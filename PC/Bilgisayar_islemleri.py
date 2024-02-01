import time

class bilgisayar:
    def __init__(self, pc_durumu = "kapalı",marka = "[casper]",yas = "[3]",ram = "[16]",islemci = "[i5]",içindeki_programlar = ["above"]):
        self.pc_durumu = pc_durumu
        self.marka = marka
        self.yas = yas
        self.ram = ram
        self.islemci = islemci
        self.içindeki_programlar = içindeki_programlar

    def pc_ac(self):
        if(self.pc_durumu == "açık"):
            print("bilgisayar zaten acıktır...")
        else:
            print("bilgisayar açılıyor....")
            self.pc_durumu == "açık"
    def pc_kapat(self):
        if(self.pc_durumu == "kapalı"):
            print("bilgisayar zaten kapalıdır...")
        else:
            print("bilgisayar acılıyor...")
            self.pc_durumu == "açık"
    def program_ekle(self,program_ismi):
        print("Program ekleniyor...")
        time.sleep(1)
        self.içindeki_programlar.append(program_ismi)
        print("Program eklendi...")
    def program_silme(self,silinicek_program_ismi):
        print("Program siliniyor...")
        time.sleep(1)
        self.içindeki_programlar.remove(silinicek_program_ismi)

    def __len__(self):
        return len(self.içindeki_programlar)

    def __str__(self):
        return "Pc durumu = {}\nMarkası = {}\nYaşı = {}\nRamı = {}\nİşlemcisi = {}\nİçindeki Programlar = {}\n".format(self.pc_durumu,self.marka,self.yas,self.ram,self.islemci,self.içindeki_programlar)

bilgisayar = bilgisayar()

print("""******************************************
    BİLGİSAYAR İSLEMLERİ
    1-)PC AC
    2-)PC KAPAT
    3-)PROGRAM EKLE
    4-)PROGRAMI SİL
    5-)PROGRAMLARIN İSİMLERİ
    6-)BİLGİSAYAR ÖZELLİKLERİ
    Çıkıs için '7'ya basınız.
    ****************************************""")
while True:

        işlem = input("Lütfen işlem seciniz = ")
        if(işlem == "1"):
            bilgisayar.pc_ac()
        elif(işlem == "2"):
            bilgisayar.pc_kapat()
        elif(işlem == "3"):
            program_ismi = input("Ekleyecek olacagınız programı ',' ile ayırarak giriniz = ")
            içindeki_programlar = program_ismi.split(",")
            for eklenecekler in içindeki_programlar:
                bilgisayar.program_ekle(eklenecekler)
        elif(işlem == "4"):
            silinicek_program_ismi = input ("Silicek olacagınız programı ',' ile ayırarak giriniz = ")
            içindeki_programlar = silinicek_program_ismi.split(",")
            for silinicekler in içindeki_programlar:
                bilgisayar.program_silme(silinicekler)
        elif(işlem == "5"):
            print("Programlar = ",len(bilgisayar))
        elif(işlem == "6"):
            print(bilgisayar)
        elif(işlem == "7"):
            print("Programdan cıkılıyor...")
            break
        else:
            print("Gecersiz islem yaptınız...")



