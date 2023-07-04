def solution(phone_number):
    answer = ''
    answer = answer.rjust(len(phone_number) - 4, '*') + phone_number[-4:]
    # phone_number - 4 만큼 * 채우기 + 뒤에서 4번째 숫자 
    
    return answer