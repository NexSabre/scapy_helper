def normalize(text):
    """
    Remove whitespaces and new line characters from text
    :param text: String
    :return: String
    """
    for char in (" ", "\n"):
        text = text.replace(char, "")
    return text
