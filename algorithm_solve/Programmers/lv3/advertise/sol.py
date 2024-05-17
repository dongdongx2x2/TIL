def time_to_sec(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def sec_to_time(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h:02}:{m:02}:{s:02}"

def solution(play_time, adv_time, logs):
    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)
    
    total_time = [0] * (play_time_sec + 1)
    
    for log in logs:
        start, end = log.split('-')
        start_sec = time_to_sec(start)
        end_sec = time_to_sec(end)
        total_time[start_sec] += 1
        total_time[end_sec] -= 1
        
    # 시청자 수 누적 합
    for i in range(1, len(total_time)):
        total_time[i] += total_time[i - 1]
    
    # 누적 시청 시간 계산을 위해 다시 한 번 누적 합
    for i in range(1, len(total_time)):
        total_time[i] += total_time[i - 1]
        
    # 광고 시작 위치를 결정하는 변수
    max_view_time = total_time[adv_time_sec - 1]
    max_start_time = 0
    
    # 광고 시간을 기준으로 누적 재생 시간을 계산하여 최대값 찾기
    for start in range(1, play_time_sec - adv_time_sec + 1):
        view_time = total_time[start + adv_time_sec - 1] - total_time[start - 1]
        if view_time > max_view_time:
            max_view_time = view_time
            max_start_time = start
    
    return sec_to_time(max_start_time)