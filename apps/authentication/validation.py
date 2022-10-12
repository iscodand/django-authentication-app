def verify_password(field_name: str, password1: str, password2: str, error_list: dict) -> None:
    if password1 != password2:
        error_list[field_name] = 'Passwords do not match!'
        
    if password1 or password2 == None:
        error_list[field_name] = 'Password lenght must be higher than 8 digits!'

    elif len(password1.strip()) < 8:
        error_list[field_name] = 'Password lenght must be higher than 8 digits!'