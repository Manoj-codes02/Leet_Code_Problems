class Solution(object):
    def plusOne(self, digits):
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # All digits were 9, e.g., [9, 9, 9] → [1, 0, 0, 0]
        return [1] + digits
