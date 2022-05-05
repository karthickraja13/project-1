import mysql.connector
from tabulate import tabulate
def insert(name, password):
    mydb = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="new_project")
    data = mydb.cursor()
    sql = "INSERT INTO file(name,password )values(%s,%s)"
    user = (name,password)
    data.execute(sql, user)
    mydb.commit()
    data.close()
    mydb.close()
    print("insert is success")


def update(id, name, password):
    mydb = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="python")
    data = mydb.cursor()
    sql = "UPDATA file SET name=%s,password=%s WHERE id=%s"
    # user = (id,name,password)
    data.execute(sql)
    mydb.close()
    data.close()
    mydb.commit()
    print("update is success")


def select():
    mydb = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="python")
    data = mydb.cursor()
    sql = "select ID,NAME,PASSWORD from file"
    data.execute(sql)
    result = data.fetchall()
    print(tabulate(result, headers=["id", "name", "password"]))
    data.close()
    mydb.close()

def delete(id):
    mydb = mysql.connector.connect(host="localhost", port="3306", user="root", password="", database="python")
    data = mydb.cursor()
    sql = "DELET FROM file where id=?"
    user = (id)
    data.execute(sql, user)
    data.close()
    mydb.close()
    mydb.commit()
    print("delete is success")

while True:
    print("1.insert data")
    print("2.update data")
    print("3.select data")
    print("4.delete data")
    print("5.exit")
    choice = int(input("Enter the choice:"))
    if choice == 1:
        name = input("Enter the name:")
        password = input("Enter the password:")
        insert(name, password)
    elif choice == 2:
        id = input("Enter the id :")
        name = input("Enter the name:")
        password = input("Enter the password:")
        update(id, name, password)
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("delete id :")
        delete(id)
    elif choice == 5:
        exit()
    else:
        print("please try again")