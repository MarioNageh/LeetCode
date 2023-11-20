def clamp(power, type = 0, max_corner = 1000):
    """
    By Default We get MinValue
    type = 1 Get Max Value
    """
    min_value = min(1 * power, 5 * power)
    max_value = max(1 * power , 5 * power)

    if max_value > max_corner:
        max_value = max_corner
    return min_value if type == 0 else max_value




class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {
            1 : 'I',
            5 : 'V',
            10 : 'X',
            50 : 'L',
            100 : 'C',
            500 : 'D',
            1000 : 'M'
        }
        # 1943
        current_power = 1
        res = []
        while num > 0:
            d = num % 10
            min_sim = dic[clamp(current_power)]
            max_sim = dic[clamp(current_power,type = 1)]
            if d < 4:
                res.append(min_sim * d)

            elif d >= 5 and  d < 9:
                res.append(min_sim * (d - 5))
                res.append(max_sim)

            elif d == 4:
                res.append(max_sim)
                res.append(min_sim)

            elif d == 9:
                max_sim = dic[clamp(current_power * 10)]
                res.append(max_sim)
                res.append(min_sim)

            current_power *= 10
            num = num // 10
        return ''.join(res[::-1])
