import re
def extract_errors(logs: str):
errors = []
for line in logs.split("\n"):
if re.search(r"ERROR|Exception|CRITICAL", line):
errors.append(line)
return errors
