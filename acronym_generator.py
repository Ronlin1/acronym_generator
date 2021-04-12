print('__------__WELCOME__------__')


# make a function definition
def acronym_gen():
    """
    This cli acronym generator takes input from the user and generates an acronym or initials
    :return: acronym --> String
    """
    # Get input from the user
    input_var = input("Enter word(s) for processing: ").strip(' ')
    final_acronym = []
    # Separating words if there is space
    if ' ' in input_var:
        acronym = input_var.split(' ')
        print(acronym)
        for word in acronym:
            # get the first letter of each word(upper) in  acronym & append it final
            first_letter = word[0].upper()
            final_acronym.append(first_letter)
        return f"I guess you could use {''.join(final_acronym)}"
    # If no space
    else:
        len_input = len(input_var)
        # if word is less that 3 characters
        if len_input <= 3:
            return f'I guess you could use {input_var[0].upper()}'
        # word greater than 3
        else:
            mid = len_input // 2
            final_acronym = input_var[0] + input_var[mid] + input_var[-1]
            return f'I guess you could use {final_acronym.upper()}'


# run
print(acronym_gen())

# Kindly let me know if you need any help or any questions regarding this app
# will apply tkinter in future for gui
