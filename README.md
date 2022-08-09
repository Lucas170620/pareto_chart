# pareto_chart
This application aims plot pareto chart using Python with Tkinter for graphic user interface and matplotlib for plot

Input:
color for bar -> chose using colorchooser.askcolor , the interface pre-made of Tkinter
Xml File -> open using askopenfilename from tkinter, you choose an file in the following format:
        <?xml version="1.0" encoding = "ISO-8859-1"?>
            <data>
                <cd>
                    <name>exemplo</name>
                    <number>20</number>
                </cd>
                <cd>
                    <name>exemplo2</name>
                    <number>30</number>
                </cd>
                <cd>
                    <name>exemplo3</name>
                    <number>60</number>
                </cd>
            </data>
Output:
-> Pareto Chart ploted in the colors chose
-> Can it be save the chart in your pc in the bottom corner
