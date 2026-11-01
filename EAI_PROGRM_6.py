# Pandas Series and DataFrame
import pandas as pd

scores = pd.Series([82, 94, 75, 89, 97],
                   index=["P", "Q", "R", "S", "T"])
print("--- Pandas Series ---")
print(scores)

student_data = {
    "RollNo": [201, 202, 203, 204, 205],
    "Name": ["Karthik", "Divya", "Meena", "Suresh", "Lavanya"],
    "Department": ["CSE", "CSE", "ECE", "CSE", "ECE"],
    "Mark": [82, 94, 75, 89, 97]
}
df = pd.DataFrame(student_data)

print("\n--- DataFrame ---")
print(df)
print("\nAverage Mark:", round(df["Mark"].mean(), 2))
print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])