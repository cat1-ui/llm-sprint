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
