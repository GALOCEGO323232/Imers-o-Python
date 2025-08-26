def format_names(name : dict[str, str]) -> dict[str]:
    namess = []
    for name, lastname in name.items():
        names = f"{name.capitalize()} {lastname.capitalize()}"
        namess.append(names)
    return namess