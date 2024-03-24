class Solution:
    def to_reverse_numbers(self, l1, l2):
        l1_reversed_number = ""
        l2_reversed_number = ""

        i = len(l1) - 1
        i2 = len(l2) - 1

        while i >= 0:
            l1_reversed_number += str(l1[i])
            i -= 1

        while i2 >= 0:
            l2_reversed_number += str(l2[i2])
            i2 -= 1

        return [int(l1_reversed_number), int(l2_reversed_number)]

    def addition_of_numbers(self, rev_fun):
        added_sum = 0

        for i in rev_fun:
            added_sum += i

        result_arr = []
        reversed_sum = lambda added_sum: [int(digit) for digit in str(added_sum)][::-1]

        result_arr.extend(reversed_sum(added_sum))

        return result_arr


solution_instance = Solution()
result = solution_instance.to_reverse_numbers([1, 2, 3], [4, 5, 6])
print(solution_instance.addition_of_numbers(result))