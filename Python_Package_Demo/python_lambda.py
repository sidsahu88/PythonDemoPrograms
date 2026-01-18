func = lambda x: 3 * x + 1

print(func(2))

full_name = lambda firstname, lastname: firstname.strip().title() + " " + lastname.strip().title()

print(full_name("             siddharth", "SAHU  "))


def build_quadratic_function(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


f = build_quadratic_function(2, 3, -5)

print(f(0))
print(f(1))
print(f(2))


def preform_operation_on_list(lst, func):
    return [func(x) for x in lst]

list_of_numbers = [1, 2, 3, 4, 5]
print("list_of_numbers:", list_of_numbers)

result_squared_list = preform_operation_on_list(list_of_numbers, lambda x: x ** 2)
print("result_squared_list:", result_squared_list)

result_cubed_list = preform_operation_on_list(list_of_numbers, lambda x: x ** 3)
print("result_cubed_list:", result_cubed_list)