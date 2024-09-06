# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
     # 시간을 분으로 변환하는 함수
    def time_to_minutes(time):
        h, m = map(int, time.split(':'))
        return h * 60 + m

    # plans를 시작 시간 순으로 정렬하고 시간을 분으로 변환
    new_plans = []
    for name, start, duration in plans:
        minutes = time_to_minutes(start)
        new_plans.append((name, minutes, int(duration)))

    new_plans = sorted(new_plans, key=lambda x: x[1])
    
    stack = []  # 진행 중인 과제를 저장할 스택
    answer = []  # 완료된 과제를 저장할 리스트
    current_time = 0

    for name, start, duration in new_plans:
        # 현재 시간부터 다음 과제 시작 시간까지 진행 중인 과제 처리
        while stack and current_time + stack[-1][1] <= start:
            ongoing_name, ongoing_duration = stack.pop()
            current_time += ongoing_duration
            answer.append(ongoing_name)

        # 진행 중인 과제가 있고, 아직 다음 과제 시작 시간이 되지 않았다면
        if stack and current_time < start:
            stack[-1] = (stack[-1][0], stack[-1][1] - (start - current_time))

        # 새로운 과제 시작
        stack.append((name, duration))
        current_time = start

    # 남은 과제들 처리
    while stack:
        answer.append(stack.pop()[0])

    return answer