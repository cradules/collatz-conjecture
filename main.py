import numpy as np
import matplotlib.pyplot as plt
import os.path
import logging
import sys
import time

# Log information to stdout. Change log level from "root.setLevel"
root = logging.getLogger()
root.setLevel(logging.INFO)  # Here you can change the log level

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

start_time: float = time.time()

dst: int = int(input("Enter a range \n"))
dst: int = dst ** 10  # calculate to power of 10
print(f"The iteration will run from 1 to {dst} iterations.")
save_to = './plot-graphs/'

for n in range(1, int(dst)):
    data = [n]
    name_file = n
    fig, ax = plt.subplots()
    while n > 1:
        if (n % 2) == 0:
            n = int(n / 2)
            data.append(n)
        else:
            n = n * 3 + 1
            data.append(n)
    data = np.array(data)
    plt.plot(data)
    plt.grid(True)
    for index, value in enumerate(data):
        plt.text(index, value, str(value), size='xx-small')
    if not os.path.exists(save_to + f"{name_file}-plot.svg"):
        fig.savefig(save_to + f"{name_file}-plot.svg", format="svg", dpi=1200)
    plt.close(fig)

print("--- %s seconds ---" % (time.time() - start_time))
