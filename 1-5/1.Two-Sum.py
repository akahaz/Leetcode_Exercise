'''
Topic:
  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
  You may assume that each input would have exactly one solution, and you may not use the same element twice.
  You can return the answer in any order.
Example:
  Input: nums = [2,7,11,15], target = 9
  Output: [0,1]
'''
class Solution:
    def twoSum(self, nums, target):
        # Create a hashtable to store the complement of each number encountered
        hashtable = {}
        
        # Iterate through the list of numbers along with their indices
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            
            # Check if the complement exists in the hashtable
            if complement in hashtable:
                # If the complement is found, return the indices of the two numbers
                return hashtable[complement], i
            
            # Store the current number and its index in the hashtable
            hashtable[num] = i
        
        # If no pair of numbers is found that adds up to the target, return an empty list
        return []
