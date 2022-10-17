def verify_password(field_name: str, password1: str, password2: str, error_list: dict) -> None:
    if password1 and password2 is not None:
        if password1 != password2:
            error_list[field_name] = 'Passwords do not match!'

        elif len(password1) < 8:
            error_list[field_name] = 'Password lenght must be higher than 8 digits!'
