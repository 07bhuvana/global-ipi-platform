import re

# Test the UUID pattern
test_string = 'API_KEY:12345678-48C0-1234-EF0F-567890ABCDEF'

uuid_pattern = r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'

matches = re.finditer(uuid_pattern, test_string)

for match in matches:
    print(f"Found: {match.group(0)}")
    print(f"Position: {match.start()} to {match.end()}")

# Test context check
line = test_string.lower()
keywords = ["api", "key", "token", "secret"]

has_context = any(keyword in line for keyword in keywords)
print(f"\nHas context: {has_context}")
