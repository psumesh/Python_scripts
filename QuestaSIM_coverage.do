# QuestSIM Coverage

vlog top.sv                              #top file name
vlog -cover bcst top.sv                  #top file name
vsim -novopt -coverage top               #top module name
add wave *
run -all
coverage save -assert -drective -cvg -codeAll coverage_results.ucdb
vcover report -html coverage_results.ucdb