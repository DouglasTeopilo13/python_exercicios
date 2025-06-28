motorcycles = ['Honda', 'Yamaha', 'Kawasaki', 'Suzuki', 'Ducati']
motorcycles [0]= 'BMW'
print(motorcycles)
motorcycles[1] = 'Triumph'
print(motorcycles)
motorcycles [2] = 'Harley-Davidson'
motorcycles[3] = 'KTM'
print(motorcycles)
motorcycles.append('Aprilia')
print(motorcycles)
motorcycles.insert(3, 'lamborghini')
print(motorcycles)
motorcycles.remove('Aprilia')
print(motorcycles)
del motorcycles[-2]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")               
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
