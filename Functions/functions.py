def sayHello(name = 'user'):
    return 'Hello '+ name

msg = sayHello('furkan')
msg = sayHello('mustafa')

print(msg)

def total(num1, num2):
    return num1 + num2

result = total(10,20)
result = total(15,20)
print(result)

def yasHesapla(dogumYili):
    return 2019 - dogumYili

agefurkan = yasHesapla(2017)
agecagri = yasHesapla(2010)
agekemal = yasHesapla(1999)

print(agefurkan, agecagri, agekemal)

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldı
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz')


EmekliligeKacYilKaldi(1983, 'Furkan')
EmekliligeKacYilKaldi(1950, 'Cagri')
EmekliligeKacYilKaldi(1974, 'Kemal')

print(help(EmekliligeKacYilKaldi))

list = [1,2,3]

print(help(list.append))