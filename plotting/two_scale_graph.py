import pickle
import numpy as np
import matplotlib.pyplot as plt

with open("acc.pkl", "rb") as a:
    acc = pickle.load(a)

with open("loss.pkl", "rb") as b:
    loss = pickle.load(b)

x = np.array([point for point in range(100)])

# plt.style.use('fivethirtyeight')

fig = plt.figure()
graph_1 = fig.add_subplot(111)

lns_1 = graph_1.plot(x, np.array(acc), 'g', label='acc')

graph_2 = graph_1.twinx()

lns_2 = graph_2.plot(x, np.array(loss), 'b', label='loss')

lns = lns_1 + lns_2
labels = [l.get_label() for l in lns]

graph_1.legend(lns, labels, loc=0)
graph_1.grid()

graph_1.set_xlabel("epochs")
graph_1.set_ylabel("acc")
graph_2.set_ylabel("loss")

plt.show()
