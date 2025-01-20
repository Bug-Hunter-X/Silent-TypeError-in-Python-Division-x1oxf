def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return float('inf')
    except TypeError:
        return None

# This won't raise an exception, but it is an uncommon behavior
# Because it does not produce an error message, but rather a unexpected result.
print(function_with_uncommon_error(10, 'a')) # Output: None