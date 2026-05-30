name = "Shreesh"
age = 13
isStudent = True
print(f"Name: {name}, Age: {age}, Is Student: {isStudent}\n")
# Typecasting
age_str = str(age)
print(f"Age as string: {age_str}, Type: {type(age_str)}\n")
isStudent_str = str(isStudent)
print(f"Is Student as string: {isStudent_str}, Type: {type(isStudent_str)}\n")
# Converting back to original types 
age_int = int(age_str)
print(f"Age as integer: {age_int}, Type: {type(age_int)}\n")
isStudent_bool = isStudent_str == "True"
print(f"Is Student as boolean: {isStudent_bool}, Type: {type(isStudent_bool)}\n") 
