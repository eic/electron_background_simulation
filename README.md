# electron_background_simulation
Code for production of edm4hep files from the hepmc3 generated events

## paths
The code includes several paths that need to be updated in order to properly run it.
### submit.py
- line 12 and 13 - output directory of the simulation
- line 22 - location of the hepmc3 input file; the most recent one can be found in the [Wiki](https://wiki.bnl.gov/EPIC/index.php?title=Electron_Beam_Gas).
- line 25 - location of the top ePIC directory
- line 28 - location of the user's `eic-shell`

## variables
Several variables can be changed to modify the code`s behaviour
- `submit.py`
  - line 16 - number of jobs
  - line 19 - number of events per job
- `run_job.csh`
  - line 33 - detector geometry, which is grabbed from the top ePIC directory
- `run_epic_template.csh`
  - line 10 - detector geometry as set in the `run_job.csh` file

## running the code
To run the code, execute the `submit.py` OUTSIDE of the `eic-shell`, as it utilises a dedicated 

## troubleshooting
in case of any questions please contact me at <jakub.ceska@fjfi.cvut.cz>
