import plotext as plt
import pandas as pd
import os
import time

file_path = '/home/pjackim/.config/thokr/log.csv'
last_modification_time = os.path.getmtime(file_path)

def stylize(w=None, h=None):
    plt.theme("clear")
    plt.ticks_style("bold")
    
    if (w is not None):
        plt.plot_size(width=w)
    if (h is not None):
        plt.plot_size(height=h)


def main():
    data = pd.read_csv(file_path)
    data['date'] = pd.to_datetime(data['date'], format='%a %b %d %H:%M:%S %Y')
    data['date'] = data['date'].dt.date

    dates = plt.datetimes_to_string(data['date'], plt.date_form('m/d'))
    
    count = 20
    plt.xticks(ticks = range(len(dates)-1, len(dates)-count, -1))
    plt.xlim(left = len(dates)-count, right = len(dates)-1)
    
    wpm = data['wpm']
    accuracy = data['accuracy']
    date_indices = range(len(dates))
    # print(data) 
    # print(dates)
    x = date_indices
    mark = "─"
    mark = "braille"
    plt.plot(x, accuracy, color="cyan", marker=mark, label="Accuracy %",  yside = "left", fillx = False)
    plt.plot(x, wpm, color="orange", marker=mark, label="WPM", yside = "right", fillx = False)

    plt.title("Typing Statistics")
    stylize()

    yupper = max(wpm) + 15
    ylower = min(min(wpm), min(accuracy))

    ymax = max(wpm)
    increment = 20
    lbound = (min(wpm) - 10) - (min(wpm) % increment)
    plt.yticks(ticks = range(lbound, ymax-(ymax % 20)+21, increment), yside="right")
    plt.ylabel("WPM", yside="right")
    plt.ylim(lbound, max(wpm)+20, yside="right")

    increment = 5
    lbound = (min(accuracy) - 10) - (min(accuracy) % increment)
    plt.yticks(ticks = range(lbound, 101, increment), yside="left")
    plt.ylabel("Accuracy %", yside="left")
    plt.ylim(lbound, max(accuracy), yside="left")
    plt.show()


main()

while True:
    current_modification_time = os.path.getmtime(file_path)
    if current_modification_time != last_modification_time:
        last_modification_time = current_modification_time
        plt.clear_terminal()
        plt.clear_data()
        plt.clear_figure()
        main()
    else:
        time.sleep(1)  # Wait for 1 second before checking again
        