# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

if __name__ == '__main__':
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    wardrobe = dict()
    for c in clothes:
        if c[1] in wardrobe.keys():
            wardrobe[c[1]].append(c[0])
        else:
            wardrobe[c[1]] = [c[0]]

    answer = 1
    for k, v in wardrobe.items():
        answer *= (len(v)+1)

    print(answer-1)