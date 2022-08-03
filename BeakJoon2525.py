#반복문 오븐 시계

# 현재시각 A시 B분
A,B = map(int,input().split())

# 요리하는데 필요한 시간 C
C = int(input())


# if A+1 >= 24 and (B+C) >= 120:
#     print(abs(A-24),(B+C)-120)
#
# elif A+1 >= 24 and (B+C) >= 60:
#     print(abs(A-24),(B+C)-60)
#
#
# elif A+1 < 24 and (B+C) >= 120:
#     print(A+2, (B+C)-120)
#
# elif A+1 < 24 and (B+C) >= 60:
#     print(A+1,(B+C)-60)
#
# elif A+1 < 24 and (B+C)<60:
#     print(A,B+C)

# ---------------------------------
# if A+1 >= 24:
#     if (B+C) >= 120:
#         print(abs(A-24),(B+C)-120)
#     elif (B+C) >= 60:
#         print(abs(A-23),(B+C)-60)
#
# else:
#     if (B+C) >= 120:
#         print(A+2, (B+C)-120)
#     elif (B+C) >= 60:
#         print(A+1,(B+C)-60)
#     else:
#         print(A, B + C)

# ---
A += C//60
B += C%60

if C>=60:
    A += 1
    B -= 60

if A>=24:
    A -= 24

print(A,B)