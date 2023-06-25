def solution(babbling):
    answer = 0
    str = ["aya", "ye", "woo", "ma"]        # 발음 가능 단어
    arr = ["/", "//", "///", "////"]        # /로 변경된 단어
    
    for word in babbling:
        for c in str:   
            word = word.replace(c, '/')     # 입력된 단어에 str 속 단어를 / 로 변경
        if word in arr:             
            answer += 1                     # 변경된 단어가 arr에 있으면 answer++
            
    return answer