def solution(food):
    answer = ""
    for i in range(1, len(food)):  # 배열의 1번은 항상 물이기 때문에 2부터 시작

        if food[i] % 2 == 0:  # 음식이 짝수개 준비되어 있는가?
            for j in range(food[i] // 2):

                answer += str(i)
        elif food[i] % 2 != 0 and food[i] != 1:  # 음식이 홀수개 일경우
            for k in range((food[i]-1)//2):
                answer += str(i)
    answer = answer + "0"
    
    re_answer = answer[-len(answer):-1] # 0을 제외한 숫자 슬라이싱
    #print(re_answer)
    answer += re_answer[::-1]

                
    return answer
