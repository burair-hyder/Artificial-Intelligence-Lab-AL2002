class Vehicle:
  def __init__(self,vehicle_id,brand,rent_per_day):
    self.vehicle_id = vehicle_id
    self.brand = brand
    self.rent_per_day = rent_per_day
  
  def display_details(self):
    print("Vehicle ID:",self.vehicle_id)
    print("Brand:",self.brand)
    print("Rent per day:",self.rent_per_day)

  def calculate_rent(self,days):
    amount = self.rent_per_day * days
    return amount
  
car1 = Vehicle("ALW-891","Toyota",500)
car1.display_details()
print("Total Rent For Car:",car1.vehicle_id," is ",car1.calculate_rent(5))
print("Total Rent For Car:",car1.vehicle_id," is ",car1.calculate_rent(2))


car2 = Vehicle("GSC-808","Toyota",1500)
car2.display_details();
print("Total Rent For Car:",car2.vehicle_id," is ",car2.calculate_rent(8))
print("Total Rent For Car:",car2.vehicle_id," is ",car2.calculate_rent(4))


