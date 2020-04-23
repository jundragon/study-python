# 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165


def dfs(arr, idx):
    global answer

    if idx == len(arr):
        if sum(arr) == target:
            answer += 1
    else:
        arr[idx] *= 1
        dfs(arr, idx+1)
        arr[idx] *= -1
        dfs(arr, idx+1)


if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3

    answer = 0
    dfs(numbers, 0)

    print(answer)
