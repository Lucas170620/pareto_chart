import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import xml.etree.ElementTree as ET

def show_pareto_graphic( filename:str , bar_color:str , line_color:str ):

    data = ET.parse(filename)
    root = data.getroot()
    dataframe = []
    indexes = []
    for i in root:
        dataframe.append(int(i[1].text))
        indexes.append(i[0].text)
    df = pd.DataFrame({'number': dataframe})
    df.index = indexes
    df = df.sort_values(by='number', ascending=False)
    df['percentage'] = (df['number'].cumsum()/df['number'].sum())*100
    line_size = 4
    fig, ax = plt.subplots()
    ax.bar(df.index, df['number'], color=bar_color)
    ax2 = ax.twinx()
    ax2.plot(df.index, df['percentage'], color=line_color, marker="D", ms=line_size)
    ax2.yaxis.set_major_formatter(PercentFormatter())
    ax.tick_params(axis='y', colors=bar_color)
    ax2.tick_params(axis='y', colors=line_color)
    plt.show()