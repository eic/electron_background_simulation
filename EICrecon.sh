#!/bin/bash

source /opt/detector/epic-23.12.0/setup.sh
source /eic/u/ceska/tools/EICrecon/install/bin/eicrecon-this.sh

eicrecon -Pdd4hep:xml_files=/opt/detector/epic-23.12.0/share/epic/epic_craterlake.xml output.edm4hep.root
