import re

def normalize_text(text):
    """
    Clean OCR text WITHOUT inventing digits
    """
    # Keep digits, + and spaces only
    text = re.sub(r"[^\d+\s]", " ", text)

    # Collapse multiple spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def extract_phone_numbers(text):
    """
    Extract ONLY valid Indian phone numbers
    """
    normalized = normalize_text(text)

    # Candidate patterns
    candidates = re.findall(r"(?:\+91\s*)?\d{10}", normalized)

    valid_numbers = []
    seen = set()

    for c in candidates:
        digits = re.sub(r"\D", "", c)

        # Remove country code
        if digits.startswith("91") and len(digits) == 12:
            digits = digits[2:]

        # Strong validation rules
        if (
            len(digits) == 10 and
            digits[0] in "6789" and
            not all(d == digits[0] for d in digits)
        ):
            if digits not in seen:
                seen.add(digits)
                valid_numbers.append(digits)

    return valid_numbers
