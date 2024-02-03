class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        result = 0

        for op in operations:
            if '++' in op:
                result += 1
            elif '--' in op:
                result -= 1
            else:
                result = 0

        return result
        