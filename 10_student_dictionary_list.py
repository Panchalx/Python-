students=[]
def get_detail():
    student_name=input("Enter a name:")
    student_age=int(input("Enter a age:"))
    if student_age <=0:
        print("please enter a real age")
    student_course=input("Enter a course:")
    return {"name":student_name,"age":student_age,"course":student_course}

student_count=int(input("how many students details do want to  add:"))
if student_count <= 0:
    print("Enter a postive number")
else:
    for position in range(1,student_count+1):
        record=get_detail()
        students.append(record)
        
    print("==== Student Database ======")
    for position,record in enumerate(students,start=1):
        print(f"Student   {position} ")
        print(f"Name:",record['name'])
        print(f"Age:",record['age'])
        print(f"Course:",record['course'])
                                