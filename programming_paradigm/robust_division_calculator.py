def robust_division_calculator(numerator, denominator):
    try:
       num = float(numerator)
       denom = float(denominator)

       result = num / denom
       return f'Result: {result}'
    
    except ZeroDivisionError:
        return f'Error: Cannot divide by zero'
    except ValueError:
        return f"Error: Please enter a valid number"
