class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n+1):
            cnt = 0 
            q = i // 2
            r = i % 2
            if q == 1:
                cnt += 1
            while q >= 2:
                q = q // 2
                tmp = q % 2 
                if tmp == 1:
                    cnt += 1
            if r == 1:
                cnt += 1

            answer.append(cnt)


        return answer 