import numpy as np
from ROOT import gROOT, TCanvas, TGraph

gROOT.Reset()
c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

#define x and y dataset
x = np.linspace(0, 2, 20)
y = x*x

#Define Graph object
gr = TGraph( x.size, x, y )

c1.SetGridx()
c1.SetGridy()
gr.Draw('AC*')
c1.Update()
