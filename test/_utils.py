from typing import List


def normalize(text: str, lowercase: bool = False) -> str:
    """Remove whitespaces and new line characters from text"""
    for char in (" ", "\n"):
        text = text.replace(char, "")
    if lowercase:
        text = text.lower()
    return text


def normalize_and_split(text: str, split_char: str = "\n") -> List[str]:
    return text.replace(" ", "").split(split_char)
