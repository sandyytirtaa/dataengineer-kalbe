#Melakukan import mysql connector
import mysql.connector 

#Melakukan percobaan koneksi ke database db
conn = mysql.connector.connect(
        host="localhost", user="root", passwd="12345", database="db" )

#Membuat kursor sebagai penanda 

cursor = conn.cursor()

#Deklarasi SQL Query untuk memasukan record ke DB (KARYAWAN)
insert_sql = (
    "INSERT INTO KARYAWAN (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)"
    "VALUES (%s, %s, %s, %s, %s)"
)
values = ("Qonita", "Faza", "19", "F", "1500000")

try:
    #Eksekusi SQL Command
    cursor.execute(insert_sql, values)

    #Melakukan perubahan (commit) pada DB
    conn.commit()
    print("Berhasil terhubung ke database")

except mysql.connector.Error as err:
    #Roll Back apabila ada issue
    conn.rollback()

#Menutup koneksi
conn.close()
