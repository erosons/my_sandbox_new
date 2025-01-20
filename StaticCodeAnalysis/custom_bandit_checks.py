# custom_bandit_checks.py
import bandit
import re

@bandit.test_id('B998')
def check_for_ssn(context):
    # Define a simple pattern to match a potential SSN
    ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
    
    # Check each line in the code for the SSN pattern
    for line_number, line in enumerate(context.get_code().split('\n'), start=1):
        if re.search(ssn_pattern, line):
            return bandit.Issue(
                severity=bandit.HIGH,
                confidence=bandit.HIGH,
                text="Potential SSN pattern found on line {}".format(line_number)
            )
