import numpy as np
import math as m
from ROOT import gROOT, TCanvas, TGraph

gROOT.Reset()
c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

#define x and y dataset
x = np.linspace(0, 2, 20)
y1 = x*x
y2 = np.sin(x)

#Define Graph object
gr1 = TGraph( x.size, x, y1 )
gr2 = TGraph( x.size, x, y2 )

#grid of x and y
c1.SetGridx()
c1.SetGridy()

gr1.SetMarkerStyle(21)
gr1.SetMarkerColor(2)
gr1.SetLineColor(2)
gr1.Draw("ACP")
#superimpose the second graph by leaving out the axis option A
gr2.SetMarkerStyle(23);
gr2.SetMarkerColor(4)
gr2.SetLineColor(4)
gr2.Draw("CP")

c1.Update()
