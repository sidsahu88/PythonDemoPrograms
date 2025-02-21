import numpy as np

for item in ['Sid', 'Git', 'Kanha', 'Lisha']:
    print(item)

print()

# range(start, end, increment)
for num in range(5, 10, 2):
    print(num)

print()

for _ in [1, 2, 3, 4, 5]:
    print("For without initialization.")

print()

radii = [10, 2, 5.2, 8, 0.4]

for i, radius in enumerate(radii):
    area = np.pi * pow(radius, 2)
    print(f'Area of circle {i} with radius {radius} = {area}')
