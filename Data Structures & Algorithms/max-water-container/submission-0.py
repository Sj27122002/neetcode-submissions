class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(x,y):
            area = x*y
            return area
        def min(a,b):
            if a>b:
                return b
            elif a==b:
                return a
            else:
                return a
        i = 0
        j = len(heights) -1
        max_area = 0
        while i<j:
            q = j-i
            if max_area < area(q,min(heights[i],heights[j])):
                max_area = area(q,min(heights[i],heights[j]))
                if heights[i] > heights[j]:
                    j = j - 1
                else:
                    i = i + 1
            else:
                max_area = max_area
                if heights[i] > heights[j]:
                    j = j - 1
                else:
                    i = i + 1
        return max_area