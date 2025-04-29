import matplotlib.pyplot as plt 


# Sample data
students = ['Alice', 'Bob', 'Charlie', 'David']
marks = [85, 72, 90, 65]

# Create bar chart
plt.bar(students, marks, color='skyblue')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.title('Marks of Students')
plt.show()
