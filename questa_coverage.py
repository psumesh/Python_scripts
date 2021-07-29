import os

top_file_name = input("\t Enter your top file name e.g. top.sv \n")
top_module_name = input("Enter your top module instance name e.g top_wrapper")

#entering into questa command mode
os.system('vsim -c')

compile_ = 'vlog ' + top_file_name
os.system(compile_)

#coverage compilation
cov_comp = 'vlog -cover bcst ' + compile_
os.system(cov_comp)

#coverage simulation
cov_sim = 'vsim -novopt -coverage ' + top_module_name
os.system(cov_sim)

#run the simulation 
os.system('run -all')

#save the coverage in ucdb file
ucdb_fname = top_module_name + '.ucdb'
ucdb_cmd   = 'coverage save -assert -directive -cvg -codeall ' ucdb_fname
os.system(ucdb_cmd)
html_report = 'vcover report -html ' + ucdb_fname
os.system(html_report)




#For future use/Developer
"""

/////////////////////////////////////powershell////////////////////

qverilog +incdir+src+/tools/questasim_10.4e/verilog_src/uvm-1.1c/src +define+UVM_NO_DPI top.sv

///////////////questasim_10 UVM compile n simulate////////////////////////////////

vlog -sv top.sv +incdir+/questasim_10.4e/verilog_src/uvm-1.1c/src
vsim -sv_lib C:/questasim_10.4e/uvm-1.1c/win32/uvm_dpi -l run.log -novopt work.top

//////// ////////////////////////Verilog coverage//////////////////////////////////


vlog _TOP_.sv
vlog -cover bcst _TOP_.sv
vsim -novopt -coverage TOP_fifo
add wave *
-----------simulate --------
coverage report -html

////////////////////////////////////////UVM coverage/////////////////////////////////////////

vlog -coveropt 3 +cover +acc top.sv  +incdir+/questasim_10.4e/verilog_src/uvm-1.1c/src C:/questasim_10.4e/verilog_src/uvm-1.1c/src/uvm_pkg.sv


vsim -coverage top -sv_lib C:/questasim_10.4e/uvm-1.1c/win32/uvm_dpi -l run.log

///////////////////////////////////////////UVM assertion///////////////////////////////////

vlog +acc top.sv  +incdir+/questasim_10.4e/verilog_src/uvm-1.1c/src C:/questasim_10.4e/verilog_src/uvm-1.1c/src/uvm_pkg.sv

vsim -assertcover -assertdebug -gui -sv_lib C:/questasim_10.4e/uvm-1.1c/win32/uvm_dpi -l run.log work.top



///////////////////////////to merge coverage report//////////////////////////////////////

coverage save -assert -directive -cvg -codeAll test7.ucdb  //to save file as ucdb

vcover merge result.ucdb <file1>.ucdb <file2>.ucdb

vcover report -details -html result.ucdb 




////////////////////////////////SV ASSERTION////////////////////////////////////

vlog +acc _TOP_.sv
vsim -assertdebug TOP_fifo


////////////////////////////////////////SV Coverage ///////////////////////////////////

vlog -coveropt 3 +cover +acc _DUT_.sv _TOP_.sv
vsim -coverage -novopt TOP_fifo

"""

