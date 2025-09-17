def calculate_average(students):
    averages = {}
    for name, marks in students.items():
        total = 0
        for m in marks:
            total += m
        avg = total / len(marks)
        averages[name] = round(avg,2)
    return averages

def top_performer(averages):
    top_student = max(averages, key=averages.get)
    return top_student

students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

averages = calculate_average(students)
print("Average Marks:", averages)

top_student = top_performer(averages)
print("Top Performer:", top_student)
