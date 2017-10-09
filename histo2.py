from ROOT import gROOT, TCanvas, TH1F, gRandom

gROOT.Reset()
c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

#define histogram object
h = TH1F("histo", "random numbers with error bars", 50, -3, 3);

for i in xrange(10000):
    r = gRandom.Gaus(0 ,1)
    h.Fill(r)

h.Draw('simple')
c1.Update()
