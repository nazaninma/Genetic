import csv
import random

# Function to generate random x and compute f(x)
def function_generator(filename, num_samples):
    # Open a CSV file for writing
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["x", "f(x)"])
        
        # Generate random x values and compute f(x)
        for _ in range(num_samples):
            x = random.uniform(-30, 30)  # Random x in the range [-100, 100]
            f_x =x**2 + 4*x  + 10    # Compute f(x)
            writer.writerow([x, f_x])  # Write x and f(x) to the file

# Parameters
output_file = "1D\dataset.csv"
num_samples = 5000  # Number of samples to generate

# Generate data
function_generator(output_file, num_samples)
