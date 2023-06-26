def solution(wallpaper):
    w = []    # 가로 좌표
    h = []    # 세로 좌표
    
    for i in range(len(wallpaper)):            
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                w.append(i)                  # '#'의 가로 시작
                h.append(j)                  # '#'의 세로 시작
    
    answer = [min(w), min(h), max(w) + 1, max(h) + 1]    # 아이콘의 크기 = 1, 가장 먼 아이콘의 시작 좌표 + 1 = 아이콘 끝 좌표 
        
    return answer
