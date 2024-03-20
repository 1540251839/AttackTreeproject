import random
import matplotlib.pyplot as plt

n = 350
core_node = int(0.02 * n)
relay_node = int(0.2 * n)
service_node = n - core_node - relay_node

print("core_node: ", core_node)
print("relay_node: ", relay_node)
print("service_node: ", service_node)

DuList = [13 + random.randint(-1, 3) for _ in range(core_node)] + [6 + random.randint(-1, 3) for _ in range(relay_node)] + [3 + random.randint(-1, 3) for _ in range(service_node)]
PageRankLst = [int(I*3.14 + random.randint(-4, 3)) for I in DuList]

DuListSample = {}
PageRankLstSample = {}

print(DuList)
print(PageRankLst)
for i in range(len(DuList)):
    if DuList[i] not in DuListSample.keys():
        DuListSample[DuList[i]] = 0
    DuListSample[DuList[i]] += 1
    if PageRankLst[i] not in PageRankLstSample.keys():
        PageRankLstSample[PageRankLst[i]] = 0
    PageRankLstSample[PageRankLst[i]] += 1

# 现在对DuListSample和PageRankLstSample画散点图进行可视化
plt.scatter(DuListSample.values(), DuListSample.keys(), s=10, c='r', marker='o')
plt.scatter(PageRankLstSample.values(), PageRankLstSample.keys(), s=10, c='b', marker='o')
plt.xlabel('Frequency')
plt.ylabel('Degree or PageRankValue')
plt.show()

# 现在对DuList和PageRankLst画折线图进行可视化
SumLst = []
for index, i in enumerate(DuList):
    SumLst.append([i, PageRankLst[index]])
# 现在基于SumLst中的每个列表子元素的第一项对其进行排序
SumLst.sort(key=lambda x: x[0])
# 现在对SumLst中的元素进行可视化，画出两条折线图
plt.plot([i[1] for i in SumLst], c='r', label='PageRankValue')
plt.plot([i[0] for i in SumLst], c='b', label='Degree')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.show()