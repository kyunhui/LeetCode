class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n+1):
            cnt = 0 
            q = i // 2
            r = i % 2

            if q == 1:
                cnt += 1
            if r == 1:
                cnt += 1

            while q >= 2:
                tmp = q
                q = tmp // 2
                r = tmp % 2 
                
                if r == 1:
                    cnt += 1
                if q == 1:
                    cnt += 1
                    
                    
            answer.append(cnt)


        return answer 