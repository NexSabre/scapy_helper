from typing import List


def normalize(text: str) -> str:
    """Remove whitespaces and new line characters from text"""
    for char in (" ", "\n"):
        text = text.replace(char, "")
    return text


def normalize_and_split(text: str, split_char: str = "\n") -> List[str]:
    return text.replace(" ", "").split(split_char)
