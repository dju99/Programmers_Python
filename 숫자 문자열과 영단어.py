def solution(s):
    answer = 0
    
    dic = {             # 알파벳: 숫자 형태 딕셔너리 생성
        'zero':0,
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
    }
    
    for alp in dic:
        if alp in s:
            s = s.replace(alp, str(dic[alp]))   # s에 알파벳을 숫자로 변경
    
    answer = int(s)

    return answer