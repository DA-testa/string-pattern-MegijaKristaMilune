# python3
# Megija Krista Miļūne, 221RDB229

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    izvele = input().rstrip().lower()
    if izvele == "i":

        pattern = input().rstrip()
        text = input().rstrip()
    else:
        with open(input().rstrip()) as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
            
    return pattern, text

    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(" ".join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    p = 31
    m = 10**9 + 9

    n = len(text)
    m_pattern = len(pattern)
    p_power = pow(p, m_pattern, m)

    pattern_hash = 0
    text_hash = 0


    for i in range(m_pattern):
        pattern_hash = (pattern_hash * p + ord(pattern[i])) % m
        text_hash = (text_hash * p + ord(text[i])) % m

    occurrences = []

    for i in range(n - m_pattern + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+m_pattern]:
                occurrences.append(i)

        if i < n - m_pattern:
            text_hash = ((text_hash - ord(text[i]) * p_power) * p + ord(text[i+m_pattern])) % m


    # and return an iterable variable
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
