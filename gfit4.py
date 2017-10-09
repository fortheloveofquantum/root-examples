import numpy as np
from ROOT import gROOT, TCanvas, TGraph, gStyle, TF1, TGraphErrors

gROOT.Reset()
c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

#define x and y dataset and errors x and y
x  = np.array( [0.5, 1.0, 1.5, 2.0, 2.5, 3.0], dtype=float )
y  = np.array( [2.7, 4.7, 6.3, 7.6, 8.6, 9.3], dtype=float )
ex = np.array( [0, 0, 0, 0, 0, 0],             dtype=float )
ey = np.array( [0, 0, 0, 0, 0, 0],             dtype=float )

#define error values in that case arbitrary
for i in range( ey.size ):
    ey[i] = 0.05*y[i]

#Define Graph object
gr = TGraphErrors( x.size, x, y, ex, ey )

c1.SetGridx()
c1.SetGridy()

gr.SetMarkerStyle(20)
gr.SetMarkerSize(1)

#user defined fit function
f1 = TF1('fitfun', '[0]*(1-exp(-x/[1]))', 0.5, 3)
#force paremeter 0 and 1 to initial values
f1.SetParameter(0,6)
f1.SetParameter(1,0.8)
#apply fit onto graph
gr.Fit(f1)
#fit information in graph
gStyle.SetOptFit(111)

gr.Draw('AP')

c1.Update()
