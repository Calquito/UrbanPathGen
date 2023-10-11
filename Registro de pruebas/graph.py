import matplotlib.pyplot as plt

# Sample data (replace these with your own lists)
x_values = [1, 2, 3, 4, 5 , 6]
y1_values = [0.098804,0.107684,0.117711,0.139421,0.148520,0.168593]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the first line
ax.plot(x_values, y1_values, marker='o', linestyle='-', color='blue')

ax.set_ylim(0.08, 0.19)
custom_xticks = [1, 2, 3, 4, 5 , 6]
ax.set_xticks(custom_xticks)

# Add labels and a legend
ax.set_xlabel('Cantidad de drones')
ax.set_ylabel('Tiempo de inferencia promedio(s)')
ax.set_title('Tiempo de inferencia promedio vs Cantidad de drones')
ax.legend()

# Save the plot as an image (optional)
# plt.savefig('plot.png')

# Display the plot
plt.show()