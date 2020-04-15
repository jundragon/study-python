if __name__ == '__main__':
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]

    time = 0
    bridge = list()
    bridge_time = list()

    while True:
        time += 1 # 한 루프당 1초씩 증가

        # 트럭이 다리를 건널 수 있는지 체크
        if truck_weights:
            if truck_weights[0] + sum(bridge) <= weight:
                bridge.append(truck_weights.pop(0))
                bridge_time.append(bridge_length)

        if not bridge:
            break

        # 다리를 건너는 트럭의 시간 갱신
        for i in range(len(bridge_time)):
            bridge_time[i] -= 1

        if bridge_time[0] <= 0:
            # 선두 트럭이 다리를 빠져 나왔다
            bridge_time.pop(0)
            bridge.pop(0)


    print(time)