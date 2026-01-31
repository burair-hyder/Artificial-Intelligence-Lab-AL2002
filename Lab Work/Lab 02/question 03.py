# TASK 3
class Student:
  def __init__(self,name,student_id):
    self.name = name
    self.__marks = 0
    self.student_id = student_id

  def set_marks(self,marks):
    if marks < 0 or marks > 100:
      print("Invalid Marks")
    else:
      self.__marks = marks

  def get_marks(self):
    return self.__marks 

  def calculate_grade(self):
    if self.__marks >= 90:
      return 'A'
    elif self.__marks >= 80:
      return 'B'
    elif self.__marks >= 70:
      return 'C'
    elif self.__marks >= 60:
      return 'D'
    else:
      return 'F'
Burair = Student('Burair',123)
Burair.set_marks(95)
print(Burair.name,"Marks:",Burair.get_marks(),"Grade:",Burair.calculate_grade())
Leenah = Student('Leenah',124)
Leenah.set_marks(85)
print(Leenah.name,"Marks:",Leenah.get_marks(),"Grade:",Leenah.calculate_grade())
