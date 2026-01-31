class Employee:
  def __init__(self,name,emp_id):
    self.name=name
    self.emp_id=emp_id
  def calculate_salary(self):
    pass

  def display_details(self):
    print("Name:",self.name)
    print("Employee ID:",self.emp_id)

class FullTimeEmployee(Employee):
  def __init__(self,name,emp_id,monthly_salary):
    super().__init__(name,emp_id)
    self.monthly_salary = monthly_salary
  def calculate_salary(self):
    return self.monthly_salary
class PartTimeEmployee(Employee):
  def __init__(self,name,emp_id,hours_worked,hourly_rate):
    super().__init__(name,emp_id)
    self.hours_worked = hours_worked
    self.hourly_rate = hourly_rate


  def calculate_salary(self):
    return self.hours_worked * self.hourly_rate


Burair = FullTimeEmployee("burair","k0804",500000)
Burair.display_details()
print("Burair's Salary:",Burair.calculate_salary())

Leenah = PartTimeEmployee("Leenah","K1022",12,1000)
Leenah.display_details()
print("Leenah's Salary:",Leenah.calculate_salary())


