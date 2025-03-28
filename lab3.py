"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Learn how to identify and fix thr three types of errors
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# The program below should analyse a list of grades and print out some information.
# However, it does not yet work. There are seven errors in total to find and fix.

grades = [80, 95, 78, 92, 85, 90]
print(f"Starting grade analysis {grades}")


def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average
# Runtime Error 2: TypeError in string concatenation
average_grade = calculate_average(grades)
print(f"Average Grade: {average_grade}" )

# Final print statement
print("Grade analysis complete.")


if average_grade < 50:
    print("Average grade is failing.")
else:
    print("Average grade is passing.")

grades.sort()
print("Highest Grade:", grades[len(grades) - 1])

