import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NanumBarunGothic.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font',family=font_name)
plt.title("영화 장르 네트워크 분석")
G = nx.Graph()

# 엣지 이름 및 weight 가져오기

weightFile = open('genre_weight.csv','r')
weightFile.readline()

for lines in weightFile:
    lines = lines.strip().split(',')
    wgt = lines[2]
    lines.pop(2)
    G.add_edge(lines[0], lines[1], weight=int(wgt))

weightFile.close()

# 그래프 그리기
pos = nx.shell_layout(G)
nx.draw(G, pos=pos, font_family='NanumBarunGothic', font_size=10, with_labels=True)

# weight 값 가져오기
labels = nx.get_edge_attributes(G, 'weight')
edges = G.edges()
weights = [G[u][v]['weight'] for u,v in edges]
nx.draw(G, pos, edges=edges, width = weights)
print(labels)
nx.draw_networkx_edge_labels(G, pos, font_family='NanumBarunGothic', font_size=10, edge_labels=labels, width = weights)
plt.show()
