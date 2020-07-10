class Solution:
    def permuteUnique(self, num):
        res = []
        if len(num) == 0:
            return res
        self.permute(res, num, 0)
        return res

    def permute(self, res, num, index):
        if index == len(num):
            res.append(list(num))
            return
        appeared = set()
        for i in range(index, len(num)):
            if num[i] in appeared:
                continue
            appeared.add(num[i])
            num[i], num[index] = num[index], num[i]
            self.permute(res, num, index + 1)
            num[i], num[index] = num[index], num[i]