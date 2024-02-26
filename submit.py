#!/gpfs/mnt/gpfs02/eic/jadam/packages/python/mypython/bin/python3

import os
from subprocess import Popen, PIPE

from hepmc_selector import hepmc_selector

#_____________________________________________________________________________
def main():

    #production output directory
    outdir = "/eic/u/ceska/gpfs/eic/simulation/output"
    os.system("mkdir -p "+outdir)

    #number of jobs
    njob = 2000

    #number of events per one job
    nev = 1000

    #input file
    infile = "/eic/u/ceska/gpfs/eic/simulation/beam_gas_ep_10GeV_foam_emin10keV_10Mevt_rotx.hepmc"

    #top package directory containing detector subdirectiories
    eic_top = "/eic/u/ceska/gpfs/eic"

    #eic-shell location
    eic_shell = "/eic/u/ceska"

    #--- end of configuration ---


    #selector for job inputs
    sel = hepmc_selector(infile)

    #condor submit command
    cmd = "executable = run_job.csh\n"
    cmd += "universe = vanilla\n"
    cmd += "getenv = True\n"

    for ijob in range(njob):

        print("Job:", ijob)

        #4-digit job id
        job_id = "{0:04d}".format(ijob)

        #job output directory
        job_dir = outdir+"/"+job_id
        os.system("mkdir -p "+job_dir)

        #job input hepmc file
        sel.get_n(nev, job_dir+"/input.hepmc")

        #submit command
        job_cmd = cmd + "arguments = "+str(nev)+" "+job_dir+" "+eic_top+" "+eic_shell+"\n"
        job_cmd += "output = "+job_dir+"/run.log\n"
        job_cmd += "error = "+job_dir+"/run.err\n"
        job_cmd += "queue\n"

        #print(job_cmd)

        #submit the job
        submit = Popen(["condor_submit", "-"], stdout=PIPE, stderr=PIPE, stdin=PIPE)
        out = submit.communicate(job_cmd.encode("utf-8"))

        #print(out)

    print("All done")

#main

#_____________________________________________________________________________
if __name__ == "__main__":

    main()

