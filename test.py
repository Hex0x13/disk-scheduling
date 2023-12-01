# import matplotlib.pyplot as plt

# # Sample data representing disk requests
# requests = [5, 8, 12, 20]

# # Calculate the differences between consecutive values
# diffs = [0] + [requests[i + 1] - requests[i] for i in range(len(requests) - 1)]

# # Calculate the cumulative sum of differences to represent disk arm movement
# cumulative_diffs = [sum(diffs[:i+1]) for i in range(len(diffs))]

# # Plotting the graph
# plt.figure(figsize=(8, 6))
# plt.step(range(len(cumulative_diffs)),
#          cumulative_diffs, marker='o', where='mid')

# # Set custom ticks and labels
# plt.xticks(range(len(requests)), requests)
# plt.xlabel('Disk Requests')
# plt.ylabel('Disk Head Movement')
# plt.title('Disk Scheduling Visualization')

# # Show gridlines for better visualization
# plt.grid(True)

# # Display the plot
# plt.show()

import matplotlib.pyplot as plt

# Sample data representing disk requests
requests = [5, 8, 12, 20, 3]

# Calculate the differences between consecutive values
diffs = [0] + [requests[i + 1] - requests[i] for i in range(len(requests) - 1)]

# Calculate the cumulative sum of differences to represent disk arm movement
cumulative_diffs = [sum(diffs[:i+1]) for i in range(len(diffs))]

# Plotting the graph to showcase disk head movement
plt.figure(figsize=(8, 6))

# Plot lines connecting the points representing disk head movement
plt.plot(requests, cumulative_diffs, marker='o', linestyle='-', color='blue')

# Adding labels and title
plt.xlabel('Disk Requests')
plt.ylabel('Disk Head Movement')
plt.title('Disk Scheduling Visualization')

# Show gridlines for better visualization
plt.grid(True)

# Display the plot
plt.show()
