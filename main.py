import tkinter as tk
import math

root = tk.Tk()
intro = tk.Label(text="This is a position size calculator.")
risk = tk.Label(text="Please enter your max risk (in % format). ")
intro.pack()
risk.pack()

maxRisk = tk.Entry(root)
maxRisk.pack()
sL = tk.Label(text="Please enter your stop loss. This will be the maximum risk per share.")
sL.pack()
stopLoss = tk.Entry(root)
stopLoss.pack()


def calculateShares():
    maxDollarRisk = maxRisk.get()
    maxStopLoss = stopLoss.get()
    result = tk.Toplevel(root)
    result.title("Calculated Shares")
    resultLabel = tk.Label(result, text="Position sizing complete. Calculated position size: ")
    resultLabel.pack()
    shareLabel = tk.Label(result, text="{} shares ".format(math.floor((float(maxDollarRisk) / float(maxStopLoss)))))
    shareLabel.pack()


submit = tk.Button(text="Calculate", command=calculateShares)
submit.pack()

root.mainloop()
