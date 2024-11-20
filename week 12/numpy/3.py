import numpy as np

array = np.random.randint(1, 101, size=20)

filtered_array = array[array % 5 == 0]

print("Original Array:\n", array)
print("\nFiltered Array (Divisible by 5):\n", filtered_array)
