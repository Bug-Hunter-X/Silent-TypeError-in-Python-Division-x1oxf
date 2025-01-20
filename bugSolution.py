def function_with_uncommon_error_solution(x, y):
    try:
        if not isinstance(y, (int, float)):
            raise TypeError("Divisor must be a number.")
        result = x / y
        return result
    except ZeroDivisionError:
        return float('inf')
    except TypeError as e:
        return f'Error: {e}' 

# This now raises a more informative error
print(function_with_uncommon_error_solution(10, 'a')) # Output: Error: Divisor must be a number.