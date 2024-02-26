
from pyHepMC3 import HepMC3 as hepmc

# Selector for consecutive samples out of an input hepmc file

#_____________________________________________________________________________
class hepmc_selector:

    #_____________________________________________________________________________
    def __init__(self, infile):

        #open the input
        self.inp = hepmc.ReaderAscii(infile)

    #_____________________________________________________________________________
    def get_n(self, n, outfile):

        #get a given number 'n' of events and put them to 'outfile'

        #create the output
        out = hepmc.WriterAscii(outfile, self.inp.run_info())

        #event loop
        for i in range(n):

            #input event
            evt = hepmc.GenEvent(hepmc.Units.GEV, hepmc.Units.MM)
            self.inp.read_event(evt)
            if( self.inp.failed() ): break

            #write to output
            out.write_event(evt)

