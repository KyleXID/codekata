# Day17.Week4(day3) 단어의 input이 주어졌을 때 같은 알파벳으로 이루어진 단어끼리 묶어주는 함수입니다.

def groupAnagrams(strs):
    d = {}

    for w in sorted(strs):
        key = tuple(sorted(w))
        d[key] = d.get(key, []) + [w]
    return d.values()

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
