class pieces():
    beyazPuan = 0
    siyahPuan = 0

    # Nesnenin ozelliklerinin belirlenmesi
    def __init__(self, renk, tip, puan, tehdit):
        self.renk = renk
        self.tip = tip
        self.puan = puan
        self.tehdit = tehdit

    # Row ve col degerlerinden lokasyon niteliginin olusturulmasi.
    def pos(self, row, col):
        self.lokasyon = (row, col)

    # Sinif niteliklerinin, ornek nitelikler kullanilarak hesaplanmasi.
    # Bu degerler, butun islemler yapildiktan sonra hesaplanacak ve
    # output olarak cikartilacak.
    def hesapla(self):
        if self.renk == 'beyaz':
            pieces.beyazPuan += self.puan
        if self.renk == 'siyah':
            pieces.siyahPuan += self.puan

    # Bir tasin baska taslar tarafindan tehdit edilmesi durumunda
    # puan oz niteliginin yariya dusurulmesi.
    def tehdit_varmi(self):
        if self.tehdit >= 1:
            self.puan /= 2

    # Tehdit olusumlarinin kontrolu icin taslarin olasi hamle/saldiri yapabilecekleri,
    # hucrelerin belirlenmesi. Daha sonra lokasyonlarda tas olup olmadigi kontrol edilip,
    # tehdit puanlari arttirilacak.
    def olasi_saldiri(self):
        # beyaz ve siyah piyon`un ayrilmasinin sebebi,
        # renk niteligine gore, hareket yonu belirleniyor.
        if self.tip == 'piyon' and self.renk == 'beyaz':
            self.hamle = list()
            self.hamle.append((self.lokasyon[0] - 1, self.lokasyon[1] - 1))
            self.hamle.append((self.lokasyon[0] - 1, self.lokasyon[1] + 1))

        elif self.tip == 'piyon' and self.renk == 'siyah':
            self.hamle = list()
            self.hamle.append((self.lokasyon[0] + 1, self.lokasyon[1] - 1))
            self.hamle.append((self.lokasyon[0] + 1, self.lokasyon[1] + 1))


        # At tasi`nin olasi hamleleri, 1 hucreye 2 hucre L seklinde ilerledigi
        # goze alinarak, iki degerin hipotenusu hesaplanarak olusturulmustur.
        # daha sonra oyun tahtasinin disina cikip cikmadigi kontrol edilip
        # hamle listesi niteligine bu lokasyonlar eklenmistir.
        elif self.tip == 'at':
            self.hamle = list()
            for a in range(-2, 3):
                for b in range(-2, 3):
                    if a ** 2 + b ** 2 == 5:
                        if self.lokasyon[0] + a >= 0 and self.lokasyon[0] + a <= 7 and self.lokasyon[1] + b >= 0 and self.lokasyon[1] + b <= 7:
                            self.hamle.append((self.lokasyon[0] + a, self.lokasyon[1] + b))


        # Vezirin olasi hamleleri hesaplanirken sekiz yonde, surekli devam edebiliyorken,
        # baska bir tasla karsilastiginda durmasi gerektigi icin, vezirin saldiri hamleleri,
        # nesneler olusturulduktan sonra hesaplanacaktir.
        elif self.tip == 'vezir':
            self.hamle = list()

        # Kale ve filin tehdit durumlarinin denetlenmesi istenmedigi icin,
        # olasi hamlelerin hesabi goz ardi edilmistir. Vezir`in hamleleri kale ve filin
        # birlesimi oldugu icin ayrica eklenmemistir.
        elif self.tip == 'kale':
            self.hamle = list()

        elif self.tip == 'fil':
            self.hamle = list()

        elif self.tip == 'sah':
            self.hamle = list()


##############################################################################################

while True:
    secim = input("""
    *******************************************************
        Hesaplanmasini istediginiz txt dosyasinin adini 
            'board' olarak, ayni dizine kopyalayin 
    *******************************************************
            Programi kapatmak icin q`ya basiniz
            Devam etmek icin enter`e basiniz...
    *******************************************************
        
        """)

    if secim == 'q':
        print("Programdan cikiliyor...")
        break

    else:
        # Modul`un bulundugu klasordeki txt dosyasinin okunmasi. Txt dosyasindan alinan
        # input`un her satiri once ayriliyor. Ayrilan her satiri da bir tasi temsil edecek
        # sekilde tekrar ayrilip, arr diye adlandirilan listenin icine ekleniyor.
        arr=list()
        with open('board.txt', 'r') as f:
            for line in f:
                a = line.split()
                for i in range(8):
                    arr.append(a[i])


        # 64 hucre icin bilgi bulunduran txt dosyasindan, hangilerinin tas oldugunun belirlenmesi.
        # Olusturulan taslar listesi, tas objelerini olusturmak icin kullanilacak.
        taslar = list()
        for i in range(1, 33):
            tasx = "tas{}".format(i)
            taslar.append(tasx)


        # Listedeki string degerine gore tas nesnelerinin olusturulmasi.
        # Her nesnenin nitelikleri sirayla renk, tip, puan ve tehdit sayisi olarak belirlenmistir.
        # Tehdit sayisi, o nesnenin kac tas tarafindan tehdit edildigini gostermektedir.
        # Dongu icinde i degerinin 8e bolumunden, lokasyon bilgisi elde ediliyor ve
        # Nesnenin lokasyon niteligine ataniyor.
        j = 0
        for i in range(64):
            if arr[i]!= "--":
                if arr[i] == "ks":
                    taslar[j] = pieces("siyah", "kale", 5, 0)
                    taslar[j].pos(i // 8, i % 8)
                    j += 1
                elif arr[i] == "as":
                    taslar[j] = pieces("siyah", "at", 3, 0)
                    taslar[j].pos(i // 8, i % 8)
                    j += 1
                elif arr[i] == "fs":
                    taslar[j] = pieces("siyah", "fil", 3, 0)
                    taslar[j].pos(i // 8, i % 8)
                    j += 1
                elif arr[i] == "vs":
                    taslar[j] = pieces("siyah", "vezir", 9, 0)
                    taslar[j].pos(i // 8, i % 8)
                    j += 1
                elif arr[i] == "ss":
                    taslar[j] = pieces("siyah", "sah", 100, 0)
                    taslar[j].pos(i // 8, i % 8)
                    j += 1
                elif arr[i] == "ps":
                    taslar[j] = pieces("siyah", "piyon", 1, 0)
                    taslar[j].pos(i // 8, i % 8)
                    j += 1
                elif arr[i] == "kb":
                    taslar[j] = pieces("beyaz", "kale", 5, 0)
                    taslar[j].pos(i // 8, i % 8)
                    j += 1
                elif arr[i] == "ab":
                    taslar[j] = pieces("beyaz", "at", 3, 0)
                    taslar[j].pos(i // 8, i % 8)
                    j += 1
                elif arr[i] == "fb":
                    taslar[j] = pieces("beyaz", "fil", 3, 0)
                    taslar[j].pos(i // 8, i % 8)
                    j += 1
                elif arr[i] == "vb":
                    taslar[j] = pieces("beyaz", "vezir", 9, 0)
                    taslar[j].pos(i // 8, i % 8)
                    j += 1
                elif arr[i] == "sb":
                    taslar[j] = pieces("beyaz", "sah", 100, 0)
                    taslar[j].pos(i // 8, i % 8)
                    j += 1
                elif arr[i] == "pb":
                    taslar[j] = pieces("beyaz", "piyon", 1, 0)
                    taslar[j].pos(i // 8, i % 8)
                    j += 1


        # Tehdit durumlarinin kontrolu icin taslarin olasi saldiri lokasyonlari belirlenmesi icin
        #olasi_saldiri metodu, her tas icin cagiriliyor.
        for k in range(j):
            taslar[k].olasi_saldiri()


        # Vezirin hamleleri, diger nesnelere bagli oldugu icin asagidaki gibi hesaplanmistir.
        # J degerimiz artik tas sayisini ifade etmektedir. Ilk dongude her tas tek tek kontrol ediliyor,
        # eger tas nesnesinin tip oz niteligi vezirse devam ediliyor. 2.dongude belirlenen yonde(kuzey) olasi
        # maksimum hareket sayisi, tahtanin disina cikmamasi kontrol edilip hesaplaniyior. Son dongude ise hamle
        # listesine eklenen son lokasyonda herhangi bir tas olup olmadigi kontrol ediliyor. Eger varsa,
        # test tam sayi degeri 1 yapiliyor ve artik hamle listesine baska bir lokasyon eklenmesine
        # izin verilmiyor. Renk kontrolu, tehdit olusturmasi kontrol edilirken hesaba katilacagi icin
        # burda goz ardi edilmistir. Bu kontol 8 farkli yon icin ayri ayri hesaplanmistir.
        for k in range(j):
            test = 0
            if taslar[k].tip == "vezir":
                for a in range(1, 8):
                    if taslar[k].lokasyon[0] - a >= 0 and test == 0:
                        taslar[k].hamle.append((taslar[k].lokasyon[0] - a, taslar[k].lokasyon[1]))
                        for b in range(j):
                            if taslar[k].hamle[a-1] == taslar[b].lokasyon:
                                test = 1

        for k in range(j):
            boy = len(taslar[k].hamle)
            test = 0
            if taslar[k].tip == "vezir":
                for a in range(1, 8):
                    if taslar[k].lokasyon[1] + a <= 7 and test == 0:
                        taslar[k].hamle.append((taslar[k].lokasyon[0], taslar[k].lokasyon[1]+a))
                        for b in range(j):
                            if taslar[k].hamle[a + boy - 1] == taslar[b].lokasyon:
                                test = 1

        for k in range(j):
            boy = len(taslar[k].hamle)
            test = 0
            if taslar[k].tip == "vezir":
                for a in range(1, 8):
                    if taslar[k].lokasyon[0] + a <= 7 and test == 0:
                        taslar[k].hamle.append((taslar[k].lokasyon[0]+a, taslar[k].lokasyon[1]))
                        for b in range(j):
                            if taslar[k].hamle[a + boy - 1] == taslar[b].lokasyon:
                                test = 1

        for k in range(j):
            boy = len(taslar[k].hamle)
            test = 0
            if taslar[k].tip == "vezir":
                for a in range(1, 8):
                    if taslar[k].lokasyon[1] - a >=0 and test == 0:
                        taslar[k].hamle.append((taslar[k].lokasyon[0], taslar[k].lokasyon[1] - a))
                        for b in range(j):
                            if taslar[k].hamle[a + boy - 1] == taslar[b].lokasyon:
                                test = 1

        for k in range(j):
            boy = len(taslar[k].hamle)
            test = 0
            if taslar[k].tip == "vezir":
                for a in range(1, 8):
                    if taslar[k].lokasyon[0] - a >= 0 and taslar[k].lokasyon[1] +a<=7 and test == 0:
                        taslar[k].hamle.append((taslar[k].lokasyon[0] - a, taslar[k].lokasyon[1] + a))
                        for b in range(j):
                            if taslar[k].hamle[a + boy - 1] == taslar[b].lokasyon:
                                test = 1

        for k in range(j):
            boy = len(taslar[k].hamle)
            test = 0
            if taslar[k].tip == "vezir":
                for a in range(1, 8):
                    if taslar[k].lokasyon[0] + a <= 7 and taslar[k].lokasyon[1] + a <= 7 and test == 0:
                        taslar[k].hamle.append((taslar[k].lokasyon[0] + a, taslar[k].lokasyon[1] + a))
                        for b in range(j):
                            if taslar[k].hamle[a + boy - 1] == taslar[b].lokasyon:
                                test = 1

        for k in range(j):
            boy = len(taslar[k].hamle)
            test = 0
            if taslar[k].tip == "vezir":
                for a in range(1, 8):
                    if taslar[k].lokasyon[0] + a <= 7 and taslar[k].lokasyon[1] - a >= 0 and test == 0:
                        taslar[k].hamle.append((taslar[k].lokasyon[0] + a, taslar[k].lokasyon[1] - a))
                        for b in range(j):
                            if taslar[k].hamle[a + boy - 1] == taslar[b].lokasyon:
                                test = 1

        for k in range(j):
            boy = len(taslar[k].hamle)
            test = 0
            if taslar[k].tip == "vezir":
                for a in range(1, 8):
                    if taslar[k].lokasyon[0] - a >= 0 and taslar[k].lokasyon[1] - a >= 0 and test == 0:
                        taslar[k].hamle.append((taslar[k].lokasyon[0] - a, taslar[k].lokasyon[1] - a))
                        for b in range(j):
                            if taslar[k].hamle[a + boy - 1] == taslar[b].lokasyon:
                                test = 1



        # Butun taslarin lokasyonlarina gore hamleleri daha once hesaplanmisti. Bu kisimda bu hamlelerin,
        # tehdit olusturup olusturmadigi denetlenmistir.Sirayla, her bir tas icin olusturulan hamle listesi
        # oz nitelikleri, tekrar butun taslarla kontrol edilip esit olmasi durumunda, kontrol edilen tasin,
        # tehdit oz niteligi 1 arttiriliyor.
        for k in range(j):
            for a in range(len(taslar[k].hamle)):
                for b in range(j):
                    if taslar[k].hamle[a] == taslar[b].lokasyon and taslar[k].renk != taslar[b].renk:
                        taslar[b].tehdit +=1

        # Farkli taslar tarafindan tehdit altinda olan taslarin puani her seferinde 2ye bolunmesin diye
        # tehdit sayisinin sadece 1`den buyuk olmasi "tehdir_varmi" metodu tarafindan kontrol edilip,
        # puani hesaplaniyor. Daha sonrahesapla metoduyla butun taslarin puani toplanip,
        # sinif niteliklerine ataniyor.
        for k in range(j):
            pieces.tehdit_varmi(taslar[k])
            pieces.hesapla(taslar[k])


        # Beyaz ve siyah taslarin puanlari, sinif niteliklerinden cagirilip bastiriliyor.
        print("""
               
               Beyazlarin toplam puani: {}
               Siyahlarin toplam puani" {}
               
        """.format(pieces.beyazPuan, pieces.siyahPuan))

        pieces.beyazPuan = 0
        pieces.siyahPuan = 0

