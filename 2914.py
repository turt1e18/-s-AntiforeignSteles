from sys import stdin

input = stdin.readline

song_num, song_avg = map(int, input().rstrip().split(" "))

print(song_num*(song_avg-1)+1)

# 1단 공식:  저작권 멜로디 개수 / 앨범 수록곡 개수 = 멜로디 포함 곡 평균값  -> 이때 평균값은 올림으로 항상 정수여야 한다
# 2단 구하고 싶은 것 : `저작권이 있는 멜로디의 곡수``
# 3단 입력값 : 수록 곡 수, 멜로디 포함 곡 평균값
# 4단 그렇다면 ? / 수록곡 = 평균값 -> ? = 수록곡 * (평균값-1) + 1 -> 올림햇으니 -1