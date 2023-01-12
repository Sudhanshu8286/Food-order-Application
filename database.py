#1.Create a Food Storage System which perform following Operation on it.
import pymysql as pm
#Food Entity  has Following Properties (foodId, foodName, foodType(Veg/Non-Veg) ,foodPrice)

#. Add Food 
#2. Update Food 
#3. Delete Food 
#4. Show Food List
#5. Show Food by Id
#6. Show Food by Name
#7. Show Food by Type 
#8. Sort Food List by Name
#9. Sort Food List by Price



con= pm.connect(port=3306,user='Localhost',password='',database='food_order_app')
print("connected")

cur= con.cursor()

def createtable():
    sqlQuery="create table if not exists food(foodId int primary key auto_increment, foodName varchar(100) not Null, foodType varchar(50) not Null, foodPrice double(15,2) default 0)"
    i= cur.execute(sqlQuery)
    print(i,'rows affected')
    print("table is created")
    con.commit()

    
def insert(foodName,foodPrice,foodType):
    sqlQuery= f"insert into food (foodName,foodType,foodPrice) values ('{foodName}','{foodType}',{foodPrice})"
    i= cur.execute(sqlQuery)
    print(i,'rows affected')
    con.commit()


def update(foodId,foodName,foodPrice,foodDescription):
    sqlQuery= f"update food set foodName='{foodName}',foodPrice={foodPrice},foodDescription='{foodDescription}' where foodId={foodId}"                          
    i= cur.execute(sqlQuery)
    print(i,'rows affected')
    con.commit()


def delete(foodId):
    sqlQuery= f"delete from food where foodId={foodId}"
    i= cur.execute(sqlQuery)
    print(i,'rows affected')
    con.commit()


def getall():
    sqlQuery= "select * from food"
    i= cur.execute(sqlQuery)
    print(i,'row affected')
    rows= cur.fetchall()
    return rows

def getfoodbyid(foodId):
    sqlQuery= f'select * from food where foodId={foodId}'
    i= cur.execute(sqlQuery)
    print(i,'row affected')
    rows= cur.fetchone()
    return rows

def searchbyId(foodId):
    sqlQuery= f"select* from food where foodId={foodId}"
    i= cur.execute(sqlQuery)
    print(i,'row is affected')
    row=  cur.fetchone()
    return row

def searchbyname(foodName):
    sqlQuery= f"select* from food where foodName='{foodName}'"
    i= cur.execute(sqlQuery)
    print(i,'row is affected')
    row= cur.fetchone()
    return row

def getallbyType(foodType):
    sqlQuery= f"select* from food order by foodName"
    i= cur.execute(sqlQuery)
    print(i,'row is affected')
    rows= cur.fetchall()
    return rows


def sortbyName():
    sqlQuery= f"select* from food order by foodName"
    i= cur.execute(sqlQuery)
    print(i,'row is affected')
    rows= cur.fetchall()
    return rows

def sortbyPrice(foodPrice):
    sqlQuery= f"select* from food order by foodPrice"
    i= cur.execute(sqlQuery)
    print(i,'row is affected')
    rows= cur.fetchall()
    return rows

def closeDB():
    con.close()















    







    
    
    



























