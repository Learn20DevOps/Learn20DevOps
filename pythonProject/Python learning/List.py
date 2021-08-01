Cities = ['Kyiv', 'moscov', 'New York', 'Minsk', 'London', 'Lviv', 'rom', 'Paris']

print(Cities)
print(len(Cities))
print(Cities[0])
print(Cities[-1])
print(Cities[1].title())

Cities[2] = 'bagdad'
print(Cities)

Cities.append('New York')
print(Cities)

Cities.insert(2, 'pekin')
print(Cities)

del Cities[3]
print(Cities)

Cities.remove('Minsk')
print(Cities)

deleted_city = Cities.pop()
print(deleted_city)

#Cities.sort()
#print(Cities)

#Cities.sort(reverse=True)
#print(Cities)

Cities.reverse()
print(Cities)
  