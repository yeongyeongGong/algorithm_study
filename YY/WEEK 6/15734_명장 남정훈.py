L,R,A = map(int,input().split())

#왼발 오른발 인원 차이 몇명이지
people = L-R

if people<0: #음수라면 오른발 잡이가 많은거임
    diff=R-L
    if A<=diff: #양발 인원수가 차이 인원보다 작거나 같으면
        L+=A #왼발에 추가하고
        print(2*L) #어차피 음수에 차이보다 작으면 그냥 왼발 인원 두배로 출력

    else: #양발 인원수가 차이 인원보다 크면
        L+= diff #왼발에 차이나는 인원만큼 추가해주고
        A -= diff #양발 이제 다 빼주고

        #그래도 양발이 남아있으면 오른발 왼발 똑같이 나눠주기
        L += A//2
        R += A//2
        print(L+R)

if people == 0:#왼발 오른발 인원수 같은거임
    L+=A//2
    R+=A//2
    print(L+R)

if people > 0: #양수라면 왼발 잡이가 더 많은거임
    diff = L -R

    if A <= diff:  # 양발 인원수가 차이 인원보다 작거나 같으면
        R += A  # 왼발에 추가하고
        print(2 * R)  # 어차피 음수에 차이보다 작으면 그냥 오른발 인원 두배로 출력

    else:  # 양발 인원수가 차이 인원보다 크면
        R += diff  # 오른발에 차이나는 인원만큼 추가해주고
        A -= diff  # 양발 이제 다 빼주고

        # 그래도 양발이 남아있으면 오른발 왼발 똑같이 나눠주기
        L += A // 2
        R += A // 2
        print(L + R)