def findEvenNumbers(digits):
    def count_digits(lst):
        freq = [0] * 10
        for d in lst:
            freq[d] += 1
        return freq

    cnt = count_digits(digits)
    ans = []

    for x in range(100, 1000, 2):  # Only 3-digit even numbers
        y = x
        cnt1 = [0] * 10
        valid = True

        # Count digits of x
        while y:
            y, rem = divmod(y, 10)
            cnt1[rem] += 1

        # Check if x can be formed from input digits
        for i in range(10):
            if cnt1[i] > cnt[i]:
                valid = False
                break

        if valid:
            ans.append(x)

    return ans
print(findEvenNumbers([2,1,3,0]))