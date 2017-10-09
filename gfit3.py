import numpy as np
from ROOT import gROOT, TCanvas, TGraph, gStyle, TF1, TGraphErrors

gROOT.Reset()
c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

#define x and y dataset and errors x and y
x  = np.array( [24, 32, 40, 48, 64, 80],       dtype=float )
y  = np.array( [4.8, 6.0, 10.2, 12, 18, 27],   dtype=float )
ex = np.array( [0, 0, 0, 0, 0, 0],             dtype=float )
ey = np.array( [0.3, 0.4, 1.0, 1.1, 1.4, 1.5], dtype=float )

#Define Graph object
gr = TGraphErrors( x.size, x, y, ex, ey )

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
