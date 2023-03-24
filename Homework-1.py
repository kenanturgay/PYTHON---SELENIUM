"""

Temel olarak şu veri tipleri vardır:

Sayısal Veri Tipleri: Bu veri tipleri, sayısal verileri ifade etmek için kullanılır. İki temel sayısal veri tipi şunlardır:

Tam Sayılar (int): Negatif veya pozitif tamsayıları ifade eder. Örnek: 1, -5, 10
Ondalıklı Sayılar (float): Virgülden sonra sayılar içerebilen sayıları ifade eder. Örnek: 3.14, 2.0, -0.5
Metinsel Veri Tipi: Bu veri tipi, metinleri ve karakterleri ifade etmek için kullanılır.

Metin (string): Tek tırnak veya çift tırnak işaretleri içinde yazılan karakter dizileridir. Örnek: "Merhaba!", 'Python Programlama'
Mantıksal Veri Tipleri: Bu veri tipleri, doğru veya yanlış değerleri ifade etmek için kullanılır.

Boolean (bool): True (doğru) veya False (yanlış) değerlerini ifade eder.
Liste Veri Tipi: Bu veri tipi, bir dizi veri öğesini saklamak için kullanılır.

Liste (list): Köşeli parantez içinde virgülle ayrılan verilerin bir listesi şeklindedir. Örnek: [1, 2, 3], ["elma", "armut", "kiraz"]
Demet Veri Tipi: Bu veri tipi, bir dizi veri öğesini saklamak için kullanılır ancak değiştirilemezdir.

Demet (tuple): Parantez içinde virgülle ayrılan verilerin bir listesi şeklindedir. Örnek: (1, 2, 3), ("elma", "armut", "kiraz")
Sözlük Veri Tipi: Bu veri tipi, bir anahtar-değer çiftlerinin birleşimini saklamak için kullanılır.

Sözlük (dictionary): Süslü parantez içinde anahtar ve değer çiftleri şeklinde yazılır. Örnek: {'elma': 1, 'armut': 2, 'kiraz': 3}
Küme Veri Tipi: Bu veri tipi, bir dizi benzersiz veriyi saklamak için kullanılır.

Küme (set): Süslü parantez içinde virgülle ayrılan verilerin bir listesi şeklindedir. Örnek: {1, 2, 3}, {"elma", "armut", "kiraz"}


kodlama.io websitesinde kullanılan veri tipleri, websitesinin tasarımına, veritabanına, kullanıcı bilgilerine ve diğer özelliklere bağlı olarak farklılık göstermektedir. Ancak genel olarak web geliştirme alanında kullanılan bazı yaygın veri tipleri şunlardır:

Dize (String): Kullanıcı adı, şifre, e-posta, isim ve soyisim gibi metinsel veriler için kullanılır.

Tamsayı (Integer): Sayfa sayısı, sipariş numarası, öğe sayısı ve benzeri tam sayısal veriler için kullanılır.

Ondalıklı Sayı (Float): Ürün fiyatı, vergi oranı ve benzeri ondalıklı sayısal veriler için kullanılır.

Boolean (Bool): Kullanıcının oturum açtığı veya açmadığı gibi doğru/yanlış veya açık/kapalı gibi durumları belirtmek için kullanılır.

Liste (List): Öğelerin sıralı bir listesini tutmak için kullanılır. Örneğin, bir sitede gösterilecek olan ürünlerin listesi gibi.

Sözlük (Dictionary): Anahtar-değer çiftleri şeklinde verileri tutmak için kullanılır. Örneğin, bir kullanıcının isim, e-posta, şifre gibi bilgilerinin bir sözlükte saklanması gibi.

Demet (Tuple): Değiştirilemez veri yapılarıdır. Örneğin, bir kitabın yazarı, yayınevi, basım tarihi gibi bilgilerin bir demette saklanması gibi.

Küme (Set): Benzersiz veri öğelerini saklamak için kullanılır. Örneğin, bir yorumda kullanılan benzersiz kelimelerin bir kümede saklanması gibi.

"""


UserName = "kenan.turgay"
Password = "asd"

loginUserName = "kenan.turgay"
loginPassword = "asd"

if  UserName== loginUserName and Password == loginPassword:
        print("Giriş başarılı")
else:
        print("E-posta veya şifreniz yanlıştır.")


courses = {"Python", "PHP", "JAVA", "C#"}

researchCourse = input("Lütfen aradığınız kursu yazınız: ")

if researchCourse in courses:
    print("Aradığınız kurs bulunmaktadır.")
else:
    print("Aradığınız kurs bulunmamaktadır.")
