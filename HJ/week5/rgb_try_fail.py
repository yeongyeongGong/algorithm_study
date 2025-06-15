### 백준 - 1149 RGB 거리
'''
3
26 40 83
49 60 57
13 89 99

4
5 4 3
1 1 2
1 5 1
5 3 2


'''

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

dp_n = ['']*N
dp = [0] * N

dp[0] = min(house[0])
dp_n[0] = house[0].index(dp[0])

i = 0
while i < N-1 :
    i += 1
    if i == 1 :
        tmp_now = house[i][:]
        tmp_now[dp_n[i-1]] = 1001
        min_idx = house[i].index(min(house[i]))
        tmp_last = house[i-1][:]
        tmp_last[min_idx] = 1001
        dp[1] = min(dp[0] + min(tmp_now), min(house[i]) + min(tmp_last))
        if dp[1] == dp[0] + min(tmp_now) :
            if tmp_now.count(min(tmp_now)) >= 2 and i < N-1 :
                min_idx = house[2].index(min(house[2]))
                if tmp_now.index(min(tmp_now)) == min_idx :
                    idx = tmp_now.index(min(tmp_now))
                    dp_n[1] = tmp_now.index(min(tmp_now), idx+1)
                    continue
            dp_n[1] = tmp_now.index(min(tmp_now))

        else :
            if house[i].count(min(house[i])) >= 2 and i < N-1 :
                min_idx = house[2].index(min(house[2]))
                if house[i].index(min(house[i])) == min_idx :
                    idx = house[i].index(min(house[i]))
                    dp_n[1] = house[i].index(min(house[i]), idx+1)
                    continue
            dp_n[1] = house[i].index(min(house[i]))
    else :
        tmp_now = house[i][:]
        tmp_now[dp_n[i-1]] = 1001
        num1 = dp[i-1] + min(tmp_now)

        num2 = []
        tmp_min = min(house[i])
        if house[i].count(tmp_min) >= 2 and i < N-2 :
            next_min = house[i+1].index(min(house[i+1]))
            if house[i].index(tmp_min) == next_min :
                idx = house[i].index(tmp_min)
                min_idx = house[i].index(tmp_min, idx+1)
            else :
                min_idx = house[i].index(tmp_min)
        else :
            min_idx = house[i].index(tmp_min)
        tmp_last = house[i-1][:]
        tmp_last[min_idx] = 1001
        tmp_last[dp_n[i-2]] = 1001
        num2 = tmp_min + dp[i-2] + min(tmp_last)
        # print('#',i)
        # print(num1, num2)
        dp[i] = min(num1, num2)
        if dp[i] == num1 :
            if tmp_now.count(min(tmp_now)) >= 2 and i < N-2 :
                min_idx = house[i+1].index(min(house[i+1]))
                if tmp_now.index(min(tmp_now)) == min_idx :
                    idx = tmp_now.index(min(tmp_now))
                    dp_n[i] =tmp_now.index(min(tmp_now), idx+1)
                    continue
            dp_n[i] = tmp_now.index(min(tmp_now))
        else :

            dp_n[i] = min_idx

print(dp)
print(dp_n)

print(dp[i])
