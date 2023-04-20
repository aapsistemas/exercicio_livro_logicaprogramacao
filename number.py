import math
A = 1
B = 5
C = 3
if (A > B) and (A > C) and (B > C):
    print(str(A) + str(B) + str(C))

elif (A > B) and (A > C) and (C > B):

    print(str(A) + str(C) + str(B))

elif (B > A) and (B > C) and (A > C):

    print(str(B) + str(A) + str(C))

elif (B > A) and (B > C) and (C > A):

    print(str(B) + str(C) + str(A))

elif (C > A) and (C > B) and (A > B):

    print(str(C) + str(A) + str(B))

elif (C > A) and (C > B) and (B > A):

    print(str(C) + str(B) + str(A))



