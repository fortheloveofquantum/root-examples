import numpy as np
from ROOT import gROOT, TCanvas, TGraph

gROOT.Reset()
c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

#define x and y dataset
x = np.array( [0, 0.1 , 0.2 ,  0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] )
y = np.array( [0, 0.01, 0.04, 0.09, 0.16, 0.25, 0.36, 0.49, 0.64, 0.81, 1] )

#Define Graph object
gr = TGraph( x.size, x, y )

c1.SetGridx()
c1.SetGridy()
gr.Draw('AC*')
c1.Update()
