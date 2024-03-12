#!/usr/local/bin/tcsh

#job arguments
set nev = ${1}
set outdir = ${2}
set eic_top = ${3}
set eic_shell = ${4}

touch ${outdir}/SUCC

echo "Starting the job"
echo "Hostname:", `hostname`

#job submit directory
set jobdir = `pwd`

#move to job directory
cd ${_CONDOR_SCRATCH_DIR}

#load simulation macro
cp ${jobdir}/run_epic_template.sh .
cat run_epic_template.sh | sed "s%__NEV__%${nev}%g" | sed "s%__EIC_TOP__%${eic_top}%g" > run_epic.sh
echo "--- Simulation macro ---"
cat run_epic.sh
echo "----------------------"

echo
echo "Copying files..."
#get input hepmc file
cp ${outdir}/input.hepmc .

#compactFile
cp ${eic_top}/epic/epic_craterlake.xml .

#magnetic field
cp -r ${eic_top}/epic/fieldmaps .

#calibrations
cp -r ${eic_top}/epic/calibrations .

#EICrecon script
cp /eic/u/ceska/gpfs/electron_background_simulation/EICrecon.sh .
echo "Files copied!"
echo "--- Recon macro ---"
cat EICrecon.sh
echo "----------------------"
echo

echo "--- Local directory ---"
pwd
ls -alh
echo "-----------------------"

#run the EPIC
echo "Running EPIC in eic-shell"
echo "echo begin" | ${eic_shell}/eic-shell > run.log
cat run_epic.sh | ${eic_shell}/eic-shell >> run.log
echo "echo done" | ${eic_shell}/eic-shell >> run.log
cat EICrecon.sh | ${eic_shell}/eic-shell >> run.log

#attach the log
cat run.log

ls -alh

#put output to the output directory
mv output.edm4hep.root ${outdir}"/output.edm4hep.root"
mv podio_output.root ${outdir}"/podio_output.root" 

echo "All done"
