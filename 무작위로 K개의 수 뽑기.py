def solution(arr, k):
    answer = []
    
    for num in arr:
        if num not in answer:       # num이 answer에 없다면
            answer.append(num)      # 추가
        if len(answer) == k:        # answer의 길이가 K가 되면 멈춤
            break
            
    if len(answer) < k:                         # answer의 길이가 K 보다 작으면
        for i in range(0, k - len(answer)):     # 남은 공간에 -1 추가
            answer.append(-1)
    
    return answer