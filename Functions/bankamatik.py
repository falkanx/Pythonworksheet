# Bankamatik Uygulaması

hesap1 = {
    'ad': 'Furkan Alkan',
    'hesapNo': '12354344',
    'bakiye': 3000,
    'ekHesap': 2000
}

hesap2 = {
    'ad': 'Mustafa Alkan',
    'hesapNo': '53423456',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar 
        print('paranızı alabilirsiniz.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            print(f"Cekmek istediginiz {miktar}TL bakiyenizden({hesap['bakiye']}TL) fazla.")
            ekHesapKullanimi = input('ek hesap kullanılsın mı (e/h)')

            if ekHesapKullanimi == 'e':
                ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapKullanilacakMiktar
                print('paranızı alabilirsiniz.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print(f"Cekmek istediginiz {miktar}TL genel bakiyenizden({hesap['bakiye']+hesap['ekHesap']}TL) fazla.")
            print('üzgünüz bakiye yetersiz')
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(hesap1, 2999)


