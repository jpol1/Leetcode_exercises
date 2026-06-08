class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        j = 0
        arr_less = []
        arr_eq = []
        arr_greater = []
        for num in nums:
            if num < pivot:
                arr_less.append(num)
            elif num == pivot:
                arr_eq.append(num)
            else:
                arr_greater.append(num)
        res = arr_less + arr_eq + arr_greater
        return res