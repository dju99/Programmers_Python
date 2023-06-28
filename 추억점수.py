def solution(names, yearnings, photos):
    answer = []
    score = 0
    
    dic = {name: yearning for name, yearning in zip(names, yearnings)}      # 이름:점수 형태로 저장

    for i in photos:                
        for j in i:
            if j in dic:            # 해당 원소가 dic에 있으면
                score += dic[j]     # score에 value값 더하기
        answer.append(score)
        score = 0
    
    return answer