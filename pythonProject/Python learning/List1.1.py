cars = ['bmw', 'vw', 'fiat', 'skoda', 'lada', 'honda']

print(cars)

for x in cars:
    print(x.upper())

for x in range(1, 6):
    print(x)

number_list = list(range(0, 10))
print(number_list)

for x in number_list:
    x = x * 2
    print(x)

number_list.sort(reverse = True)
print(number_list)

print("Max number is " + str(max(number_list)))
print("Min number is " + str(min(number_list)))
print("Sum of list is " + str(sum(number_list)))

cars = ['bmw', 'vw', 'fiat', 'skoda', 'lada', 'honda']

my_cars = cars[1:4]
print(my_cars)

my_cars = cars[:4]
print(my_cars)

number_list2 = number_list[3: 5]
print(number_list2)

number_list2 = number_list[:]
