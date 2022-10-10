def verify_empty_fields(field: str, field_name: str, error_list: dict) -> None:
    if not field.strip():
        error_list[field_name] = f'Field {field_name.capitalize()} is required!'
        
def verify_password(field_name, password1, password2, error_list) -> None:
    if password1 != password2:
        error_list[field_name] = 'Passwords do not match!'

    if len(password1.strip()) < 8:
        error_list[field_name] = 'Password lenght must be higher than 8 digits!'
        