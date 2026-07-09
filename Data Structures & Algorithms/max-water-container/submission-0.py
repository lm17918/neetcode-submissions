class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best_a=0
        l,r=0,len(heights)-1
        while l<r:
            h=min(heights[l],heights[r])
            b= r-l
            print(f"given l,r {l},{r} i got b {b} h {h} and a {b*h}")
            if h*b>best_a:
                best_a=b*h
            else:
                if heights[l]<=heights[r]:
                    l+=1
                else:
                    r-=1
        return best_a


