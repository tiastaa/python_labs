class Car:
    def __init__(self, brand="-", colour="-" , number="-" , manufacturer_firm="-", manufacturer_foundation="-" , manufacturer_phone_number="-",manufacturer_car_per_year="-" ,seller_firm="-", seller_foundation="-" , seller_phone_number="-", seller_car_per_year="-" , owner_name="-", owner_id="-" , owner_number="-" ,release_date="-" ):
        self.brand = brand
        self.colour=colour
        self.number=number
        self.manufacturer=Manufacturer(manufacturer_firm, manufacturer_foundation , manufacturer_phone_number,manufacturer_car_per_year)
        self.seller=Seller(seller_firm, seller_foundation, seller_phone_number, seller_car_per_year )
        self.owner=Owner( owner_name, owner_id , owner_number)
        self.release=Release(release_date)
    def get_age(self):
        return 2021-int(self.release)
    def get_owner_number(self):
        return int(self.owner)
    def __str__(self):
        return 'Number (a={0})'.format(self.a)
class Manufacturer:
    def __init__(self, manufacturer_firm="-", manufacturer_foundation="-" , manufacturer_phone_number="-", manufacturer_car_per_year="-" ):
        self.manufacturer_firm=manufacturer_firm
        self.manufacturer_foundation=manufacturer_foundation
        self.manufacturer_phone_number = manufacturer_phone_number
        self.manufacturer_car_per_year = manufacturer_car_per_year

class Owner:
    def __init__(self, owner_name="-", owner_id="-", owner_number="-"  ):
        self.owner_name=owner_name
        self.owner_id=owner_id
        self.owner_number=owner_number
    def __int__(self):
        return int(self.owner_number)

class Seller:
    def __init__(self, seller_firm="-", seller_foundation="-" , seller_phone_number="-", seller_car_per_year="-" ):
        self.seller_firm=seller_firm
        self.seller_foundation=seller_foundation
        self.seller_phone_number = seller_phone_number
        self.seller_car_per_year = seller_car_per_year

class Release:
    def __init__(self, release_date="-" ):
        self.release_date=release_date
    def __int__(self):
        return int(self.release_date)

car=Car("Lamborghini" , "чорний" , "МО 7777 АА" , "Lamborghini" , 1870 , "+380990145966" ,29399402 , "Авто дешево" , 2005 , "+0509093027" , 900, "Йовбак НІ", 29392099 ,3, 2003)
print(car.get_age())
print(car.get_owner_number())
