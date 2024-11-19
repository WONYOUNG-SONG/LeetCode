class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = []
        for num in nums:
            if num in answer:
                answer.remove(num)
            else:
                answer.append(num)
                
        return answer[0]