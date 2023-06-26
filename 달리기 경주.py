def solution(players, callings):
    dic = {name: rank for rank, name in enumerate(players)}     # (이름: 등수) 형식으로 딕셔너리 생성
    
    for name in callings:
        index = dic[name]               # 호명된 선수 등수
        dic[name] -= 1                  # 호명된 선수의 등수 - 1
        dic[players[index - 1]] += 1    # 호명된 선수 앞 선수의 등수 + 1
        players[index - 1], players[index] = players[index], players[index - 1]
                                        # 호명된 선수 <-> 호명된 선수 앞 선수         
    return players