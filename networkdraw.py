import networkx as nx
import matplotlib.pyplot as plt

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
  edges = set()
  for nodes in positions.keys() :
    xdata, ydata = positions[nodes]
    ax.text(xdata, ydata, nodes, picker=5)
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

  return

# various function trigger on events associated with it
def mousepres(event):
  print(event)

def mouserelease(event) :
  global positions
  ax.clear()
  draw(positions, stri, y, ax)
  global picked
  picked = False
  fig.show()
  
def on_pick(event):
  point = event.artist
  global picked
  global picked_vert
  picked = True
  picked_vert = point.get_text()

def motion(event) :
  if(not picked):
    return
  positions[picked_vert] = [event.xdata, event.ydata]
  ax.clear()
  draw(positions, stri, y, ax)
  fig.show()


# preprocessing of input from file to variables
file = open("input.txt")
content = file.readlines()
n = int(content[0])
gauss_code = content[1]
stri = gauss_code.split()
global picked 
picked = False
picked_vert = ''

# preprocessing of data before converting it to planar network
graph = {}
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

# initializing the axes for our figure/plot
fig, ax = plt.subplots()

# getting the position of vertices
positions = main(graph)

# drawing the planar graph
draw(positions, stri, y, ax)


# connecting function with respective events
fig.canvas.mpl_connect('button_press_event', mousepres)
fig.canvas.mpl_connect('button_release_event', mouserelease)
fig.canvas.mpl_connect('pick_event', on_pick)
fig.canvas.mpl_connect('motion_notify_event', motion)

plt.show()

