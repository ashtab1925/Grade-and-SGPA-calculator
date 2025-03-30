# Function to calculate total and average marks
def cal_average_total(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

# Function to determine grade based on average marks
def determine_grade(average):
    if average >= 90:
        return "O"
    elif average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "B+"
    elif average >= 50:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"
def grade_to_grade_point(grade):
    grade_points = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5, "F": 0}
    return grade_points.get(grade, 0) 
# Function to calculate SGPA 
def cal_sgpa(subjects):
    total_grade_points = 0 
    total_credits = 0 

    for marks, credits in subjects:
        grade = determine_grade(marks)  # Get letter grade
        grade_point = grade_to_grade_point(grade)  # Convert to numerical grade point
        total_grade_points += grade_point * credits
        total_credits += credits

    sgpa = total_grade_points / total_credits if total_credits > 0 else 0
    return sgpa








def main ():
    num_students = int(input("Enter the number of students : "))
    for x in range(num_students):
        name = input("Enter you name : ")
        num_of_subs = int(input("Enter number of subjects in your semester : "))
        
        subjects = []
        marks = []
        for y in range(num_of_subs):
            mark = int(input(f"Enter marks for subject {y+1} : "))
            credits = int(input(f"Enter credits for subject {y+1} : "))
            subjects.append((mark,credits))
            marks.append(mark)

        total , average = cal_average_total(marks)
        grade = determine_grade(average)
        Sgpa = cal_sgpa(subjects)

        print("\n----- Student Report -----")
        print(f"Name: {name}")
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")
        print(f"Grade: {grade}")
        print(f"SGPA : {Sgpa: .2f}")
        print("-------------------------")


main ()
