import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Changes made
# Data from the image provided by the user for survival times in months for two different therapies
standard_therapy_data = [
    4, 15, 24, 10, 1, 27, 31, 14, 2, 16, 32, 7, 13, 36, 29, 6, 12, 18, 14, 15, 18, 6, 13, 21, 20, 8, 3, 24
]

new_therapy_data = [
    5, 20, 29, 15, 7, 32, 36, 17, 15, 19, 35, 10, 16, 39, 27, 14, 10, 16, 12, 13, 16, 9, 18, 33, 30, 29, 31, 27
]


# Let's start by creating relative frequency histograms for both datasets
# We first need to decide on the number of bins for the histograms
# A common method is to take the square root of the number of data points
bins_standard = int(np.sqrt(len(standard_therapy_data)))
bins_new = int(np.sqrt(len(new_therapy_data)))

# Create histograms
plt.figure(figsize=(14, 7))

# Histogram for Standard Therapy Data
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
relative_freq_standard, bins_standard, patches_standard = plt.hist(standard_therapy_data, bins=bins_standard, color='blue', edgecolor='black', alpha=0.7, density=True)
plt.title('Standard Therapy Survival Times')
plt.xlabel('Survival time (months)')
plt.ylabel('Relative Frequency')
plt.grid(True)

# Histogram for New Therapy Data
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
relative_freq_new, bins_new, patches_new = plt.hist(new_therapy_data, bins=bins_new, color='green', edgecolor='black', alpha=0.7, density=True)
plt.title('New Therapy Survival Times')
plt.xlabel('Survival time (months)')
plt.ylabel('Relative Frequency')
plt.grid(True)

# Show the histograms
plt.tight_layout()
plt.show()
