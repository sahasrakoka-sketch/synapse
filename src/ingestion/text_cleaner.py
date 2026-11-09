
import re


def clean_text(text: str) -> str:
    """
    Clean extracted PDF text while preserving paragraph breaks.
    """

    # Remove unwanted soft hyphen characters
    text = text.replace("\u00ad", "")

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove extra spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Remove spaces around line breaks
    text = re.sub(r" *\n *", "\n", text)

    # Replace excessive blank lines with one blank line
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()
