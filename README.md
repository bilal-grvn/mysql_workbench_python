<h1 align="center">
👋 Herkese Selamlar 👋
</h1>


## `Ubuntu 18.04`'te  temel seviyede database işlemlerini gerçekleştirmeye çalıştım. Bunun için `MySQL`, `MySQL Workbench`  kullandım. Ayrıca `Python` programlama dili ile de yine temel seviyede bazı database işlemlerini gerçekleştirdim. Umarım sizlere de katkısı olur.

# -----------------------------------------------------------------------------
# 🚀 MYSQL KURULUMU

[linkten](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04) kaynak bilgiye ulaşabilirsiniz.


```sh
$ sudo apt update
```

```sh
$ sudo apt install mysql-server
```
kurulan mysql versiyonunu kontrol edebiliriz
```sh
$ mysql --version
```

```sh
$ sudo systemctl start mysql.service
```   

güvenlik ayarlarını yapılandırmak için
```sh
$ sudo mysql_secure_installation
``` 

```sh
$ SELECT user,authentication_string,plugin,host FROM mysql.user;
``` 
```sh
$ ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
``` 
```sh
$ FLUSH PRIVILEGES;
``` 

çıkış yapmak için
```sh
$ exit
``` 

tekrardan giriş yapmak için
```sh
$ sudo mysql -u root -p
``` 


<p align="center">
  <img width="500" height="350" src="image/workbench_screen.png?raw=true">
</p>


# -----------------------------------------------------------------------------
# 🚀 MYSQL WORKBENCH KURULUMU

izinleri vermek önemli, yoksa kullanıcı ekleyemeiyoruz.

# -----------------------------------------------------------------------------
# 🚀 TEMEL SEVİYEDE PYTHON DATABASE KODLARI


EK olarak [nmcli](https://www.cyberithub.com/30-nmcli-command-examples-in-linux-rhel-centos-cheat-sheet/) kodlarını kullanarak da wifi ile ilgili bir çok işlem yapılabilir.