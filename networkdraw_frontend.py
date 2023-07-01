import networkx as nx
import matplotlib.pyplot as plt
from threading import Thread
import regina
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import Button


# It will use networkx library to find the planar layout
# parameter : 
#   G : adjacent list of graph
# return : coordinates of nodes
def main(G):
  graph = nx.MultiDiGraph()
  for v in G.keys():
    graph.add_node(v)

  for delta in G.items():
    for w in delta[1]:
      graph.add_edge(delta[0], w)

  posit = nx.planar_layout(graph, scale=10)

  return posit


# It will draw the knot daigram with given position and gauss code
# parameters : 
#   positions : contain coordinates of nodes/crossing
#   stri : gauss code in array format
#   y : size of stri
#   ax : axes of matplotlib
def draw(positions, stri, y, ax) :
  ax.clear()
  edges = set()
  for nodes in positions.keys() :
        xdata, ydata = positions[nodes]
        if((nodes[0] == 'h') or (nodes[0] == 'e')) :
            ax.text(xdata, ydata, nodes, picker=2)
        else :
            ax.text(xdata, ydata, nodes, picker=2, bbox=dict(boxstyle="circle,pad=0.3",
                    fc="lightblue", ec="steelblue", lw=2), horizontalalignment='center')
  for i in range(0, y) :
    nod1 = int(stri[i])
    nod2 = int(stri[(i+1)%y])
    cord1 = positions[str(abs(nod1))]
    cord2 = positions[str(abs(nod2))]
    mid = [(cord1[0] + cord2[0])/2, (cord1[1] + cord2[1])/2]
    if(abs(nod1)==abs(nod2)) :
        eqcord1 = positions["eq1_" + str(abs(nod1))]
        eqcord2 = positions["eq2_" + str(abs(nod1))]
        ax.plot([cord1[0], eqcord1[0]], [cord1[1], eqcord1[1]], 'k')
        ax.plot([eqcord1[0], eqcord2[0]], [eqcord1[1], eqcord2[1]], 'k')
        ax.plot([eqcord2[0], cord1[0]], [eqcord2[1], cord1[1]], 'k')
    else :
        if((str(abs(nod1)) + str(abs(nod2))) in edges) :
            mid = positions['h' + str(abs(nod1)) + str(abs(nod2))]
        else :
            edges.add(str(abs(nod1)) + str(abs(nod2)))
        if(nod1<0) :
            ax.plot([cord1[0] , mid[0]], [cord1[1], mid[1]], '--r')
        else :
            ax.plot([cord1[0] , mid[0]], [cord1[1], mid[1]], ':k')

        if(nod2<0) :
            ax.plot([mid[0], cord2[0]], [mid[1], cord2[1]], '--r')
        else :
            ax.plot([mid[0], cord2[0]], [mid[1], cord2[1]], ':k')
    
  fig.canvas.draw_idle()
  return

# various function trigger on events associated with it
def mouserelease(event) :
  global picked
  picked = False
  
def on_pick(event):
    point = event.artist
    global picked
    global picked_vert
    picked = True
    picked_vert = point.get_text()
    # print(picked)
    if(input_move) :
        print(point)
        point.set_backgroundcolor('red')
        input_array.append(picked_vert)
        fig.canvas.draw_idle()
    
   
def motion(event) :
    if(not picked):
        return
    positions[picked_vert] = [event.xdata, event.ydata]
    draw(positions, stri, y, ax)


def computation() :
  global stri
  global positions
  global gauss_code
  global lnk
  global ax
  global fig
  global y
  global graph
  graph = {}
  n = lnk.size()
  gauss_code = lnk.gauss()
  stri = gauss_code.split()
  y = 2*n
  for i in range(0, y) :
    if(str(abs(int(stri[i]))) in graph) :
        if(abs(int(stri[i])) == abs(int(stri[(i+1)%y]))) :
            graph[str(abs(int(stri[i])))].append("eq1_" + str(abs(int(stri[i]))))
            graph["eq1_" + str(abs(int(stri[i])))] = [("eq2_" + str(abs(int(stri[i]))))]
            graph["eq2_" + str(abs(int(stri[i])))] = [str(abs(int(stri[i])))]
        else :
            if(str(abs(int(stri[(i+1)%y]))) in graph[str(abs(int(stri[i])))]):
                graph[str(abs(int(stri[i])))].append('h' + str(abs(int(stri[i]))) + str(abs(int(stri[(i+1)%y]))))
                graph['h' + str(abs(int(stri[i]))) + str(abs(int(stri[(i+1)%y])))] = [str(abs(int(stri[(i+1)%y])))]
            else :
                graph[str(abs(int(stri[i])))].append(str(abs(int(stri[(i+1)%y]))))
    else:
        if(abs(int(stri[i])) == abs(int(stri[(i+1)%y]))) :
            graph[str(abs(int(stri[i])))] = [("eq1_" + str(abs(int(stri[i]))))]
            graph["eq1_" + str(abs(int(stri[i])))] = [("eq2_" + str(abs(int(stri[i]))))]
            graph["eq2_" + str(abs(int(stri[i])))] = [str(abs(int(stri[i])))]
        else :
            graph[str(abs(int(stri[i])))] = [str(abs(int(stri[(i+1)%y])))]
  positions = main(graph)
  draw(positions, stri, y, ax)


# preprocessing of input from file to variables
file = open("input.txt")
content = file.readlines()
n = int(content[0])
gauss_code = content[1]
lnk = regina.Link.fromGauss(gauss_code)
stri = gauss_code.split()
picked = False
picked_vert = ''
graph = {}
global input_array
input_array = []

# initializing the axes for our figure/plot
fig, ax = plt.subplots()

# getting the position of vertices
positions = main(graph)

computation()

# connecting function with respective events
fig.canvas.mpl_connect('button_release_event', mouserelease)
fig.canvas.mpl_connect('pick_event', on_pick)
fig.canvas.mpl_connect('motion_notify_event', motion)

running = True
arg1 = None
arg2 = None
# this function used by thread to integrate regina with our visualization
def take_input(event):
        print('hello')
    # return
        global lnk

    # while(running):
        move = input_array[0]
        # if(not running) :
        #     break
        changed = False
        if(move == "r1") :
            cros = int(input_array[1])
            if(lnk.r1(lnk.crossing(cros-1), True, True)) :
                changed = True

        elif(move == "r1+"):
            cros1 = int(input_array[1])
            cros2 = int(input_array[2])
            side = arg1
            sign = arg2
            if(lnk.crossing(cros1-1).next(1).crossing().index() == (cros2-1)):
                if((side is not None) and (sign is not None) and (lnk.r1(lnk.crossing(cros1-1).upper(), side, sign, True, True))) :
                    changed = True
            elif(lnk.crossing(cros1-1).next(0).crossing().index() == (cros2-1)) :
                if((side is not None) and (sign is not None) and (lnk.r1(lnk.crossing(cros1-1).lower(), side, sign, True, True))) :
                    changed = True
            elif(lnk.crossing(cros2-1).next(1).crossing().index() == (cros1-1)) :
                if((side is not None) and (sign is not None) and (lnk.r1(lnk.crossing(cros2-1).upper(), side, sign, True, True))) :
                    changed = True
            elif(lnk.crossing(cros2-1).next(0).crossing().index() == (cros1-1)) :
                if((side is not None) and (sign is not None) and (lnk.r1(lnk.crossing(cros2-1).lower(), side, sign, True, True))) :
                    changed = True
        elif(move == "r2"):
            cros1 = int(input_array[1])
            cros2 = int(input_array[2])
            if(lnk.crossing(cros1-1).next(1).crossing().index() == (cros2-1)):
                if(lnk.r2(lnk.crossing(cros1-1).upper(), True, True)) :
                    changed = True
            elif(lnk.crossing(cros2-1).next(1).crossing().index() == (cros1-1)) :
                if(lnk.r2(lnk.crossing(cros2-1).upper(), True, True)) :
                    changed = True
        elif(move == "r2+"):
            cros1 = int(input_array[1])
            cros2 = int(input_array[2])
            cros3 = int(input_array[3])
            cros4 = int(input_array[4])
            side1 = arg1
            side2 = arg2
            arc1 = None
            arc2 = None
            if(lnk.crossing(cros1-1).next(1).crossing().index() == (cros2-1)):
                arc1 = lnk.crossing(cros1-1).upper()
            elif(lnk.crossing(cros1-1).next(0).crossing().index() == (cros2-1)) :
                arc1 = lnk.crossing(cros1-1).lower()
            elif(lnk.crossing(cros2-1).next(1).crossing().index() == (cros1-1)):
                arc1 = lnk.crossing(cros2-1).upper()
            elif(lnk.crossing(cros2-1).next(0).crossing().index() == (cros1-1)) :
                arc1 = lnk.crossing(cros2-1).lower()
            
            if(lnk.crossing(cros3-1).next(1).crossing().index() == (cros4-1)):
                arc2 = lnk.crossing(cros3-1).upper()
            elif(lnk.crossing(cros3-1).next(0).crossing().index() == (cros4-1)) :
                arc2 = lnk.crossing(cros3-1).lower()
            elif(lnk.crossing(cros4-1).next(1).crossing().index() == (cros3-1)):
                arc2 = lnk.crossing(cros4-1).upper()
            elif(lnk.crossing(cros4-1).next(0).crossing().index() == (cros3-1)) :
                arc2 = lnk.crossing(cros4-1).lower()
            
            
            if((arc1 is not None) and (side1 is not None) and (arc2 is not None) and (side2 is not None) and (lnk.r2(arc1, side1, arc2, side2, True, True))) :
                changed = True
        elif(move == "r3"):
            cros1 = int(input_array[1])
            cros2 = int(input_array[2])
            cros3 = int(input_array[3])
            cros = None
            side = None
            if(lnk.crossing(cros1-1).next(1).crossing().index() == (cros2-1)) :
                cros = cros1
                if(lnk.crossing(cros1-1).next(0).crossing().index() == (cros3-1)) :
                    if(lnk.crossing(cros1-1).sign()<0):
                        side = 1
                    else :
                        side = 0
                else :
                    if(lnk.crossing(cros1-1).sign()<0):
                        side = 0
                    else :
                        side = 1
            elif(lnk.crossing(cros1-1).next(1).crossing().index() == (cros3-1)) :
                cros = cros1
                if(lnk.crossing(cros1-1).next(0).crossing().index() == (cros2-1)) :
                    if(lnk.crossing(cros1-1).sign()<0):
                        side = 1
                    else :
                        side = 0
                else :
                    if(lnk.crossing(cros1-1).sign()<0):
                        side = 0
                    else :
                        side = 1
            elif(lnk.crossing(cros2-1).next(1).crossing().index() == (cros3-1)) :
                cros = cros2
                if(lnk.crossing(cros2-1).next(0).crossing().index() == (cros1-1)) :
                    if(lnk.crossing(cros2-1).sign()<0):
                        side = 1
                    else :
                        side = 0
                else :
                    if(lnk.crossing(cros2-1).sign()<0):
                        side = 0
                    else :
                        side = 1
            elif(lnk.crossing(cros2-1).next(1).crossing().index() == (cros1-1)) :
                cros = cros2
                if(lnk.crossing(cros2-1).next(0).crossing().index() == (cros3-1)) :
                    if(lnk.crossing(cros2-1).sign()<0):
                        side = 1
                    else :
                        side = 0
                else :
                    if(lnk.crossing(cros2-1).sign()<0):
                        side = 0
                    else :
                        side = 1
            elif(lnk.crossing(cros3-1).next(1).crossing().index() == (cros2-1)) :
                cros = cros3
                if(lnk.crossing(cros3-1).next(0).crossing().index() == (cros1-1)) :
                    if(lnk.crossing(cros3-1).sign()<0):
                        side = 1
                    else :
                        side = 0
                else :
                    if(lnk.crossing(cros3-1).sign()<0):
                        side = 0
                    else :
                        side = 1
            elif(lnk.crossing(cros3-1).next(1).crossing().index() == (cros1-1)) :
                cros = cros3
                if(lnk.crossing(cros3-1).next(0).crossing().index() == (cros2-1)) :
                    if(lnk.crossing(cros3-1).sign()<0):
                        side = 1
                    else :
                        side = 0
                else :
                    if(lnk.crossing(cros3-1).sign()<0):
                        side = 0
                    else :
                        side = 1
            if((cros is not None) and (side is not None) and (lnk.r3(lnk.crossing(cros-1), side,True, True))) :
                changed = True
        else :
            print("write exact moves\n")
        
        if(changed) :
            computation()
            ax.set_title("It performed\n")
        else :
            draw(positions, stri, y, ax)
            ax.set_title("Unfeasible move try again\n")
        fun_apply()



def add_arg1(label):
    global arg1
    if(label!= 'none'):
        if(label=='left') :
            arg1 = 0
        else :
            arg1 = 1

def add_arg2(label):
    global arg2
    if(label!= 'none'):
        if(label=='left') :
            arg2 = 0
        elif(label=='right') :
            arg2 = 1
        elif(label=='+ ve') :
            arg2 = 1
        elif(label=='- ve') :
            arg2 = 0



def fun_apply():
    global bapply
    global radio2
    global radio3
    if(len(input_array)==0) :
        return
    if(input_array[0]=='r1'):
        fig.delaxes(axapply)
        del bapply
    elif(input_array[0]=='r1+'):
        fig.delaxes(axapply)
        fig.delaxes(axbox2)
        fig.delaxes(axbox3)
        del bapply
        del radio2
        del radio3
    elif(input_array[0]=='r2'):
        fig.delaxes(axapply)
        del bapply
    elif(input_array[0]=='r2+'):
        fig.delaxes(axapply)
        fig.delaxes(axbox2)
        fig.delaxes(axbox3)
        del bapply
        del radio2
        del radio3
    elif(input_array[0]=='r3'):
        fig.delaxes(axapply)
        fig.delaxes(axbox2)
        del bapply
        del radio2
    input_array.clear()

input_move = False

def handle_buttons(label):
    fun_apply()
    draw(positions, stri, y, ax)
    input_array.append(label)
    global input_move
    global axapply
    global axbox2
    global axbox3
    global bapply
    global radio2
    global radio3
    print('here initial')
    if(label=='r1'):
        input_move = True
        ax.set_title('Select the crossing you want to untwist')
        axapply = fig.add_axes([0.81, 0.01, 0.1, 0.075])
        bapply = Button(axapply, 'Apply')
        bapply.on_clicked(take_input)
    elif(label=='r1+') :
        input_move = True
        ax.set_title('Select the edge')
        axbox2 = fig.add_axes([0.001, 0.3, 0.1, 0.2], facecolor=axcolor)
        radio2 = RadioButtons(axbox2, ('none','left', 'right'),
                        label_props={'color': 'cm'},
                        radio_props={'s': [16, 16, 16]})
        radio2.on_clicked(add_arg1)
        print('here2')
        axbox3 = fig.add_axes([0.001, 0.1, 0.1, 0.2], facecolor=axcolor)
        radio3 = RadioButtons(axbox3, ('none','+ ve', '- ve'),
                        label_props={'color': 'cm'},
                        radio_props={'s': [16, 16, 32]})
        radio3.on_clicked(add_arg2)
        axapply = fig.add_axes([0.81, 0.01, 0.1, 0.075])
        bapply = Button(axapply, 'Apply')
        bapply.on_clicked(take_input)
    elif(label=='r2'):
        input_move = True
        ax.set_title('Select any one edge')
        axapply = fig.add_axes([0.81, 0.01, 0.1, 0.075])
        bapply = Button(axapply, 'Apply')
        bapply.on_clicked(take_input)
    elif(label=='r2+') :
        input_move = True
        ax.set_title('Select the upper and lower edge in the order')
        axbox2 = fig.add_axes([0.001, 0.3, 0.1, 0.2], facecolor=axcolor)
        radio2 = RadioButtons(axbox2, ('none','left', 'right'),
                        label_props={'color': 'cm'},
                        radio_props={'s': [16, 16, 16]})
        radio2.on_clicked(add_arg1)
        axbox3 = fig.add_axes([0.001, 0.1, 0.1, 0.2], facecolor=axcolor)
        radio3 = RadioButtons(axbox3, ('none','left', 'right'),
                        label_props={'color': 'cm'},
                        radio_props={'s': [16, 16, 16]})
        radio3.on_clicked(add_arg2)
        axapply = fig.add_axes([0.81, 0.01, 0.1, 0.075])
        bapply = Button(axapply, 'Apply')
        bapply.on_clicked(take_input)
    elif(label=='r3') :
        input_move = True
        ax.set_title('Select the three crossings')
        axapply = fig.add_axes([0.81, 0.01, 0.1, 0.075])
        bapply = Button(axapply, 'Apply')
        bapply.on_clicked(take_input)
    fig.canvas.draw_idle()






axcolor = 'white'
rax1 = fig.add_axes([0.001, 0.7, 0.1, 0.15], facecolor=axcolor)
radio1 = RadioButtons(rax1, ('r1', 'r1+', 'r2', 'r2+', 'r3'),
                     label_props={'color': 'cmy'},
                     radio_props={'s': [16, 16, 16, 16, 16]})

radio1.on_clicked(handle_buttons)












# t1 = Thread(target = take_input)
# t1.start()

plt.show()
running = False
# t1.join()

