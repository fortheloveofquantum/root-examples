from ROOT import gROOT, TCanvas, TH1F, gRandom

gROOT.Reset()
c1 = TCanvas( 'c1', 'Example with Formula', 200, 10, 700, 500 )

#define histogram object
h1 = TH1F("h1", "Uniform rnd", 50, 0.0, 1.0)
h2 = TH1F("h2", "Gaus rnd", 50, -3.0, 3.0)
h3 = TH1F("h3", "Exp rnd",50, 0.0, 1.0)
h4 = TH1F("h4", "BW rnd",50, -3.0, 3.0)
for i in xrange(10000):
    h1.Fill( gRandom.Uniform() )
    h2.Fill( gRandom.Gaus(0,1) )
    h3.Fill( gRandom.Exp(5) )
    h4.Fill( gRandom.BreitWigner(0,1) )

c1.Divide(2,2)
c1.cd(1); h1.Draw()
c1.cd(2); h2.Draw()
c1.cd(3); h3.Draw()
c1.cd(4); h4.Draw()

c1.Update()
