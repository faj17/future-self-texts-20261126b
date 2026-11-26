"""Write one funny text from your future self to /output/entry.txt."""

SETUP = "Future you. That unread email from your dentist? I just paid $4,200 for the tooth."
PUNCH = "Open the email. Open it now."


def assemble():
    return SETUP + " " + PUNCH


def validate(text):
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def main():
    line = validate(assemble())
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
