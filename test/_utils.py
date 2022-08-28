def normalize(text: str) -> str:
    """Remove whitespaces and new line characters from text"""
    for char in (" ", "\n"):
        text = text.replace(char, "")
    return text
