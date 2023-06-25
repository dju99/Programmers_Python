def solution(dots):
    w = max(dots)[0] - min(dots)[0]     # 길이 = x의 최댓값 - x의 최솟값
    h = max(dots)[1] - min(dots)[1]     # 높이 = y의 최댓값 - y의 최솟값
    
    answer = w * h
    
    return answer