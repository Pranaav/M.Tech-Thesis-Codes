import networkx as nx
import matplotlib.pyplot as plt
from threading import Thread
import regina

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
    ax.text(xdata, ydata, nodes, picker=2)
  for i in range(0, y) :
    nod1 = int(stri[i])
    nod2 = int(stri[(i+1)%y])
    cord1 = positions[str(abs(nod1))]
    cord2 = positions[str(abs(nod2))]
    mid = [(cord1[0] + cord2[0])/2, (cord1[1] + cord2[1])/2]
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
  global positions
  draw(positions, stri, y, ax)
  global picked
  picked = False
  
def on_pick(event):
    point = event.artist
    global picked
    global picked_vert
    picked = True
    picked_vert = point.get_text()
    print(picked)
   
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
      if(str(abs(int(stri[(i+1)%y]))) in graph[str(abs(int(stri[i])))]):
        graph[str(abs(int(stri[i])))].append('h' + str(abs(int(stri[i]))) + str(abs(int(stri[(i+1)%y]))))
        graph['h' + str(abs(int(stri[i]))) + str(abs(int(stri[(i+1)%y])))] = [str(abs(int(stri[(i+1)%y])))]
      else :
        graph[str(abs(int(stri[i])))].append(str(abs(int(stri[(i+1)%y]))))
    else:
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
# this function used by thread to integrate regina with our visualization
def take_input():
  global lnk

  while(running):
    move = input("enter your move r1/r1+/r2/r2+/r3\n")
    if(not running) :
      break
    changed = False
    if(move == "r1") :
        cros = int(input("enter crossing number\n"))
        if(lnk.r1(lnk.crossing(cros-1), True, True)) :
            changed = True

    elif(move == "r1+"):
        cros1 = int(input("enter crossing number of starting point of edge\n"))
        cros2 = int(input("enter crossing number of ending point of edge\n"))
        side = int(input("enter the side you want twist left or right -- 0/1\n"))
        sign = int(input("enter the sign you want of twist -ve or +ve -- 0/1\n"))
        if(lnk.crossing(cros1-1).next(1).crossing().index() == (cros2-1)):
          if(lnk.r1(lnk.crossing(cros1-1).upper(), side, sign, True, True)) :
              changed = True
        else :
          if(lnk.r1(lnk.crossing(cros1-1).lower(), side, sign, True, True)) :
              changed = True
    elif(move == "r2"):
        cros = int(input("enter the crossing number of upper arc starting point\n"))
        if(lnk.r2(lnk.crossing(cros-1), True, True)) :
            changed = True
    elif(move == "r2+"):
        cros1 = int(input("enter the crossing number of upper arc starting point\n"))
        cros2 = int(input("enter the crossing number of lower arc starting point\n"))
        side1 = int(input("enter the side you want new arc be wrt upper arc left or right -- 0/1\n"))
        side2 = int(input("enter the side you want new arc be wrt lower arc left or right -- 0/1\n"))
        if(lnk.r2(lnk.crossing(cros1-1).upper(), side1, lnk.crossing(cros2-1).lower(), side2, True, True)) :
            changed = True
    elif(move == "r3"):
        cros = int(input("enter the crossing number of upper arc starting point\n"))
        side = int(input("enter the side third crossing is on left or right -- 0/1\n"))
        if(lnk.r3(lnk.crossing(cros-1), side,True, True)) :
            changed = True
    else :
        print("write exact moves\n")
    
    if(changed) :
      print("It performed\n")
      computation()
    else :
      print("Unfeasible move try again\n")


t1 = Thread(target = take_input)
t1.start()
plt.show()
running = False
t1.join()

