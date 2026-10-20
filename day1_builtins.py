# 词频统计：给一段英文文本，统计每个单词出现几次。提示：text.split() 得到单词列表 → 用字典累加，键不存在时用 d.get(word, 0) 兜底；
def word_frequency(text: str) -> dict[str, int]:
   words = [w.lower() for w in text.split()]

   frequency = {}
   for word in words:
        frequency[word] = frequency.get(word, 0) + 1
   return frequency
# 字典合并：d1 = {"a": 1, "b": 2}，d2 = {"b": 3, "c": 4}，合并成 {"a": 1, "b": 5, "c": 4}（同键相加）。提示：遍历 + get(key, 0)；
def merge_dicts(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    merged = d1.copy()  # 先复制 d1
    for key, value in d2.items():
        merged[key] = merged.get(key, 0) + value  # 同键相加
    return merged
# 按值倒序：把上面合并后的字典按值从大到小输出。提示：sorted(d.items(), key=lambda x: x[1], reverse=True)——lambda 你先照着用，机制的我们下个阶段细讲。
def sort_dict_by_value(d: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(d.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    text = "the cat and the dog and the bird"
    print(word_frequency(text))

    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    merged = merge_dicts(d1, d2)
    print(merged)

    print(sort_dict_by_value(merged))
    print(list(zip(merged.keys(), merged.values())))

