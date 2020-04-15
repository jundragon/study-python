# 탑
# https://programmers.co.kr/learn/courses/30/lessons/42588


if __name__ == '__main__':
    heights = [6, 9, 5, 7, 4]

    answer = [0 for _ in range(len(heights))]

    for idx, t in enumerate(heights):
        for i in range(idx, -1, -1):
            if heights[i] > heights[idx]:
                answer[idx] = i+1
                break

    print(answer)