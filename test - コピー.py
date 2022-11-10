from matplotlib import pyplot as p


def show_plt(sleeptime = 0.5):
    XMAX = 10 #  x方向の表示大きさ
    time = 0  #  x軸
    x = [time]
    y = [0]
    fig, ax = p.subplots(1,1)
    ax.set_xlim( (0, XMAX) )
    while True:
        line, = ax.plot(x, y, color="blue")

        time += sleeptime
        x.append(time)
        y.append(file_to_data("./csv.txt"))

        if time > XMAX:
            ax.set_xlim( (time-XMAX, time) )
        
        p.pause(sleeptime)
        line.remove()


def file_to_data(path):
    Data = []
    with open(path, 'r') as f:
        f.readline()
        Data = f.readlines()[-1]
    Data.strip()
    return int(Data)


if __name__ == '__main__':
    show_plt()
