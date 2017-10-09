import numpy as np
from ROOT import gROOT, TCanvas, TGraph, gStyle

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
#polinomial fit
gr.Fit('pol1')
#fit information in graph
gStyle.SetOptFit(111)

gr.Draw('AP')

c1.Update()
