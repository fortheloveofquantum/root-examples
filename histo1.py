from ROOT import gROOT, TCanvas, TH1F, gRandom

gROOT.Reset()
c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

#define histogram object
h = TH1F("histo","random numbers",50,0,1);

for i in xrange(1000):
    r = gRandom.Uniform()
    h.Fill(r)

h.Draw()
c1.Update()
