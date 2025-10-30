class Solution:
    def largestTriangleArea(self, p: list[list[int]]) -> float:
        n=len(p)
        ans=0.0
        for i in range(n-2):
            x1,y1=p[i]
            for j in range(i+1,n-1):
                x2,y2=p[j]
                for k in range(j+1,n):
                    x3,y3=p[k]
                    area=0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
                    ans=max(ans,area)
        return ans