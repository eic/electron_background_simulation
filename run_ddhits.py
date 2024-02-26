#!/usr/local/bin/python3

from glob import glob

import sys
sys.path.append("/direct/eic+u/jadam/Athena/athena_particle_counter/macro/ddhits")

from analysis import analysis

#_____________________________________________________________________________
def main():

    #geometry
    compact = "/eic/u/jadam/Athena/athena_particle_counter/athena_with_fe.xml"

    #input
    indir = "/gpfs/mnt/gpfs02/eic/jadam/athena/beam-gas/cnt1a"
    inlist = glob(indir+"/????/"+"output.root")

    outfile = indir+"/ddhits_pass3.root"

    ana = analysis(outfile)
    ana.set_input(inlist)

    ana.load_detectors(compact)

    ana.event_loop()



#_____________________________________________________________________________
if __name__ == "__main__":

    main()


