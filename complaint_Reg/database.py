import sqlite3
def createTables():
    try:
        conn=sqlite3.connect("data.db")
        query='''create table user(id integer primary key,name varchar(50) not null,phone varchar(10) not null )'''


        conn.execute(query)
        conn.commit()
        
        query='''create table department(id int primary key,name varchar(15) not null)'''
        conn.execute(query)
        conn.commit()

        query='''create table complaint(id integer primary key,description text not null,userid integer,deptid int,foreign key (userid) references user(id),foreign key (deptid) references department(id))'''
        conn.execute(query)
        conn.commit()
        print("Table created")
    except Exception as e:
        print(e)

#if __name__=='__main__':
 #    createTables()    

def addUser(name,phone):
    try:
        conn=sqlite3.connect("data.db")
        query="""insert into user(name,phone) values(?,?)"""
        conn.execute(query,(name,phone))
        conn.commit()
        print("User created")
    except Exception as e:
        print(e)
#if __name__=='__main__':
 #    addUser("muttu",'9590877890')
def adddept(id,name):
    try:
        conn=sqlite3.connect("data.db")
        query="""insert into department(id,name)values(?,?)"""
        conn.execute(query,(id,name))
        conn.commit()
        print("Department created")
    except Exception as e:
        print(e)

#if __name__=='__main__':   adddept(101,'Water_department')

def getUser():
    try:
        conn=sqlite3.connect("data.db")
        query="""select * from user"""
        users=conn.execute(query)
        return users.fetchall() 
    except Exception as e:
        print(e)    

def givecomplaint(user_id):
    try:
        conn=sqlite3.connect("data.db")
        query='''insert into complaint(userid,description,deptid,Date) values(?,?,?,?)'''
        description=input("Enter your complaint here")
        dept_id=input("mention the dept id")
        Date=input("Type Date")
        conn.execute(query,(user_id,description,dept_id,Date))
        conn.commit()
    except Exception as e:
        print(e)    

def displaycomplaint():
    try:
        conn=sqlite3.connect("data.db")
        query="""select * from complaint"""
        complaint=conn.execute(query)
        return complaint.fetchall()
    except Exception as e:
        print(e)


def completedetails():
    conn=sqlite3.connect("data.db")
    query="""select * from user,department,complaint"""
    result=conn.execute(query)
    return result.fetchall()
if __name__=='__main__':
  #  print(displaycomplaint())
   # givecomplaint(2)
    # addUser('Pratik','7488909900')
    # addUser('sunil','1234567890')
    # addUser('varun','0987654321')

#     # addUser("pratik","9698764590")
#     # addUser("chandan","7865432190")
       # print(getUser()) 
    print(completedetails())