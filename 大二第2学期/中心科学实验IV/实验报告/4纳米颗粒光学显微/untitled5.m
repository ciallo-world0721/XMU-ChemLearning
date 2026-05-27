clc,clear
trace = xlsread("./src/1.xlsx");
trace = trace .* 246.8; % nm
[MSD,D,alpha,myfit,t] = Cal_coefficient(trace,150)
