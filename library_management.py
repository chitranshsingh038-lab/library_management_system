import pymysql
import pandas as pd
import time 
a=time.localtime()
b=time.strftime("%d-%m-%Y",a)

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='pass123',
    database='library',
    port=3306
)

print("Connection successful!")

# --- programming of library ---

# ---- INSERTING STUDENT IN DATABASE ----

def insert_student():    
   while True:

      student=input("enter the name of the student :").strip().lower()

      if (student==""):
         break

      class_=input("enter the class of ths student :")
      sql="insert into student(s_name,s_class) values(%s,%s)"
      values=(student,class_)
      cursor=connection.cursor()
      cursor.execute(sql,values)
      connection.commit()
      
      print("data inserted successfully")
   

#-----------------------------------------------------------------------------------------------------   

def delete_student():
   sql="select * from student"
   cursor=connection.cursor()
   cursor.execute(sql)
   result=cursor.fetchall()
   for row in result:
      print(row)

   student_id=int(input("Enter student_id :"))
   sql="delete * from student where student_id=%s"
   values=(student_id) 
   cursor=connection.cursor()
   cursor.execute(sql,values) 
   connection.commit()
   print("student deleted successfully") 

#-----------------------------------------------------------------------------------------------------

def insert_book():
   while True:
      book=input("enter the name of book").strip().lower()     # Name of books

      if (book==""):
         break 

      author=input("enter the name of author").strip().lower() # name of author
      no=int(input("enter no of books"))        #no. of books
   
      sql="insert into books(book_name,author,no_of_books)values(%s,%s,%s)"
      values=(book,author,no)
      cursor=connection.cursor()
      cursor.execute(sql,values)
      connection.commit()
      
      print("book is inserted")
         

# ----------------------------------------------------------------------------------------------------

def issuing_book():

   student_id=int(input("enter the id of student :"))
   book_id =int(input("enter the book_id :"))
   borrow_date=b
   sql="select no_of_books from books where book_id=%s"
   values=(book_id)
   cursor=connection.cursor()
   s=cursor.execute(sql,values)
   if(s<=0):
      print("book is not available ")

   else:
      sql1="insert into issue_book(student_id,book_id,date_of_issue)values(%s,%s,%s)"
      values1=(student_id,book_id,borrow_date)
   
      sql2="update books set no_of_books=no_of_books-1 where book_id=%s"
      values2=(book_id)
   
      cursor=connection.cursor()
      cursor.execute(sql1,values1)
      cursor.execute(sql2,values2)
      connection.commit()

#-----------------------------------------------------------------------------------------------------

def returning_book():
   returning_date=b
   cursor=connection.cursor()
   sql="select * from issue_book "
   cursor.execute(sql)
   result=cursor.fetchall()
   for row in result:
      print(row)

   borrow_id=int(input("enter your borrow_id :"))
   sql1="update issue_book set returning_date=%s where borrow_id=%s"
   values1=(b,borrow_id)

   sql2="update books set no_of_books=no_of_books+1 where book_id=(select book_id from issue_book where borrow_id=%s)"
   values2=(borrow_id)

   cursor=connection.cursor()
   cursor.execute(sql1,values1)
   cursor.execute(sql2,values2)
   connection.commit()
                        

def search_book():
   book_name=input("enter the name of book :").strip().lower()  
   sql="select * from books where book_name=%s"
   values=(book_name)
   cursor=connection.cursor()
   result=cursor.execute(sql,values)                 

print("enter 1 for insert new student in database :\nenter 2 for delete student from database :\n"
       "enter 3 for search any student :\nenter 4 insert book :\nenter 5 for search book :\n" 
       "enter 6 for issue_book\nenter 7 for return book\nenter 8 for exit")

a=int(input("enter a number :"))

if (a==1):
   insert_student()
if (a==2):
   delete_student()   
if (a==3):
   pass
if (a==4):
   insert_book()
if (a==5):
   search_book()
if (a==6):
   issuing_book()
if (a==7):
   returning_book()




