from random import sample

# 컴퓨터가 3자리 숫자를 문제로 내도록.

# 1~9로만 사용
# 중복된 숫자 허용 X


cpu_numbers = sample(range(1,10), 3)

print(cpu_numbers)

# 사람이 3자리 숫자를 입력
while True :
# 숫자 3개를 저장할 공간
    user_numbers = list()
    # 사람이 3자리 숫자를 입력 => 맞출때 까지 계속 입력

    # 3자리 숫자를 입력 하면 => 3칸의 목록으로 분리
    input_number = int(input('3자리 숫자를 입력 : '))

    # ex. 123 => [1,2,3] 으로 분리.
    # 3자리 정수가 들어왔다고 전제하자.

    # 제일 먼저 추가 : 100의 자리
    # 그 다음 : 10의 자리
    # 그 다음 : 1의 자리

    user_numbers.append( input_number//100 ) # 100의 자리
    user_numbers.append( input_number//10 % 10 ) #10의 자리
    user_numbers.append( input_number%10 ) #1의 자리

    print(user_numbers)

    # ?S ?B인지 판단 => 힌트 제공

    s_count = 0
    b_count = 0

    # 문제 숫자/ 내 숫자 비교 => S/B 갯수 파악
    

    # 3S가 되었다면? => 정답 맞춤! => 게임 종료
