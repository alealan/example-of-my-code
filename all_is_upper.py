import re

def is_all_upper(text: str) -> bool:
    text_check = re.sub(r'[A-Z, ,0-9]', "",  text,)
    if len(text_check) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False