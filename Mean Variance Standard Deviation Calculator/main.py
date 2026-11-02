
from mean_var_std import calculate

result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

print(result)
print("\nMean:", result['mean'])
print("Sum:", result['sum'])

# Test invalid input
try:
    calculate([1, 2, 3])
except ValueError as e:
    print(e)
