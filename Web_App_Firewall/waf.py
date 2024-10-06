import re

# SQL injection patterns
SQL_INJECTION_PATTERNS = [
    r"(?i)select.*from",
    r"(?i)union.*select",
    r"(?i)insert.*into",
    r"(?i)drop\s+table",
    r"(?i)or\s+1=1",
]

# XSS patterns
XSS_PATTERNS = [
    r"(?i)<script.*?>.*?</script.*?>",
    r"(?i)<.*?on.*?=.*?>",
    r"(?i)alert\(.*?\)",
]

def check_request_for_attacks(user_input):
    # Check for SQL injection
    for pattern in SQL_INJECTION_PATTERNS:
        if re.search(pattern, user_input):
            return "SQL Injection"

    # Check for XSS
    for pattern in XSS_PATTERNS:
        if re.search(pattern, user_input):
            return "XSS"

    return None  # No attack detected
