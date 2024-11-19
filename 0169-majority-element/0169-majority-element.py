class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = dict()
        for num in nums:
            answer[num] = answer.get(num, 0) + 1
        
        return max(answer, key = lambda k: answer[k])