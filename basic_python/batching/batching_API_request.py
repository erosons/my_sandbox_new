from itertools import islice
from time import sleep

REQS_PER_MINUTE = 100

class Request:
    def __init__(self, data):
        self.data = data

    def make_request(self):
        # Simulate making a request (this would be the actual API call)
        print(f"Making request with data: {self.data}")

def batched(iterable, batch_size):
    """
    Generate batches from an iterable.
    
    :param iterable: An iterable (e.g., list, generator).
    :param batch_size: Size of each batch.
    :return: Generator that yields batches of the given size.
    """
    iterator = iter(iterable)
    for first in iterator:
        batch = list(islice(iterator, batch_size - 1))
        batch.insert(0, first)
        yield batch

def process_requests_in_batches(all_requests):
    """
    Process requests in batches, respecting the rate limit of REQS_PER_MINUTE.
    
    :param all_requests: An iterable of Request objects.
    """
    for batched_requests in batched(all_requests, REQS_PER_MINUTE):
        for request in batched_requests:
            request.make_request()
        sleep(60)  # Sleep a minute to refresh API limits

# Example usage
if __name__ == "__main__":
    # Simulate a list of requests
    all_requests = [Request(data=i) for i in range(1, 301)]  # 300 requests

    # Process the requests in batches
    process_requests_in_batches(all_requests)
