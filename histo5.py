from ROOT import gROOT, TCanvas, TH2F, gRandom

gROOT.Reset()
c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

h2d = TH2F("hist","2d histo", 50,-4,4, 50,-4,4)


#define histogram object
for i in xrange(10000):
    r1 = gRandom.Gaus();
    r2 = gRandom.Gaus();
    h2d.Fill( r1, r2 )

h2d.Draw()
c1.Update()
