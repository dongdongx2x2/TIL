# https://school.programmers.co.kr/learn/courses/30/lessons/17683
def minute(time):
    minute = int(time[:2]) * 60 + int(time[3:])
    return minute

def replace(music):
    tem = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    for k, v in tem.items():
        music = music.replace(k, v)
    return music

def solution(m, musicinfos):
    answer = []
    
    for music in musicinfos:
        music = music.split(',')
        music[3] = replace(music[3])
        t = minute(music[1]) - minute(music[0])
        
        if t >= len(music[3]):
            tem = music[3] * (t//len(music[3])) + music[3][:t%len(music[3])]
        
        else:
            tem = music[3][:t]
            
        if replace(m) in tem:
            answer.append((t, music[2]))
    
    if len(answer) == 0:
        return '(None)'
    
    else:
        answer.sort(key=lambda x:-x[0]) 
        return answer[0][1]