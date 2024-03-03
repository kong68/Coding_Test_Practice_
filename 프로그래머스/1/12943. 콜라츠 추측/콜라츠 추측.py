def solution(num):
    answer = 0
    if num ==1: # 1이 입력되었을 때
        answer = 0
        return answer
    
    for i in range(1,502):
        
        if num ==1: #Collatz 추측이 완료되었을때
            answer = i # 반복된 횟수만큼 반환
            return answer - 1 # 마지막 1일때의 상태를 빼줌
        elif (i == 501) and (num != 1):
            answer = -1
            return answer
        elif num%2==0: #짝수일 경우
            num = num/2
        
        elif num%2!=0: #홀수일 경우
            num = (num*3)+1
        
    return answer