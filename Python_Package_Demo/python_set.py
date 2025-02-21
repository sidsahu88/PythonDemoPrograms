l = ['Starlord', 'Ironman', 'Gamora', 'Groot', 'Ironman', 'Rocket']

print(l)

lset = set(l)  # No duplicates in set

print(lset)

lset.add('Spiderman')
lset.add('Drax')
lset.add('Groot')
lset.discard('Ironman')
print(lset)
