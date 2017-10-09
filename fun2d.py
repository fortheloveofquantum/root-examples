from ROOT import gROOT, TCanvas, TF2

gROOT.Reset()
c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

#
# Create a one dimensional function and draw it
#
fun2d = TF2( 'fun2d', 'x*x+y*y', -2, 2, -2, 2 )
c1.SetGridx()
c1.SetGridy()
fun2d.Draw('surf')
c1.Update()
