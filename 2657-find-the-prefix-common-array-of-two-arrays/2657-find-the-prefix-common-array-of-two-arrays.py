class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = []
        seen = set()
        common = 0

        for i in range(len(A)):
            if A[i] in seen:
                common += 1
            else:
                seen.add(A[i])
            
            if B[i] in seen:
                common += 1
            else:
                seen.add(B[i])

            C.append(common)
        return C