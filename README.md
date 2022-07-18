<h1 align="center">
👋 Herkese Selamlar 👋
</h1>


## `Ubuntu 18.04`'te  temel seviyede database işlemlerini gerçekleştirmeye çalıştım. Bunun için `MySQL`, `MySQL Workbench`  kullandım. Ayrıca `Python` programlama dili ile de yine temel seviyede bazı database işlemlerini gerçekleştirdim. Umarım sizlere de katkısı olur.

# -----------------------------------------------------------------------------
# 🚀 MYSQL KURULUMU

[linkten](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04) kaynak bilgiye ulaşabilirsiniz.


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

```sh
sudo systemctl start mysql.service
```   

güvenlik ayarlarını yapılandırmak için

```sh
sudo mysql_secure_installation
``` 

Kullanıcılar hakkında genel bilgiyi görmek için

```sh
SELECT user,authentication_string,plugin,host FROM mysql.user;
``` 

Şifreyi bu şekilde de değiştirebiliriz

```sh
sudo mysql;
``` 

```sh
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
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
CREATE USER 'bilal'@'localhost' IDENTIFIED BY 'password';
``` 

daha sonra oluşturduğumuz bu kullanıcıya ayrıcalıklar verebiliriz.

```sh
GRANT ALL PRIVILEGES ON *.* TO 'bilal'@'localhost' WITH GRANT OPTION;
``` 

yine değişiklikleri aktif etmek için

```sh
FLUSH PRIVILEGES;
``` 

mysql durumunu sorgulamak için

```sh
systemctl status mysql.service
``` 

eğer mysql çalışmıyorsa aşağıdaki kod ile onu aktif edebiliriz.
 
```sh
sudo systemctl start mysql
``` 

# -----------------------------------------------------------------------------
# 🚀 MYSQL WORKBENCH KURULUMU VE KULLANIMI

`Ubuntu software` yardımı ile `mysql workbench` kurulumunu gerçekleştirebiliriz

<p align="center">
  <img width="500" height="350" src="image/workbench_screen.png?raw=true">
</p>


Ayrıca [linkten](https://dev.to/gsudarshan/how-to-install-mysql-and-workbench-on-ubuntu-20-04-localhost-5828) yararlanılarak da kurulum yapılabilir

Yukarıda belirtildiği gibi oluşturduğumuz kullanıcı ve şifresini kullanarak `MySQL Workbench` de database için bir bağlantı oluşturalım

<p align="center">
  <img width="600" height="360" src="image/baglanti.gif?raw=true">
</p>

# -----------------------------------------------------------------------------
# 🚀 TEMEL SEVİYEDE PYTHON DATABASE KODLARI
