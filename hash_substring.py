# python3
# Megija Krista Miļūne, 221RDB229


def read_input():
    input_method = input()

    if 'I' in input_method:
        pattern = input().rstrip()
        string = input().rstrip()       

    elif 'F' in input_method:
        with open("tests/06","r") as file:
            pattern = file.readline().rstrip()
            string = file.readline().rstrip()
    else: 
        print('wrong input')
    
    return (pattern, string)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = hash(pattern)
    window_hash = hash(text[:pattern_len])
    result = []
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == window_hash:
            if pattern == text[i:i+pattern_len]:
                result.append(i)
        if i < text_len - pattern_len:
            window_hash = (window_hash - ord(text[i])*pow(26,pattern_len-1)) * 26 + ord(text[i+pattern_len])
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
