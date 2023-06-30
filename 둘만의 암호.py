def solution(s, skip, index):
    answer = ''
    arr = "abcdefghijklmnopqrstuvwxyz"          # 알파벳 문자열              
    arr = [x for x in arr if x not in skip]     # skip에 있는 문자 제외
    arr = ''.join(arr)                          # list의 값 문자열로 만들기
    
    for i in s:
        answer += arr[(arr.find(i) + index) % len(arr)]     # s의 위치 + index, z를 넘지 않게 arr의 길이로 나눈 몫 
        
    return answer