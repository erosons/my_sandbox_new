
# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

#     A stone '#'
#     A stationary obstacle '*'
#     Empty '.'

# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

# Return an n x m matrix representing the box after the rotation described above

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        result = [['.'] * m for _ in range(n)]  # Transposed and empty result matrix
        
        for i in range(m):
            place_index = n - 1  # Start placing stones at the bottom of the new column
            for j in range(n - 1, -1, -1):  # Reverse iterate to simulate gravity
                if box[i][j] == '*':
                    result[j][m - 1 - i] = '*'
                    place_index = j - 1  # Reset the stone placement index below the obstacle
                elif box[i][j] == '#':
                    result[place_index][m - 1 - i] = '#'  # Place stone at the correct position
                    place_index -= 1  # Move up the placement index for the next stone
                # If it's '.', do nothing just decrease the place_index

        return result

# Example Usage
test = Solution()
print(test.rotateTheBox([["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]))


# There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.
# You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.
# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.
# Return the original array nums. If there are multiple solutions, return any of them.

from collections import defaultdict
from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Create a dictionary to store adjacency list
        graph = defaultdict(list)
        
        # Build the graph
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        # Find the start node (node with only one neighbor)
        start = None
        for key, value in graph.items():
            if len(value) == 1:
                start = key
                break
        
        # Use the start node to build the result array
        result = []
        current = start
        previous = None
        
        # Traverse the graph to reconstruct the array
        while current is not None:
            result.append(current)
            next_nodes = graph[current]
            # Set the next node considering not to revisit the previous node
            next_node = None
            for node in next_nodes:
                if node != previous:
                    next_node = node
                    break
            previous, current = current, next_node

        return result

# Example usage:
adjacentPairs1 = [[2,1],[3,4],[3,2]]
test = Solution()
print(test.restoreArray(adjacentPairs1))  # Output: [1, 2, 3, 4] or any valid permutation


# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def sum_divisors(n):
            total, count = 0, 0
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    if i * i == n:
                        total += i
                        count += 1
                    else:
                        total += i + n // i
                        count += 2
                    if count > 4:
                        return 0
            return total if count == 4 else 0

        total_sum = 0
        for num in nums:
            total_sum += sum_divisors(num)
        
        return total_sum

# Example usage:
solution = Solution()
nums1 = [21, 4, 7]
print(solution.sumFourDivisors(nums1))  # Expected output might be 32 for this input


# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.
# We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
# Return the reformatted license key.
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove dashes and convert to uppercase
        s = s.replace('-', '').upper()
        
        # List to hold the new formatted parts
        parts = []
        # Start from the end and capture groups of size k
        start = len(s)
        while start > 0:
            end = start
            start = max(0, start - k)  # Calculate the start position of the next group
            parts.append(s[start:end])  # Append the substring to the parts list
        
        # Reverse the parts to match the required order and join them with dashes
        return '-'.join(reversed(parts))

# Example usage:
solution = Solution()
print(solution.licenseKeyFormatting("5F3Z-2e-9-w", 4))  # Output: "5F3Z-2E9W"
print(solution.licenseKeyFormatting("2-5g-3-J", 2))    # Output: "2-5G-3J"


# Given an integer n, return the number of prime numbers that are strictly less than n.
import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0  # There are no primes less than 2
        
        # Boolean array of the truth value of indices as prime numbers
        is_prime = [True] * n
        is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime numbers
        
        # Sieve of Eratosthenes
        for start in range(2, int(math.sqrt(n)) + 1):
            if is_prime[start]:
                for multiple in range(start*start, n, start):
                    is_prime[multiple] = False
        
        # Count the number of primes found
        return sum(is_prime)

# Example usage:
solution = Solution()
print(solution.countPrimes(10))  # Output: 4, because there are four primes less than 10: 


# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = float('inf')  # Initialize min_price to a very high value
        max_profit = 0  # Initialize max_profit to 0
        
        for price in prices:
            if price < min_price:
                min_price = price  # Update the minimum price found so far
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update the maximum profit
        
        return max_profit

# Example usage:
solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5 (Buy on day 2 at price 1 and )



# Reverse Nodes in k-Group
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 1:
            return head
        
        # Dummy node to handle edge cases more easily
        dummy = ListNode(0)
        dummy.next = head
        current = head
        prev_end = dummy  # End of the previous block after reversal
        
        # Count the length of the list
        length = 0
        while current:
            length += 1
            current = current.next
            
        current = head
        while length >= k:
            # Initialize the pointers for reversing the k-group
            last_node_of_group = current
            next_node = None
            prev_node = None
            
            # Reverse k nodes
            for _ in range(k):
                next_node = current.next
                current.next = prev_node
                prev_node = current
                current = next_node
            
            # Connect the end of the previous group to the start of the reversed group
            prev_end.next = prev_node
            prev_end = last_node_of_group
            
            length -= k
        
        # Connect the last group which might not be enough to reverse
        prev_end.next = current
        
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Helper function to print linked list
def print_linked_list(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print(" -> ".join(map(str, values)))

# Example usage:
head = create_linked_list([1, 2, 3, 4, 5])
k = 2
solution = Solution()
result = solution.reverseKGroup(head, k)
print_linked_list(result)  # Output should show the list with groups of 2 reversed


# 12. Integer to Roman
# Seven different symbols represent Roman numerals with the following values:

class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping Roman numerals to their corresponding integer values
        value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        # Initialize the result as an empty string
        roman = ""
        
        # Loop over the value map
        for value, symbol in value_map:
            # Count how many times the Roman numeral can fit into num
            count = num // value
            if count:
                # Append the corresponding Roman numeral count times
                roman += symbol * count
                # Reduce num by the total value added to the Roman numeral string
                num -= value * count
        
        return roman

# Example usage:
solution = Solution()
print(solution.intToRoman(3749))  # Output: "MMMDCCXLIX"
