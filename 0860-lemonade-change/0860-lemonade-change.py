class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f,t,tw = 0,0,0

        for i in bills:
            if i == 5:
                f+=1
            elif i == 10:
                t+=1
                if f>0:
                    f-=1
                else:
                    return False
            else:
                tw+=1
                if f and t:
                    f-=1
                    t-=1
                elif f > 2:
                    f-=3
                else:
                    return False
        return True