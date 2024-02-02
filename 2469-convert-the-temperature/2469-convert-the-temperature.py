class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """

        solution = []
        k = celsius + 273.15
        solution.append(float(k))
        f = celsius * 1.80 + 32.00
        solution.append(float(f))

        return solution
        