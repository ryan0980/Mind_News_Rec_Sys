import matplotlib.pyplot as plt
import pandas as pd

# Data for each recommendation type
data = {
    "Top N": [10, 100, 1000, 10000],
    "User-based Recall": [0.1559, 0.4833, 0.6367, 0.8426],
    "User-based Precision": [0.0640, 0.0240, 0.0077, 0.0046],
    "Content-based Recall": [0.0018, 0.0180, 0.0832, 0.3448],
    "Content-based Precision": [0.0010, 0.0006, 0.0004, 0.0002],
    "SVD Recall": [0.0028, 0.0128, 0.0267, 0.1425],
    "SVD Precision": [0.0020, 0.0003, 0.0001, 0.0001]
}

# Create DataFrame
df = pd.DataFrame(data)


# Plotting in one figure
plt.figure(figsize=(10, 6))

# User-based Recall and Precision
plt.plot(df['Top N'], df['User-based Recall'], label='User-based Recall', marker='o')
plt.plot(df['Top N'], df['User-based Precision'], label='User-based Precision', marker='o')

# Content-based Recall and Precision
plt.plot(df['Top N'], df['Content-based Recall'], label='Content-based Recall', marker='o')
plt.plot(df['Top N'], df['Content-based Precision'], label='Content-based Precision', marker='o')

# SVD Recall and Precision
plt.plot(df['Top N'], df['SVD Recall'], label='SVD Recall', marker='o')
plt.plot(df['Top N'], df['SVD Precision'], label='SVD Precision', marker='o')

# Title and labels
plt.title('Recall and Precision for Different Recommendation Methods')
plt.xlabel('Top N')
plt.ylabel('Score')

# Set x-scale to logarithmic
plt.xscale('log')

# Add legend and grid
plt.legend()
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
