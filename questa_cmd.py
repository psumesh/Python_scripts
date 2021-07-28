#creater : Umesh Prasad
# email  : spumesh@outlook.com
# github : psumesh


import os

top_fname = 'abc.sv'

os.system('vsim -c')   #enter into questa

start_compile = 'vlog ' + top_fname
os.system(start_compile)              #compile 

#simulate
sim = 'vlog -novopt work.top'
os.system(sim)

#add all waveform including submodules
waveforms = 'add wave -r *'
os.system(waveforms)
os.system('run 1000')

#for coverage
os.system('quit -sim')
os.system(start_compile)
compile_cover = 'vlog -cover bcst ' + top_fname
os.system(compile_cover)
os.system(waveforms)
os.system('run 10000')

#in sv for diffrent test cases with program files
os.system('coverage save -assert -directive -cvg -codeAll result1.ucdb')
#for html coverage report
os.system('vcover report -details -html result1.ucdb')

#SV assertions
assert_cmd = 'vlog +acc ' + top_fname
os.system(assert_cmd)
os.system('vsim -assertdebug top_module')   #where top_module is the top top wrapper module of dut & testbench


