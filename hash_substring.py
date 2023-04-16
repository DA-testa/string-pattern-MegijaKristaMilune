# python3
# Megija Krista Miļūne, 221RDB229


def read_input():
    izvele = input()

    if 'I' in izvele:
        pattern = input().rstrip()
        string = input().rstrip() 
      

    elif 'F' in izvele:
        with open("tests/06","r") as file:
            pattern = file.readline().rstrip()
            string = file.readline().rstrip()

    else: 
        print('wrong input')

    
    return (pattern, string)


def print_occurrences(output):

    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):

    l_pattern= len(pattern)
    l_text= len(text)
    h_pattern = hash(pattern)
    h_window = hash(text[:l_pattern])


    result = []

    for i in range(l_text- l_pattern+ 1):
        if h_pattern == h_window:

            if pattern == text[i:i+l_pattern]:
                result.append(i)

        if i < l_text - l_pattern:
            h_window = hash(text[i+1:i+1+l_pattern])


    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))