import re
len_detection = re.compile(r'.{8,}')
upper_detection = re.compile(r'[A-Z]')
lower_detection = re.compile(r'[a-z]')
digit_detection = re.compile(r'\d')


def password_detection(password):
    """
    Detects whether password is strong based on 4 criteria
    """
    if len_detection.search(password) is None:
        return "Password is weak"
    if upper_detection.search(password) is None:
        return "Password is weak"
    if lower_detection.search(password) is None:
        return "Password is weak"
    if digit_detection.search(password) is None:
        return "Password is weak"
    return "Password is strong"

print(password_detection('testpw'))
print(password_detection('Testpw'))
print(password_detection('TESTPW'))
print(password_detection('TESTPW123'))
print(password_detection('Testpw123'))
print(password_detection('TESTPW123!@#'))
print(password_detection('Tb1@Tb1@'))
print(password_detection('TestPW123'))
print(password_detection('!@345ssfe@#23T4'))

