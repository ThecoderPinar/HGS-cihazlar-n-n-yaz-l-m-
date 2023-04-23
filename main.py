class AracSinifi1:
    def __init__(self, hgs_no, isim, soyisim, gecis_tarihi, bakiye):
        self.hgs_no = hgs_no
        self.isim = isim
        self.soyisim = soyisim
        self.gecis_tarihi = gecis_tarihi
        self.bakiye = bakiye
        self.sinif = "Otomobil"

class AracSinifi2:
    def __init__(self, hgs_no, isim, soyisim, gecis_tarihi, bakiye):
        self.hgs_no = hgs_no
        self.isim = isim
        self.soyisim = soyisim
        self.gecis_tarihi = gecis_tarihi
        self.bakiye = bakiye
        self.sinif = "Minibüs"

class AracSinifi3:
    def __init__(self, hgs_no, isim, soyisim, gecis_tarihi, bakiye):
        self.hgs_no = hgs_no
        self.isim = isim
        self.soyisim = soyisim
        self.gecis_tarihi = gecis_tarihi
        self.bakiye = bakiye
        self.sinif = "Otobüs"

class Gise:
    def __init__(self):
        self.arac_sayisi = 0
        self.gelen_araclar = []

    def odeme_kabul_et(self, arac):
        if arac.sinif == "Otomobil":
            arac.bakiye -= 5
        elif arac.sinif == "Minibüs":
            arac.bakiye -= 10
        elif arac.sinif == "Otobüs":
            arac.bakiye -= 15

        self.gelen_araclar.append(arac)
        self.arac_sayisi += 1


class OGSYonetimi:
    def __init__(self, gise):
        self.gise = gise

    def toplam_gunluk_bakiye(self):
        toplam_bakiye = 0
        for arac in self.gise.gelen_araclar:
            toplam_bakiye += arac.bakiye
        return toplam_bakiye

def odeme_kabul_et(self, arac):
    if arac.arac_sinifi == "Otomobil":
        arac.bakiye -= 5
    elif arac.arac_sinifi == "Minibus":
        arac.bakiye -= 10
    elif arac.arac_sinifi == "Otobus":
        arac.bakiye -= 20
    self.gecen_araclar.append(arac)
    
def toplam_gunluk_bakiye(self):
    bakiye_toplam = 0
    for arac in self.gise.gecen_araclar:
        bakiye_toplam += arac.bakiye
    print("Toplam Günlük Bakiye: ", bakiye_toplam)

# Örnek kullanım
arac1 = AracSinifi1("1234567890", "Ali", "Yılmaz", "2023-04-23 14:30", 10)
arac2 = AracSinifi2("0987654321", "Ayşe", "Kara", "2023-04-23 15:00", 20)
arac3 = AracSinifi3("1357908642", "Mehmet", "Demir", "2023-04-23 16:00", 30)

gise = Gise()
gise.odeme_kabul_et(arac1)
gise.odeme_kabul_et(arac2)
gise.odeme_kabul_et(arac3)

ogsyonetimi = OGSYonetimi(gise)
print("Toplam Günlük Bakiye:", ogsyonetimi.toplam_gunluk_bakiye())
