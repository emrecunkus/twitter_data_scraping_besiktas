
"""
Otomotik test yazılımımızı kontrol etmek için gömülü python kütüphanesi olan
time kütüphanesini kullanıyoruz, otonom olarak tarayıcımızda yapacağımız
geçişler arasındaki süreyi bu kütüphane ile belirleyeceğiz.
"""


import time

"""
selenium kütüphanesinden webdriver'ı import ediyoruz,
webdriver bize seçili tarayıcı üzerinden otonom olarak 
yazıılımın çalışması noktasında yardım edecek.
"""

from selenium import webdriver

"""
sayfalara geçiş yaptığımızda find_element_by_.. fonksiyonunu kullanarak,
css, html ya da xpath gibi geçerli yollar alıp test yazılımında input degerleri
otonom olarak dolduracağız
"""

from selenium.webdriver.common.keys import Keys

"""
Proje dizinimizde chromedriver.exe dosyası var, bunu internet üzerinden 
indirip otonom yazılımımızın çalışması için, projeye dahil ettik, aynı şekilde
opera, mozilla gibi browserların driver.exe dosyaları eklenerek, farklı tarayıcılar 
üzerinden yazılımı çalıştırmak mümkün.

"""


browser = webdriver.Chrome()
time.sleep(0.2)

"""
Bu kod satırı açılan sayfanın 0.2 saniye içinde tam ekran 
yapılacağını bize gösteriyor.
"""

browser.maximize_window()

"""
yazılımımız bize twitter search kısmını açıp beşiktaş ile atılan son popüler 
twitleri bulacak.Yazılımı çalıştırdıktan sonra bunu ekranda 
görmek mümkün olacak.
"""

base_url = u'https://twitter.com/search?q='
query = u'besiktas'
url = base_url + query


browser.get(url)
time.sleep(1)

"""
yukarda verilen iki linki birleştirip gereken search işlemini
twitter üzerinden public olarak(authentication gerekmeden) 
yapacak.
"""

print("Tarayıcınızdan tweetler çekiliyor.... bu yazılım 1 dakika zaman alacaktır")
body = browser.find_element_by_tag_name('body')

"""
açılan sayfada by_tag_name kütüphanesini browser üzerinden çağırarak, 
ilgili twitleri tespit ediyoruz.
"""


"""
bu for döngüsü ilgili tweetleri bulup, üstünde oldugumuz sayfada 
0.1 saniyelik aralıklarla aşağıya inip diğer twitlerin datalarını da almamızı sağlayacak.
"""

tweets = browser.find_elements_by_css_selector("[data-testid=\"tweet\"]")
f = open("MyFile.txt", "a", encoding="utf-8")


mylist = tweets
mylist = []



"""
aşağıdaki for döngüsü açtığımız web sayfasında tweetleri almaya başlıyor,
bu işlemi yapma prensibi ise şöyle,
css selector yardımıyla tweeti saptayıp 
web element stackinin içinden son elementi alıyoruz ve bunu temp
yani geçici değişkenimize atıp listemize ekliyoruz, eğer stack  da
o an elemnt boşşsa continue komutumuzla yazılımın bir süre daha kontrolünü sağlıyoruz
keys.page down sayfada aşağılara inmememizi sağlayan bir komut,
for döngüsü sonlandığında tüm bilgileri listemize atmış olacağız.

"""


for _ in range(100):
    body.send_keys(Keys.PAGE_DOWN)

    tweets.extend(browser.find_elements_by_css_selector("[data-testid=\"tweet\"]"))
    temp=""
    if browser.find_elements_by_css_selector("[data-testid=\"tweet\"]"):



        temp = browser.find_elements_by_css_selector("[data-testid=\"tweet\"]").pop().text
    else:
        continue


    mylist.append(temp)

    body.send_keys(Keys.PAGE_DOWN)


    #print("whats that",temp )






    #browser.find_elements_by_css_selector("[data-testid=\"tweet\"]").remove()




    time.sleep(0.05)



"""
çok kullanışlı olan css_selector fonksiyonu artık tweetleri render 
edip işleyecebileceğimiz bir kıvama getiriyor, birazdan bunları kullanıyor
oalcağız. 
"""




f.write("Bu txt dosyası seleniumla çalışan bi otonom yazılımın,\n"
             "çektiği verileri gösterir.\n")

f.write("\n")
f.write("-"*50)



"""
aşağıdaki for döngüsü boyunca tweets içine attığımız bazı random twitleri
hem konsola hem de txt dosyasına yazılırken göreceğiz, bu durum internet hızına 
göre farklı zamanlarda gerçekleşebilir, ortalama 40-50 sn sürecektir.
"""



"""for tweet in tweets:
    print("deneme")
    if(tweet != ""):
        print(tweet.text)"""

mylist = list(dict.fromkeys(mylist))

"""
birden fazla çekilem tweet varsa listemizden duplicate
yani tekrar eden verileri temizliyoruz
"""

print("Tweetler çekilmeye başlandı ....")
time.sleep(3)
print("Tweetler yazdırılmaya başlandı, görev tamamlanmak üzere...")






"""
aşağıdaki for döngüsünde daha önce web elementi olarak aldıgımız ve html css
kodları arasında ayıkladığımız dataları, 
for each yapısı kullanarak yazdırıyoruz, yazdırırken karışıklık olmaması adına çizgilerle
ayırıyoruz.

"""








for value in mylist:

    f.write("--------------------------------------------------------\n")
    f.write("Tweet bilgileri aşağıdadır\n")
    f.write("--------------------------------------------------------\n")
    f.write("Kullanıcı twitter rumuzu, kullanıcı twitter adı, \n"
          "Tweet kaç saat önce atıldı bilgisi(örneğin 23s= 23 saat önce,) ,\n"
          "tweet içeriği(text),\n"
          "yorum sayısı, retweet sayısı, beğeni sayısı\n"
          )
    f.write("==========================================\n")
    f.write(value)


    f.write("\n")
    f.write("-"*50)
    f.write("\n")


print("tüm bilgiler MyFile.txt dosyasına yazdırıldı")












