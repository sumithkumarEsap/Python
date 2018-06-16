class Lib():
    def _init__(self):     #_init constructor
        pass

    def library(self):
        library_Name = "MNLC_UMKC"   # Private data member
        print("Library name is",library_Name)

class Membership():
    fee="$80"
    def __init__(self):  #_init constructor
       print("Membership fee: $80")

class Student_Details():
    #def _init(self): #_init constructor
     #   pass

    def __init__ (self, student_name,student_ID):
        self.student_name = student_name
        self.student_ID = student_ID
        print(self.student_name," with student ID is",self.student_ID)

'''creating a sub class student_details_i from parent clas student_details which inhertis the constructor'''
class Student_Details_i(Student_Details):

    def __init__(self,student_name,student_ID,student_HTOWN):
        Student_Details.__init__(self,student_name,student_ID)
        self.student_HTOWN  = student_HTOWN
        print(self.student_name + " with ID :"+ self.student_ID + " His home town is " + self.student_HTOWN)

class Book_Details():
    def __init__(self,book_name,book_ID,book_author):
        self.book_name=book_name
        self.book_ID=book_ID
        self.book_author=book_author
        print("Book "+self.book_name+" with ID: "+self.book_ID+"/ Author: "+self.book_author)

class SB_Details(Book_Details,Student_Details): #inheritance
    def __init__(self,book_name,book_ID,book_author,borrowdate, returndate):     #_init constructor
        super(). __init__(book_name,book_ID,book_author) #super class
        self.borrowDate = borrowdate
        self.returnDate = returndate
        print("The book was borrowed on "+self.borrowDate+" and has to be returned on "+self.returnDate)
        Book_Details.__init__(self, book_name, book_ID, book_author)
        print("------------------------------------------------------------------------------")
#instances of classes
l1=Lib()
l1.library()
Student_Details("Ashish","20")
Student_Details_i("Sumith","5","kc")
Book_Details("Python","65676778","Dr.LEE")
SB_Details("Ashsih","6538754dg","Ashu","03-20-2018","04-24-2018")

l2=Lib()
l2.library()
Student_Details("Ruthvik","45")
Student_Details_i("Vijaya lakshmi","5","kc")
Book_Details("Deep Learning","6743345"," Sidra ")
SB_Details("DP","6735546","Ashu","06-15-2018","06-27-2018")