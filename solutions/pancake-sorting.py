class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:

        def flip(sublist, k):
            i = 0
            while i < k // 2:
                sublist[i], sublist[k-i-1] = sublist[k-i-1], sublist[i]
                i += 1

        ans = []
        num = len(A) #since the array size N and all elemets are unique(1-N) we can say N is in the array
        while num > 0:

            index = A.index(num) # locate the position of the current num
            
            # make two flipps to align num to desired position
            if index != num - 1:# if num is in correct index skip 

                if index != 0:#if num is alredy on the first posn skip
                    ans.append(index+1)
                    flip(A, index+1)
                # now that the value is at the head, flip it to the bottom
                ans.append(num)
                flip(A, num)

            # move on to the next round
            num -= 1

        return ans