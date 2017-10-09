import numpy as np
from ROOT import gROOT, TCanvas, TGraph, gStyle, TH1F, gRandom, TF1

gROOT.Reset()
c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )
#define histogram object
h1 = TH1F("h","gauss dist",20,-3,3);
#define random gaus hist
for i in range( 10000 ):
    h1.Fill( gRandom.Gaus() )

#define fit function and TF1 object
fitfun = '[0]*exp(-0.5*(x-[1])/[2]*(x-[1])/[2])'
f1 = TF1("f", fitfun)
f1.SetParameter(0, 200.0)
f1.SetParameter(1, 0.1)
f1.SetParameter(2, 0.5)

#apply fit
h1.Fit(f1)
#fit information in graph
gStyle.SetOptFit(111)

h1.Draw()
c1.Update()
