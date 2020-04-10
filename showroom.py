showroom = set()
showroom.update(['Tesla', 'Toyota', 'Audi', 'BMW', 'Lexus', 'Volvo'])
showroom.add('Tesla')
showroom.discard('Volvo')


junkyard = set()
junkyard.update(['Tesla', 'Ford', 'Jeep', 'Lexus', 'Audi', 'Subaru'])

overlap = showroom.intersection(junkyard)
both= showroom.union(junkyard)
print(both)
# print(len(list(showroom)))
