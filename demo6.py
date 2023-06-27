class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        n = len(s)  # 单词数量
        arr = ["" for _ in range(n)]  # 单词数组
        for wd in s:
            # 计算位置索引对应的单词数组下标，并将单词放入对应位置
            # 数组下标为 0 开头，位置索引为 1 开头
            arr[int(wd[-1]) - 1] = wd[:-1]
        return " ".join(arr)


so = Solution()
s = "is2 sentence4 This1 a3"
print(so.sortSentence(s))
