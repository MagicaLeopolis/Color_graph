
# def backtrack(current: list, start: int, nums: list[int]) -> list:
#     nums.sort()
#     result.append(list(current))
#     for i in range(start, len(nums)):
#         if i > start and nums[i] == nums[i-1]:
#             continue
#         current.append(nums[i])
#         backtrack(current, i+1, nums)
#         current.pop()

# nums = [1,2,2]
# result = []
# nums.sort()
# backtrack([], 0, nums)
# print(result)


def backtrack_color(start: int, dic: dict, colors: list) -> dict:
    keys = list(dic.keys())
    if start == len(dic):
        return True
    our_point = keys[start]

    for color in colors:
        mist = False
        for element in dic[our_point]:
            if element in correct_color and correct_color[element] == color:
                mist = True
                break
        if mist:
            continue

        correct_color[our_point] = color

        if backtrack_color(start + 1, dic, colors):
            return correct_color
        del correct_color[our_point]

    print(f'You can not colored this dot: {our_point}')


    backtrack_color(start + 1, dic, colors)


correct_color = {}
dic = read_file('graph.csv')
start = 0
colors = ['red', 'green', 'blue']

print(backtrack_color(0, {'a': ['b', 'e'], 'b': ['a', 'd', 'c'], 'e': ['a', 'c', 'd'], 'd': ['b', 'c', 'e'], 'c': ['b', 'e', 'd']} , ['red', 'green', 'blue']))
