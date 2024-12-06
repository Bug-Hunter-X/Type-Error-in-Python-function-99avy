def function(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return "Error: Invalid input types"

result = function(5, '10')
print(result)

result2 = function(5, 10)
print(result2)