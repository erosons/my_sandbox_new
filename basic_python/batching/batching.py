from itertools import islice

def batched(iterable, batch_size):
    """
    Generate batches from an iterable.
    
    :param iterable: An iterable (e.g., list, generator).
    :param batch_size: Size of each batch.
    :return: Generator that yields batches of the given size.
    """
    iterator = iter(iterable)
    for first in iterator:  # Get the first item
        print(first)
        batch = list(islice(iterator, batch_size - 1))
        print(batch)
        batch.insert(0, first)  # Include the first item
        yield batch

# Example usage
data = range(1, 21)  # A range of numbers from 1 to 20
batch_size = 5

for batch in batched(data, batch_size):
    print(batch)