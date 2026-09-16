student_info={}
student_name=input("Enter a name:")
student_age=int(input("Enter a age:"))
student_course=input("Enter a course:")
student_info.update({"name":student_name,"age":student_age,"Course":student_course})
print("===== Student Details ======")
for key_detail,value_details in student_info.items():
    print(f"{key_detail}   : {value_details}")
    