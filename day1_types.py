# 两个 int 相加；
def add(a: int, b: int) -> int:
    return a + b

# str 首字母大写（查查 str 有没有现成方法）；
def capitalize_first_letter(s: str) -> str:
    return s.capitalize()

# list[int] 求最大（不许用 max，自己循环）；
def find_max(lst: list[int]) -> int:
    if not lst:
        raise ValueError("List is empty")
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

# dict[str, int] 求所有值的和；
def sum_dict_values(d: dict[str, int]) -> int:
    return sum(d.values())

# 返回 int | None（找得到返回下标，找不到返回 None），测两种情况。
def find_index(lst: list[int], target: int) -> int | None:
    for i, num in enumerate(lst):
        if num == target:
            return i
    return None
if __name__ == "__main__":
    # 测试 add 函数
    print(add(3, 5))  # 输出: 8

    # 测试 capitalize_first_letter 函数
    print(capitalize_first_letter("hello"))  # 输出: Hello

    # 测试 find_max 函数
    print(find_max([1, 3, 2, 5, 4]))  # 输出: 5

    # 测试 sum_dict_values 函数
    print(sum_dict_values({"a": 1, "b": 2, "c": 3}))  # 输出: 6

    # 测试 find_index 函数
    print(find_index([10, 20, 30], 20))  # 输出: 1
    print(find_index([10, 20, 30], 40))  # 输出: None

# 词频统计：给一段英文文本，统计每个单词出现几次。提示：text.split() 得到单词列表 → 用字典累加，键不存在时用 d.get(word, 0) 兜底；
def word_frequency(text: str) -> dict[str, int]:
    words = text.split()
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