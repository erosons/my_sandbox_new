from itertools import batched

for batch in batched("Hello, world!", 3):    print(batch)
# Output
# ('H', 'e', 'l')
# ('l', 'o', ',')
# (' ', 'w', 'o')
# ('r', 'l', 'd')
# ('!',)