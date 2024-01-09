class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)
        
        ans = 0
        j = 0
        for i in range(len(processorTime)):
            for k in range(4):
                ans = max(ans, processorTime[i] + tasks[j+k])
            j += 4
        return ans