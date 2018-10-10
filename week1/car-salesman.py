base_car_price = float(input("Enter the base car price: "))
tax = base_car_price * 20 / 100
license = base_car_price * 5 / 100
dealer_prep = 200
destination_charge = 50
car_price_with_extras = base_car_price + tax + license + dealer_prep + destination_charge
print("The price of your car with added extras is: ", car_price_with_extras)
