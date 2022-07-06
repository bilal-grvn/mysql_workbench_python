# !/usr/bin/python3
# -*- coding: utf-8 -*-
import pymysql.cursors
import sqlite3

class data_base_study:

    def __init__(self):

        self.DATABASE_CONNECTION_STATUS = False
        self.database_ip = '127.0.0.1'  # 'localhost' yazılsa da olur / farklı bir pc ye bağlanılacaksa o pc nin IP si yazılır
        self.database_user = 'bilal'
        self.database_pass = 'bilal123'
        self.database_adi = 'veriler_guncel'

        self.connect_database()
        #self.read_from_database()
        #self.write_to_database()
        #self.delete_row_database()
        #self.adding_row()
        #self.adding_column()
        #self.delete_column_database()

    def connect_database(self):
        try:
            self.db = pymysql.connect(host=self.database_ip,
                                      user=self.database_user,
                                      password=self.database_pass,
                                      db=self.database_adi,
                                      charset='utf8mb4',
                                      autocommit=True,
                                      cursorclass=pymysql.cursors.DictCursor)
            self.DATABASE_CONNECTION_STATUS = True
            print("CONNECTED...")
        except Exception as e:
            print("connect_database ERROR :", str(e))
            pass

    def read_from_database(self):
        try:
            arac_adi = input("arac ismi = ")
            if self.DATABASE_CONNECTION_STATUS:
                print(self.DATABASE_CONNECTION_STATUS)
                with self.db.cursor() as sqlcursor:
                    sqlcursor.execute("SELECT * FROM twist_verileri WHERE arac_adi='{}';".format(arac_adi))
                    data = sqlcursor.fetchone()
                    print(data)
                    print(data["linear_x"])
        except Exception as e:
            print("read_from_database ERROR : ", str(e))
            pass

    def write_to_database(self):
        try:
            arac_adi = input("arac ismi = ")
            if self.DATABASE_CONNECTION_STATUS:
                with self.db.cursor() as sqlcursor:
                    sqlcursor.execute("UPDATE twist_verileri SET toggle_control='{}', linear_x ='{}',angular_z='{}' WHERE "
                        "arac_adi='{}';".format(9, 0.5, 0.75, arac_adi))

        except Exception as e:
            print("write_to_database ERROR : ", str(e))
            pass

    def delete_row_database(self):
        try:
            arac_adi = input("arac ismi = ")
            if self.DATABASE_CONNECTION_STATUS:
                with self.db.cursor() as sqlcursor:
                    sqlcursor.execute("DELETE FROM twist_verileri WHERE arac_adi='{}';".format(arac_adi))

        except Exception as e:
            print("delete_from_database ERROR : ", str(e))
            pass

    def adding_row(self):
        try:
            if self.DATABASE_CONNECTION_STATUS:
                with self.db.cursor() as sqlcursor:
                    sqlcursor.execute("INSERT INTO twist_verileri (`arac_adi`, `toggle_control`, `linear_x`, `angular_z`) VALUES ('arac6', '1', '0', '0');")
        except Exception as e:
            print("adding_row ERROR : ", str(e))
            pass

    def delete_column_database(self):
        try:
            sutun_adi = input("sutun ismi = ")
            if self.DATABASE_CONNECTION_STATUS:
                with self.db.cursor() as sqlcursor:
                    sqlcursor.execute("ALTER TABLE twist_verileri DROP {};".format(sutun_adi))

        except Exception as e:
            print("delete_column_database ERROR : ", str(e))
            pass

    def adding_column(self):
        try:
            if self.DATABASE_CONNECTION_STATUS:
                with self.db.cursor() as sqlcursor:
                    sqlcursor.execute("ALTER TABLE twist_verileri ADD bilal VARCHAR(100);")

        except Exception as e:
            print("adding_colomb ERROR : ", str(e))
            pass

if __name__ == "__main__":
    try:
        data_base_study()
    except Exception as e:
        print("Starting ERROR", str(e))
        pass