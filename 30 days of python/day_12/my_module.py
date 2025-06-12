def generate_full_name(f_name, l_name):
    return f_name.title() + " " + l_name.title()

def person(
    f_name = "mohammed", 
    l_name = "ahmed", 
    nationality = "ethiopian",
    dob = 2002,
    is_married = True
):
    
    person = {
        "first_name": f_name,
        "last_name": l_name,
        "nationality": nationality,
        "date_of_birth": dob,
        "is_married": is_married
    }
        
    return person

