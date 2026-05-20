class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C = [0]*len(A)
        occurrences = {}
        common = 0

        for i in range(len(A)):
            if A[i] not in occurrences:
                occurrences[A[i]] = 1
            else:
                common += 1
            
            if B[i] not in occurrences:
                occurrences[B[i]] = 1
            else:
                common += 1

            C[i] = common
        return C