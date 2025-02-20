from anki.collection import Collection
from difflib import ndiff
import sys

ANKI_COLLECTION_PATH = sys.argv[1]
MINIMAL_PAIRS_DECK_NAME = "French Minimal Pairs"

def gather_diff(a, b):
    a_diff = ''
    b_diff = ''
    last_op = ''
    last_c = ''
    for i, diff in enumerate(ndiff(a, b)):
        op = diff[0]
        c = diff[2]
        if c == '̃' and op in '-+':
            if last_op not in '-+':
                a_diff += last_c
                b_diff += last_c
        if op == '-':
            a_diff += c
        elif op == '+':
            b_diff += c
        last_op = op
        last_c = c
    return ''.join(sorted((a_diff,b_diff)))

col = Collection(ANKI_COLLECTION_PATH)
print(col)
notes = [col.get_note(n) for n in col.find_notes(f'deck:"{MINIMAL_PAIRS_DECK_NAME}"')]
for n in notes:
    n['IPA Pair'] = gather_diff(n.values()[2], n.values()[5])

col.update_notes(notes)
