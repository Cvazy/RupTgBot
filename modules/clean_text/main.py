import re


def clean_text(text):
    if isinstance(text, str):
        cleaned_text = text.replace('\n', ' ').strip()

        cleaned_text = re.sub(r'\b(\w+)\s+(\w{1,2})\b', r'\1\2', cleaned_text)

        return cleaned_text
    return text