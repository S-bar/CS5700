set term png
set output "exp2_NewReno_Reno_droprate.png"
set title "Experienmnet 2 NewReno-Reno Drop Rate"
set xlabel "CBR[Mbps]"
set ylabel "Drop Rate"
set grid
set key left
plot 'exp2_NewReno_Reno_droprate.dat' using 1:2 with lp pt 2 lw 1 linecolor rgb "red" title 'NewReno',\
 'exp2_NewReno_Reno_droprate.dat' using 1:3 with lp pt 8 lw 1 lt 1 linecolor rgb "blue" title 'Reno'
