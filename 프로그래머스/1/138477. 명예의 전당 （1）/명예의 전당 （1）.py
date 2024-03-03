def solution(k, score):
    answer = [] # 발표 점수
    win_score = []  # 명예의 전당
    
    for i in range(len(score)): # 출연한 가수들의 점수의 길이만큼 반복
        
        if(i < k): # 명예의 전당의 점수들이 k보다 적을 때
            win_score.append(score[i]) 
            win_score.sort(reverse=True) # 내림차순 정렬

            answer.append(win_score[len(win_score)-1]) # 가장 작은 값
            
        else: # 명예의 전당의 점수들이 k보다 클 때
            win_score.sort(reverse=True)  # 내림차순 정렬
            if win_score[len(win_score)-1] < score[i]: # 명예의 전당 가장 작은 값보다 들어오는 값이 더 클 때
                win_score.pop() # 가장 작은 값 pop
                win_score.append(score[i]) # 새로운값 명예의 전당에 올리기
                win_score.sort(reverse=True) # 내림차순 정렬
                answer.append(win_score[len(win_score)-1]) # 가장 작은값 answer에 넣기
            else: # 명예의 전당 가장 작은 값보다 들어오는 값이 더 작을 때
                win_score.sort(reverse=True) # 내림차순 정렬
                answer.append(win_score[len(win_score)-1]) # 명예의 전당 점수들중 가장 작은 것을 answer에 넣기


    return answer

