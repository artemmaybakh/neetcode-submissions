class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        if strs:
            for el in strs:
                res += str(len(el)) + "#" + el
        else: 
            res = '[]'
        return res

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []

        result = []
        i = 0

        while i < len(s):
            # Находим длину слова
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # Переходим после #
            i = j + 1

            # Берём слово нужной длины
            word = s[i:i + length]
            result.append(word)

            # Переходим к следующему числу
            i += length

        return result