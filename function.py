
def format_name(fname, lname):
    formated_fname = fname.title()
    formated_lname = lname.title()
    return f"{formated_fname} {formated_lname}"


formated_fullname = format_name(fname="HITANSHU", lname="verma")
print(formated_fullname)



def format_name(fname, lname):
    # if fname or lname is null then return rest of the code will not execute
    if fname =="" or lname == "":  
        return
    formated_fname = fname.title()
    formated_lname = lname.title()
    return f"{formated_fname} {formated_lname}"


formated_fullname = format_name(fname=input("what is your fname? \n"), lname=input("what is your lname? \n"))
print(formated_fullname)