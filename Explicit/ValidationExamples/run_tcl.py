import subprocess
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

path = 'Validation_of_Leap_Frog/PGA_510/Elastic/leap_frog_mass_damping/'
p = subprocess.Popen(f'{dir_path}/OpenSees dynamic.tcl', shell=True, stdout=subprocess.PIPE, cwd=f'{dir_path}/{path}')
stdout, stderr = p.communicate()
print(p.returncode)  # is 0 if success
