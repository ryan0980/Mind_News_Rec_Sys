'''

|   SVD k |   Time (s) |   Single User Time (s) |   100 Users Time (s) |   Average Recall |   Average Precision |
|--------:|-----------:|-----------------------:|---------------------:|-----------------:|--------------------:|
|      10 |         49 |                    0.3 |                  1.2 |           0.0013 |              0.0002 |
|      50 |         37 |                    0.1 |                  1   |           0.0174 |              0.0004 |
|      20 |         50 |                    0.2 |                  1.1 |           0.0129 |              0.0004 |
|     100 |         96 |                    0.1 |                  1.1 |           0.0112 |              0.0003 |
|    1000 |        199 |                    0.2 |                  0.9 |           0.0063 |              0.0003 |



'''


import matplotlib.pyplot as plt

# Data
svd_k = [10, 20, 50, 100, 1000]
average_recall = [0.0013, 0.0129, 0.0174, 0.0112, 0.0063]
average_precision = [0.0002, 0.0004, 0.0004, 0.0003, 0.0003]

# Plot Average Recall and Precision vs. SVD k
plt.figure(figsize=(10, 6))
plt.plot(svd_k, average_recall, marker='o', linestyle='-', color='blue', label='Average Recall')
plt.plot(svd_k, average_precision, marker='o', linestyle='-', color='green', label='Average Precision')
plt.xlabel('SVD k')
plt.ylabel('Value')
plt.title('Average Recall and Precision vs. SVD k')
plt.legend()
plt.grid(True)

# Set x-axis to logarithmic scale
plt.xscale('log')
plt.xticks(svd_k)
plt.gca().get_xaxis().set_major_formatter(plt.ScalarFormatter())

plt.show()




import matplotlib.pyplot as plt

# Data
svd_k = [10, 20, 50, 100, 1000]
total_time_s = [49, 50, 37, 96, 199]
single_user_time_s = [0.3, 0.2, 0.1, 0.1, 0.2]
hundred_users_time_s = [1.2, 1.1, 1.0, 1.1, 0.9]

# Create a figure and a set of subplots
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Total Time on the first y-axis
color = 'tab:red'
ax1.set_xlabel('SVD k')
ax1.set_ylabel('Total SVD Matrix Time (s)', color=color)
ax1.plot(svd_k, total_time_s, marker='o', linestyle='-', color=color, label='Total SVD Matrix Time')
ax1.tick_params(axis='y', labelcolor=color)

# Set x-axis to logarithmic scale
ax1.set_xscale('log')
ax1.set_xticks(svd_k)
ax1.get_xaxis().set_major_formatter(plt.ScalarFormatter())

# Instantiate a second y-axis that shares the same x-axis
ax2 = ax1.twinx()

# Plot User Times on the second y-axis
color = 'tab:blue'
ax2.set_ylabel('User Time (s)', color=color)
ax2.plot(svd_k, single_user_time_s, marker='o', linestyle='-', color=color, label='Single User Time')
ax2.plot(svd_k, hundred_users_time_s, marker='o', linestyle='-', color='green', label='100 Users Time')
ax2.tick_params(axis='y', labelcolor=color)

# Add legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

plt.title('User Time and Total Time vs. SVD k')
plt.grid(True)
plt.tight_layout()
plt.show()
