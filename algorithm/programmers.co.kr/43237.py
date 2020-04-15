# 예산
# https://programmers.co.kr/learn/courses/30/lessons/43237

if __name__ == '__main__':
    budgets, M = [120, 110, 140, 150], 485
    budgets.sort()
    answer = M // len(budgets) # 임시 상한

    for idx, b in enumerate(budgets):
        if b <= answer:
            M -= b # 예산 집행
            continue

        answer = M // len(budgets[idx:])
        if b <= answer:
            M -= b # 재 배정된 예산 집행
        else:
            break

    print(answer)

