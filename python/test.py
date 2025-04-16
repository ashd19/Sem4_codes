import pandas as p

# ----------------------------
# Basic DataFrame example
# ----------------------------
myds = {"name": ["Ashton"], "div": ["S12"]}
x = p.DataFrame(myds)
print("Basic DataFrame:\n", x)

# ----------------------------
# Creating a Series with subject marks
# ----------------------------
a = [60, 74, 68, 92, 93]
var1 = p.Series(a, index=["OS", "AT", "CN", "EM", "COA"])
print("\nMarks as Series:\n", var1)

# ----------------------------
# DataFrame with multiple students
# ----------------------------
myds = {
    "name": ["Ashton", "Rohit", "Sanskar"],
    "div": ["S1", "S1", "S1"],
    "rollno": [27, 43, 55]
}
x = p.DataFrame(myds)
print("\nFull DataFrame:\n", x)

# ----------------------------
# Filtering DataFrame where rollno > 37
# ----------------------------
print("\nFiltered (rollno > 37):\n", x[x["rollno"] > 37])

# ----------------------------
# Series from dictionary, limited to selected keys
# ----------------------------
var1 = p.Series(myds, index=["name", "div"])
print("\nSeries from dict (partial keys):\n", var1)

# ----------------------------
# Displaying first 5 rows (head) and last 5 rows (tail)
# ----------------------------
print("\nFirst 5 rows (head):\n", x.head())
print("\nLast 5 rows (tail):\n", x.tail())
