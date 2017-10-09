import numpy as np
from ROOT import gROOT, TCanvas, TGraph, gStyle, TF1

gROOT.Reset()
c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

#define x and y dataset
x = np.array( [24, 32, 40, 48, 64, 80], dtype=float )
y = np.array( [4.8, 6.0, 10.2, 12, 18, 27], dtype=float )

#Define Graph object
gr = TGraph( x.size, x, y )

c1.SetGridx()
c1.SetGridy()

gr.SetMarkerStyle(20)
gr.SetMarkerSize(1)

#user defined fit function
f1 = TF1('fitfun', '[0]*x+[1]', 0, 80)
#force paremeter 0 and 1 to initial values
f1.SetParameter(0,1)
f1.SetParameter(1,1)
#apply fit onto graph
gr.Fit(f1)
#fit information in graph

gStyle.SetOptFit(111)

gr.Draw('AP')

c1.Update()
