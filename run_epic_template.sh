
#EPIC libraries
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:__EIC_TOP__/epic/install/lib:__EIC_TOP__/epic/install/lib
export DETECTOR_PATH=__EIC_TOP__/epic/install/share/epic


#simulation command
npsim \
  --inputFiles input.hepmc \
  --compactFile epic_craterlake.xml \
  --random.seed 123 \
  --physics.list FTFP_BERT \
  --field.eps_min 5e-06 \
  --field.eps_max 1e-04 \
  --numberOfEvents __NEV__ \
  --outputFile output.edm4hep.root

