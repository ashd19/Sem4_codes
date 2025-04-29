import matplotlib.pyplot as plt

# Sample data: marks scored by students
marks = [55, 60, 65, 70, 70, 72, 75, 78, 80, 85, 85, 88, 90, 92, 95, 98, 100]

# Create histogram
plt.figure(figsize=(8, 5))  # Set figure size
plt.hist(marks, bins=7, color='royalblue', edgecolor='black')

# Add labels and title
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.title('Histogram of Student Marks')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
