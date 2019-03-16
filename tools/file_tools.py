def get_text(path):
    file = open(path)
    lines = file.readlines()
    text = ""
    for line in lines:
        text += line.strip("\n")
    return text


def clean_text(raw_text):
    text_without_spaces = raw_text.replace(" ", "")
    lower_case = text_without_spaces.lower()
    return lower_case
