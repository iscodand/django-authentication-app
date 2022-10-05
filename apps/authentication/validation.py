def verify_empty_fields(field: str, field_name: str, error_list: dict) -> None:
    if not field.strip():
        error_list[field_name] = 'This field is required!'
