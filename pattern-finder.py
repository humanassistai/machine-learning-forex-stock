#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
from matplotlib.dates import bytespdate2num
import numpy as np
from matplotlib import style
style.use('ggplot')
(date, bid, ask) = np.loadtxt('GBPUSD1d.txt', unpack=True, delimiter=','
                              ,
                              converters={0: mdates.bytespdate2num('%Y%m%d%H%M%S'
                              )})


def percentChange(startPoint, currentPoint):
    return ((currentPoint-startPoint)/startPoint)*100.00

'''
The goal of patternFinder is to begin collection of %change patterns
in the tick data. From there, we also collect the short-term outcome
of this pattern. Later on, the length of the pattern, how far out we
look to compare to, and the length of the compared range be changed,
and even THAT can be machine learned to find the best of all 3 by
comparing success rates.
'''
def patternFinder():
    #Simple Average
    avgLine = ((bid+ask)/2)
    #This finds the length of the total array for us
    x = len(avgLine)-30
    #This will be our starting point, allowing us to compare to the
    #past 10 % changes.
    y = 11
    # where we are in a trade. #
    # can be none, buy,
    # print('i am here')
    currentStance = 'none'
    while y < x:
        p1 = percentChange(avgLine[y-10], avgLine[y-9])
        p2 = percentChange(avgLine[y-10], avgLine[y-8])
        p3 = percentChange(avgLine[y-10], avgLine[y-7])
        p4 = percentChange(avgLine[y-10], avgLine[y-6])
        p5 = percentChange(avgLine[y-10], avgLine[y-5])
        p6 = percentChange(avgLine[y-10], avgLine[y-4])
        p7 = percentChange(avgLine[y-10], avgLine[y-3])
        p8 = percentChange(avgLine[y-10], avgLine[y-2])
        p9 = percentChange(avgLine[y-10], avgLine[y-1])
        p10= percentChange(avgLine[y-10], avgLine[y])
        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]
        #function to account for the average of the items in the array
        reduce = lambda x, y: x + y, outcomeRange/len(outcomeRange)
        # print(reduce)
        # print("check")
        print(currentPoint)
        print(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
        print('------------------')
        time.sleep(55)
        y+=1


def graphRawFX():
    fig = plt.figure(figsize=(10, 7))
    ax1 = plt.subplot2grid((40, 40), (0, 0), rowspan=40, colspan=40)
    ax1.plot(date, bid)
    ax1.plot(date, ask)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'
                                  ))
    plt.grid(True)
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    plt.subplots_adjust(bottom=.23)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date, 0, ask - bid, facecolor='g', alpha=.3)
    plt.subplots_adjust(bottom=.23)
    plt.show()


graphRawFX()
patternFinder()
