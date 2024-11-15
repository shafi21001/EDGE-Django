import math

def maclaurin_series(x, terms):
    sum_series = 0
    for n in range(terms):
        sum_series += x**n / math.factorial(n)
    return sum_series

input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as file:
    lines = file.readlines()
    x = float(lines[0].strip())
    terms = int(lines[1].strip())

approximation = maclaurin_series(x, terms)
actual_value = math.exp(x)
error = abs(actual_value - approximation)

with open(output_file, "w") as file:
    file.write(f"Maclaurin Series Approximation: {approximation}\n")
    file.write(f"Actual Value (e^x): {actual_value}\n")
    file.write(f"Error: {error}\n")

print("Calculation completed. Results written to 'output.txt'.")
