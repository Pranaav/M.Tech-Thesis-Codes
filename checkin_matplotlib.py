import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.patches import Arc

n = 21

# list1 = [1, 6, -7, 10, 11, 12, -14, -15 ,16 ,-17, -18 ,-2 ,3, -4, 5 ,7 ,
# -9 ,-11 ,17, -21, 19, -20, -8 ,9, -10, 18, 21, -16, -13, 14, 20 ,-1, 2,
# -3, 4, -5, -6, 8, -12, 13, 15, -19]
# [1, 20, 19, 21, 18, 17, 16, 15, 14, 13, 12, 11, 9, 8, 6, 5, 4, 3, 2, 7, 10]

# list1 = [2, -3, 4, -19, 16, -21, -22,
# 1, -20, 26, -27, -29, 21, -16, -17, 7, -8, -13, -26, -25, 28 ,27 ,14,
# -15, 29, 30 ,-31, -28 ,25, -24, 23, 31, -30, 22 ,19 ,-18, 6 ,9 ,11,
# -12, 13, -14, 15 ,17, 18, 5, -9, 10, 12, 20, 24, -23, -1, -2 ,3, -4, -5,
# -6, -7 ,8, -10, -11]

# list1 = [-1, 2 ,-3, -4, -5, 6 ,-7 ,8 ,-9 ,10 ,-11, 12 ,-13, 3 ,14,
# -15, 16, -17 ,18 ,-19, 20 ,1, -21, 22, -23 ,24 ,-25 ,7 ,-26, 27, -10,
# 28, -29, 13 ,4 ,30, 31, -32, 17, -33, 34, 35, -2, -36, -22 ,-37, -38,
# 25, -8, 39, -27, 11, -40, 29, 41, 23, 37, -31, 42, -16, 33, -43, 19,
# -20, -35, -14, -30, 5, -6, 38, -24, 9, -39, 26, -12, 40, -28, -41, 36,
# 21, 32, -42, 15, -34, 43, -18]
# code = [1, 20, 19, 18, 17, 16, 15, 14, 3, 2, 35, 34, 33, 32, 31, 30, 4, 
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 29, 28, 40, 26, 39, 27, 24, 23, 41, 22, 
# 36, 21, 38, 37, 25, 42, 43]


# list1 = [-1, 2, -3, 4, -5, -6, 7, -8, 9 ,1, -2, 3,
# -4, -9, 6, -7, 8, 5]
# lis2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# fromm code = [1, 9, 8, 7, 6, 5, 4, 3, 2]   doneeee

# list1 = [1, -2, 3 ,4, 5, -6, 7 ,-8, 9 ,-3, 10, -1, 2
# ,-10, -4 ,-9 ,8 ,-5, 6, -7]
# lis2 = [1, 10, 2, 3, 4, 5, 6, 7, 8, 9]
# fromm code = [1, 10, 2, 3, 9, 8, 7, 6, 5, 4]    not doneee

# list1  = [-1, 2, 3, 4, -5, 6,
# 7, 8, -9, 10, -4, 5 ,-6, -3 ,-2, -7 ,-10, 1, -8, 9]
# list1 = [-1, 6, 7, 10, -9, 8, 5, 4, -3, 2, -10, 9, -8, -7, -6, -5, -2, 1, -4, 3]
# lis2 = [1, 4, 5, 6, 3, 2, 7, 10, 9, 8]

# list1 = [-1, 2, -3, 4 ,5 ,-6 ,7 ,1 ,-4, 3, -2, -5, 8,
# -9, 6 ,-7, 9 ,-8]
# lis2 = [1, 2, 3, 4, 5, 6, 7, 9, 8]
# fromm code = [1, 7, 6, 5, 4, 3, 2, 9, 8]  not doneee

# list1 = [1, -2, 3, -4, -5, 6, -7, 8, -9, -10, 11,
# -1, 2, -3, 4, -11, 10, 7, -8, 9, -6, 5]

# list1 = [1, -2, 3 ,4, 5, -6, 7, -8, 9 ,-3, 10, -1, 2,
# -10, -4, -9, 8, -5, 6, -7]

# list1 = [-1, 2, 3 ,-4, -5, -6, -7 ,8,
# -9, 10, -11, -3 ,4, -12, 13, 14, -8, 7 ,-14, -15, 12, 5 ,-2, 1, -16, 11,
# -10, 9, 15, -13, 6, 16]
list1 = [1, 6, -7, 10, 11, 12, -14, -15, 16, -17, -18, -2, 3 ,-4, 5, 7, -9, -11, 17, -21, 19, -20, -8, 9, -10, 18, 21, -16, -13, 14, 20, -1, 2 ,-3, 4 ,-5, -6, 8, -12,
 13, 15, -19]
# list1 = [1 ,2, -3, 4 ,5 ,-6, -7, 8 ,-9, 10, -11,
# -5, 12, -1 ,6, 13, -10, -14, -4, 15, -2 ,9, -8, 7, -13, 11, 14, 3, -15,
# -12]

# list1 = [1, -4, -3, 6, 5, -2, -7, 8 ,4, -5, -9, 10, 2, -1, -11, 7 ,12, -13, -6, 3, 14,
# -12, -10, 9, 13, -14, -8, 11, 15, -18, -17, 20 ,19, -16, -21, 17 ,22 ,-23, -20, 21 ,24,
# -15, -25, 26, 16, -19, -27, 28 ,18 ,-24, -26 ,27 ,23 ,-22, -28, 25]
lef_up = set()
lef_down = set()
ryt_up = set()
ryt_down = set()

lis = []



# lis2 = [1, 2, 10, 9, 5, 4, 8, 7, 6 , 13, 12, 14 , 11, 3 , 15]

# list1 = [1, -4, -3, 6, 5, -2, -7, 8 ,4, -5, -9, 10, 2, -1, -11, 7 ,12, -13, -6, 3, 14,
# -12, -10, 9, 13, -14, -8, 11, 15, -15]
# lis2 = [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]

ind =  [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# lis2 = [1, 15, 2, 10, 9, 5, 6, 13, 12, 14, 3, 4, 8, 7, 11]
# lis2 = [1, 11, 15, 4, 3, 6, 5, 2, 7, 8, 12, 13, 14, 9, 10]
# lis2 = [1, 2, 10, 9, 5, 4, 8, 6 , 13, 12, 14 , 3, 7, 11 , 15]
# lis2 = [1, 2, 10, 9, 5, 4, 8, 7, 6 , 13, 12, 14 , 3, 11 , 15]
# lis2 = [1, 2, 3, 4, 5, 6, 7, 9, 8]
# lis2 = [1, 7, 6, 5, 4, 3, 2, 9, 8]


# lis2 = ind



dict = {}

for i in range(0, len(list1)) :
    dict[list1[i]] = i

j = list1.index(-list1[0])
itrat = [list1[0], -list1[0]]
don = set()
code = [1]
while len(code) < n :
    # print(code)
    # print("itratttttt")
    # print(itrat)
    if(len(itrat)==0):
        # break
        itrat.append(list1[2*len(code)])
        itrat.append(-list1[2*len(code)])
        code.append(abs(list1[2*len(code)]))
    num = itrat.pop()
    i1 = dict[num]
    # print(itrat)
    # don.add(num)
    pro = []
    samp = []
    samp_itrat = itrat.copy()
    pro_code = code.copy()
    # print(num)
    # print(code)
    while True :
        num1 = list1[i1]
        if(i1==0) :
            don.add(num)
            break
        i1 -=1
        num2 = list1[i1]
        
        if(abs(num2) in code) :
            # print("hell222")
            if(abs(num2) == abs(num)):
                # print(pro_code)
                while(len(pro)!=0) :
                    # print(pro_code)
                    pro_code.append(pro.pop())
                    samp_itrat.append(samp.pop())
                    samp_itrat.append(samp.pop())
                code = pro_code.copy()
                itrat = samp_itrat.copy()
                # print(code)
            don.add(num)
            break
        if(dict[-num2] < i1) :
            if(num1 not in don) :
                itrat.append(num1)
                itrat.append(-num1)
                don.add(num1)
                # print("yes")
                break
        
        itrat.append(num2)
        itrat.append(-num2)
        samp.append(-num2)
        samp.append(num2)
        code.append(abs(num2))
        pro.append(abs(num2))
        if(dict[num] < dict[-num]) :
            # print("hell")
            don.add(num)
            break
        don.add(num)

print(code)

# code = [1, 10, 2, 3, 4, 5, 6, 7, 8, 9]

# code = lis2
code = [0 ,5 ,19, 7, 18, 6, 13, 14, 20, 8, 11, 12, 15, 1, 10, 16, 17, 2, 9, 3, 4]

# list1 = [1, -4, -3, 6, 5, -2, -7, 8 ,4, -5, -9, 10, 2, -1, -11, 7 ,12, -13, -6, 3, 14,
# -12, -10, 9, 13, -14, -8, 11, 15, -18, -17, 20 ,19, -16, -21, 17 ,22 ,-23, -20, 21 ,24,
# -15, -25, 26, 16, -19, -27, 28 ,18 ,-24, -26 ,27 ,23 ,-22, -28, 25]
# code = [1, 12, 15, 4, 14, 11, 10, 13, 7, 6, 5, 3, 2, 8, 9]
# code = [1, 2, 10, 9, 5, 6, 13, 12, 14, 3, 4, 8, 7, 11, 15, 24, 21, 16, 26, 25, 28, 27, 19, 20, 23, 22, 17, 18]
# code = [1, 10, 2, 3, 4, 5, 6, 7, 8, 9]
# code = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ,21 ,22, 23, 24, 25 ,26, 27, 28]
# code = [1, 20, 19, 18, 17, 16, 15, 14, 3, 2, 35, 34, 33, 32, 31, 30, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 29, 28, 40, 26, 39, 27, 24, 23, 41, 22, 36, 21, 38, 37, 25, 42, 43]
# code = [1, 20, 19, 18, 17, 16, 15, 14, 3, 2, 35, 34, 33, 32, 31, 30, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 29, 28, 40, 26, 39, 27, 24, 23, 41, 22, 36, 21, 38, 37, 25, 42, 43]
# code = [1, 20, 19, 18, 17, 16, 15, 14, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 2, 35, 34, 33, 32, 31, 30, 29, 28, 40, 26, 39, 24, 23, 41, 27, 25, 38, 37, 36, 43, 42, 21, 22]
#        [1, 20, 19, 18, 17, 16, 15, 14, 3, 2, 35, 34, 33, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 29, 28, 40, 26, 39, 27, 24, 23, 41, 22, 36, 21, 38, 37, 25, 30, 42, 32, 31, 43]

for i in range(0, (2*n)) :
    y = abs(list1[i])
    if list1[i] < 0 :
        lis.append(-code.index(y-1) - 1 )
    else :
        lis.append(code.index(y-1) + 1 )

print(lis)

# lis  = [-1, 2, -3, 4, -5, 6,
# 7, 8, -9, 10, -4, 5 ,-6, 3 ,-2, -7 ,-10, 1, -8, 9]

# lis = [1, -2, 3 ,4, 5, -6, 7 ,-8, 9 ,-3, 10, -1, 2
# ,-10, -4 ,-9 ,8 ,-5, 6, -7]


# j = 1
# for i in range(0, (2*n)) :
#     if list1[i] in dict :
#         lis.append(dict[list1[i]])
#     else :
#         if(list1[i] < 0) :
#             dict[list1[i]] = -j
#             dict[-list1[i]] = j
#             lis.append(-j)
#         else :
#             dict[list1[i]] = j
#             dict[-list1[i]] = -j
#             lis.append(j)
#         j += 1

# print(lis)


# '''
def draw_knot(lis, n) :
    n = 2*n
    pr = -1
    for i in range(0, n):
        st = lis[i%n]
        end = lis[(i+1)%n]
        rad = abs(st) - abs(end)
        if(rad==0) :
            if((st<0) and pr == -1) or ((end<0) and pr == 1):
                arc = Arc((abs(st) + 0.25, 0),
                -0.5, 0.5, theta1=0.0, theta2=20.0)

            else :
                arc = Arc((abs(st) + 0.25, 0),
                -0.5, 0.5, theta1=340.0, theta2=360.0)
        # end then st
        elif rad >0 :
            if(st<0):
                if(end<0):
                    if pr ==-1 :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=200.0, theta2=340.0)
                        pr = 1
                    else :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=20.0, theta2=160.0)
                        pr = -1

                else :
                    if pr ==-1 :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=180.0, theta2=340.0)
                        pr = 1
                    else :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=20.0, theta2=180.0)
                        pr = -1
            else :
                if(end<0):
                    if pr ==-1 :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=200.0, theta2=360.0)
                        pr = 1
                    else :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=0.0, theta2=160.0)
                        pr = -1

                # end > 0 st > 0
                else:
                    if pr ==-1 :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=180.0, theta2=360.0)
                        pr = 1
                    else :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=0.0, theta2=180.0)
                        pr = -1
        
        # st then end
        else :
            if(st<0):
                if(end<0):
                    if pr ==-1 :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=200.0, theta2=340.0)
                        pr = 1
                    else :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=20.0, theta2=160.0)
                        pr = -1

                else :
                    if pr ==-1 :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=200.0, theta2=360.0)
                        pr = 1
                    else :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=0.0, theta2=160.0)
                        pr = -1
            else :
                if(end<0):
                    if pr ==-1 :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=180.0, theta2=340.0)
                        pr = 1
                    else :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=20.0, theta2=180.0)
                        pr = -1

                # end > 0 st > 0
                else:
                    if pr ==-1 :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=180.0, theta2=360.0)
                        pr = 1
                    else :
                        arc = Arc((abs(end) + (rad/2) , 0),
                        abs(rad), abs(rad), theta1=0.0, theta2=180.0)
                        pr = -1
        axes.add_artist(arc)

# '''
figure, axes = plt.subplots()
# Drawing_colored_circle = plt.Circle(( 0, 0 ), 0.5, fill = False)

# elip = Ellipse((0, 0), 1, 0.5, fill = False)
# arc = Arc((0,0), 1, 1, theta1=0.0, theta2=50.0)



axes.set_aspect( 1 )
# axes.add_artist( Drawing_colored_circle )
# axes.add_artist(arc)
draw_knot(lis, n)

axes.set_xlim(0, n+1)
axes.set_ylim(-n, n)
plt.title( 'Colored Circle' )
plt.grid()

plt.show()
