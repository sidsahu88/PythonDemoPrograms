var = lambda x: 3 * x + 1

print(var(2))

full_name = lambda firstname, lastname: firstname.strip().title() + " " + lastname.strip().title()

print(full_name("             siddharth", "SAHU  "))


def build_quadratic_function(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


f = build_quadratic_function(2, 3, -5)

print(f(0))
print(f(1))
print(f(2))

