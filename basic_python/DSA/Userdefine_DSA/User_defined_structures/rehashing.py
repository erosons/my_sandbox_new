#Question 20.

def insert(table, key):
    hash_val = key % 20
    if table[hash_val] is None or len(table[hash_val]) == 0:
        table[hash_val] = [key]
    else:
        print(f'key numeber',key)
        rehash_val = (key + 3) % 20
        print(rehash_val)
        while table[rehash_val] is not None and len(table[rehash_val]) > 0:
            rehash_val = (rehash_val + 3) % 20
            #print(rehash_val)
        table[rehash_val] = [key]

keys = [66, 47, 87, 90, 126, 140, 145, 153, 177, 285, 393, 395, 467, 566, 620, 735]
table = [None] * 20

for key in keys:
    insert(table, key)

print(table)