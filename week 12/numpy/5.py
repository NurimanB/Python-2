import numpy as np

numbers = np.random.rand(20)

mean_value = np.mean(numbers)
median_value = np.median(numbers)
variance_value = np.var(numbers)
std_deviation = np.std(numbers)

print("Random Numbers Array:\n", numbers)
print("\nMean:", mean_value)
print("Median:", median_value)
print("Variance:", variance_value)
print("Standard Deviation:", std_deviation)
