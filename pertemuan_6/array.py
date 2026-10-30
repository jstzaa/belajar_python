cars = ["Ford", "Volvo", "BMW", 2, True]

print(cars[0])

cars[0] = "Toyota"

print(cars)

print(type(cars))

x = len(cars)

print(x)

for x in cars:
    print(x)

i = 0
while i < len(cars):
    print(cars[i])
    i += 1

cars.append("Honda")
print(cars)

cars.insert(2, False)
print(cars)

cars.pop(1)
print(cars)

cars.remove("BMW")
print(cars)