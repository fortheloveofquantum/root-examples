from ROOT import gROOT, TCanvas, TH2F, gRandom

gROOT.Reset()
c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

h2d1 = TH2F("hist1","2d histo", 50,-10,10, 50,-10,10)
h2d2 = TH2F("hist2","2d histo", 50,-10,10, 50,-10,10)


#define histogram object
for i in xrange(10000):
    r1 = gRandom.Gaus(-2 , 1)  # mean=-2, sigma=1
    r2 = gRandom.Gaus(-2 , 1)
    h2d1.Fill( r1, r2 )
    r3 = gRandom.Gaus(2 , 2) # mean=-2, sigma= 2
    r4 = gRandom.Gaus(2 , 2)
    h2d2.Fill( r3, r4 )

h2d1.SetMarkerColor(2)
h2d1.SetMarkerColor(4)
h2d1.Draw()
h2d2.Draw('same')
c1.Update()
