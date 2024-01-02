class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        r,c = 0,0
        flipped = [[0]*len(image[0]) for i in range(len(image))]
        
        for i in range(len(image)):
            
            for j in range(len(image[0])-1, -1,-1):
                flipped[r][c] = 0 if image[i][j] == 1 else 1
                c+=1
            r += 1
            c = 0

        return flipped