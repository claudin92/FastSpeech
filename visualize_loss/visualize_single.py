import matplotlib.pyplot as plt
import numpy as np


def visualize(file_name, start, end=-1):
    plt.figure()

    loss_arr = np.array(list())

    cnt = 0
    with open(file_name, "r") as f_loss:
        for loss in f_loss.readlines():
            # print(loss)
            # cnt = cnt + 1
            # # print(cnt)
            # if cnt % 100 == 0:
            #     print(cnt)
            loss_arr = np.append(loss_arr, float(loss))

    loss_arr = loss_arr[start:end]

    x = np.array([i for i in range(np.shape(loss_arr)[0])])
    y = loss_arr

    # print("#########")
    # print(np.shape(y))
    # print(np.shape(x))

    plt.plot(x, y, color="y", lw=0.7)
    plt.xlabel("sequence number")
    plt.ylabel("loss item")
    plt.title("loss")
    # plt.show()
    plt.savefig("loss_one.jpg")


if __name__ == "__main__":
    # Test
    visualize("total_loss.txt", 7000)
