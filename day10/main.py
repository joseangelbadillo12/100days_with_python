# Function with Outputs

def format_name(f_name, l_name):
    title_name = f_name.title()
    title_last_name = l_name.title()
    
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."