class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        opreations = []
        for op in logs:
            if op == '../':
                if len(opreations) > 0:
                    opreations.pop()
            elif op == './':
                continue
            else:
                opreations.append(op)

        return len(opreations)