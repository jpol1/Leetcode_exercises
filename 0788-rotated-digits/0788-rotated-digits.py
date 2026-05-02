class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        must_have = {2,5,6,9}
        cannot_have = {3,4,7}

        res = 0

        for i in range(n+1):
            tmp_flag = False
            while(i > 0):
                if ((i % 10) in must_have):
                    tmp_flag = True
                elif ((i%10) in cannot_have):
                    tmp_flag = False
                    break
                i //= 10
            if (tmp_flag):
                res += 1
        
        return res
        