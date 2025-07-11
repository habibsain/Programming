class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x > 0):
            Y = []
            c = 0
            l = len(str(x))
            k = l - 1
            p = 0
            while(x > 0):
                r = x % 10
                Y.append(r)
                x = (x - r)/10
            for i in range(l):
                if(Y[i] == Y[l - 1 - i] ):
                    p = p + 0

                else:
                    p = p + 1

            if (p == 0):
                return bool(1)
            if (p != 0):
                return bool(0)

        elif(x == 0):
            return True
        elif(x < 0):
            return False
