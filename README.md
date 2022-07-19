<h1 align="center">
👋 Herkese Selamlar 👋
</h1>


## `Ubuntu`'da  temel seviyede database işlemlerini gerçekleştirmeye çalıştım. Bunun için `MySQL`, `MySQL Workbench`  kullandım. Ayrıca `Python` programlama dili ile de yine temel seviyede bazı database işlemlerini gerçekleştirdim. Umarım sizlere de katkısı olur.

# -----------------------------------------------------------------------------
# 🚀 MYSQL KURULUMU

[linkten](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04) kaynak bilgiye ulaşabilirsiniz.

aşağıdaki kodlar ile kuruluma başlayalım

```sh
sudo apt update
```

```sh
sudo apt install mysql-server
```

kurulan mysql versiyonunu kontrol edebiliriz
```sh
mysql --version
```

eğer mysql çalışmıyorsa aşağıdaki kod ile onu aktif edebiliriz.
 
```sh
sudo systemctl start mysql
```  

güvenlik ayarlarını yapılandırmak için

```sh
sudo mysql_secure_installation
``` 

Kullanıcılar hakkında genel bilgiyi görmek için

```sh
SELECT user,authentication_string,plugin,host FROM mysql.user;
``` 

Şifreyi bu şekilde de değiştirebiliriz. Önce terminalden mysql e giriş yapalım

```sh
sudo mysql;
``` 

```sh
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Optimak.123';
``` 

değişikliklerin aktif edilmesi için

```sh
FLUSH PRIVILEGES;
``` 

çıkış yapmak için
```sh
exit
``` 

Artık şifre belirlediğimiz için tekrardan giriş yaparken aşağıdaki kod ile mysql terminal ekranı açılır. Daha önce belirlediğimiz şifreyi soracaktır.

```sh
sudo mysql -u root -p
``` 

yeni bir kullanıcı oluşturacaksak

```sh
CREATE USER 'bilal'@'localhost' IDENTIFIED BY 'Bilal.123';
``` 

daha sonra oluşturduğumuz bu kullanıcıya ayrıcalıklar verebiliriz.

```sh
GRANT ALL PRIVILEGES ON *.* TO 'bilal'@'localhost' WITH GRANT OPTION;
``` 

yine değişiklikleri aktif etmek için

```sh
FLUSH PRIVILEGES;
``` 

mevcut kullanıcıları görebilmek için
```sh
SELECT User, Host FROM mysql.user;
``` 

kullanıcı silmek için
```sh
DROP USER 'bilal'@'localhost';
``` 


mysql durumunu sorgulamak için

```sh
systemctl status mysql.service
``` 


# -----------------------------------------------------------------------------
# 🚀 MYSQL WORKBENCH KURULUMU VE KULLANIMI

`Ubuntu software` yardımı ile `mysql workbench` kurulumunu gerçekleştirebiliriz

<p align="center">
  <img width="700" height="400" src="image/workbench_screen.png?raw=true">
</p>


Ayrıca [linkten](https://dev.to/gsudarshan/how-to-install-mysql-and-workbench-on-ubuntu-20-04-localhost-5828) yararlanılarak da kurulum yapılabilir

Yukarıda belirtildiği gibi oluşturduğumuz kullanıcı ve şifresini kullanarak `MySQL Workbench` de database için bir bağlantı oluşturalım

<p align="center">
  <img width="1000" height="600" src="image/baglanti.gif?raw=true">
</p>





Ayrıca yukarıdaki metotla kullanıcı oluşturabildiğimiz gibi `MySQL Workbench` kullanarak da kullanıcı oluşturup izinlerini verebiliriz. 

<p align="center">
  <img width="1000" height="600" src="image/kullanıcı oluşturma.gif?raw=true">
</p>


oluşturduğumuz bu kullanıcıyı kullanarak bir bağlantı oluşturalım ve database e bağlanalım

<p align="center">
  <img width="1000" height="600" src="image/baglantı_olusturma.gif?raw=true">
</p>


# -----------------------------------------------------------------------------
# 🚀 TEMEL SEVİYEDE DATABASE KODLARI

Terminalden `MySQL` ekranına giriş yapıldıktan sonra aşağıdaki kod ile yeni bir database oluşturulabilir

```sh
create database veriler_guncel;
``` 

<p align="center">
  <img width="700" height="400" src="image/database_create.png?raw=true">
</p>

bu şekilde oluşturulan database i `MySQL Workbench` içerisinde de görebiliriz

<p align="center">
  <img width="700" height="400" src="image/database_creatae_workbench.png?raw=true">
</p>


mevcut database leri görebilmek için
```sh
show databases;
``` 

İstenilen database i silmek için
```sh
drop database veriler_guncel;
``` 

istenilen database e geçiş yapmak için
```sh
use veriler_guncel;			
``` 

aktif olan database de tablo oluşturmak için, örneğin musteri isimli tablo oluşturuldu ve içine başlıklar eklendi
```sh
create table musteri(ad varchar(20), soyad varchar(20), tcno varchar(20), dogum date);	
``` 

musteri isimli tablonun özelliklerini görüntülemek için
```sh
desc musteri;
``` 

musteri isimli tabloya veri eklemek için
```sh
insert into musteri values ("bilal", "gurevin", "28699121212", "1980-05-14");
``` 	

musteri isimli tablonun güncel halini gösterir
```sh
select * from musteri;
``` 

musteri isimli tablo silme 
```sh
drop table musteri;
``` 