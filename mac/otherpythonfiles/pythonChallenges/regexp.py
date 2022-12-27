import re

def multi_re_find(patt,phs):
    for p in patt:
        print(f"Searching for pattern {p}")
        print(re.findall(p,phs))
        print("\n")

test_phrase = 'This is str! But it has punctuation. how to remove?'

test_patterns = ['[A-Z]+']

multi_re_find(test_patterns,test_phrase)