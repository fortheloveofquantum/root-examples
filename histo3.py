from ROOT import gROOT, TCanvas, TH1F, gRandom

gROOT.Reset()
c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

#define histogram object
h1 = TH1F("histo", "random numbers superimposing", 50, -3, 3);
h2 = TH1F("histo", "random numbers superimposing", 50, -3, 3);

for i in xrange(10000):
    h1.Fill( gRandom.Gaus(0 ,1)     )
    h2.Fill( gRandom.Uniform(-3 ,3) )

h1.SetFillColor(2)

h1.Draw()
h2.Draw('same')
c1.Update()
