def solution(x):
    
    num_list = []   # 리스트 생성
    for i in str(x): # 숫자를 문자열로 변환하여 각 자릿수를 분리
        num_list.append(int(i)) # 리스트에 int형태로 변환하여 append
        
    if x % sum(num_list) ==0:  #리스트의 각 자릿수의 합과 x의 %연산이 0일경우 나누어 떨어지므로
        answer = True 
        
    else: # 나누어 떨어지지 않을때
        answer = False
    return answer