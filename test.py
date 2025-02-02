import re


def has_plus_sign(text):
    """
    Check if text contains a plus sign using regex

    Args:
        text (str): Text to check

    Returns:
        bool: True if plus sign is found, False otherwise
    """
    pattern = r'\+'  # The backslash escapes the plus sign since + is a special character in regex
    return bool(re.search(pattern, text))


# Test cases
def test_plus_sign_detection():
    test_cases = [
        "3000",  # No plus
        "+3000",  # Leading plus
        "3000+",  # Trailing plus
        "30+00",  # Middle plus
        "++3000",  # Multiple plus signs
        "3000.+50",  # Plus with decimal
        "abc+def"  # Plus in text
    ]

    for test in test_cases:
        result = has_plus_sign(test)
        print(f"Text: {test:10} Has plus: {result}")


if __name__ == "__main__":
    test_plus_sign_detection()
