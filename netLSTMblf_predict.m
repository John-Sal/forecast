 


%function newoutput = netLSTMblf_predict(input)
%load netLSTMblf
%newoutput = predict(netLSTMblf, input);
%end 


function newoutput = netLSTMblf_predict(input)
load netLSTMblf
format longG

max_prev_load = max(input(1:24));
min_prev_load = min(input(1:24));
norm_prev_load = (input(1:24) - min_prev_load) ./ (max_prev_load - min_prev_load);

max_prev_temp = max(input(25:72));
min_prev_temp = min(input(25:72));
norm_prev_temp = (input(25:72) - min_prev_temp) ./ (max_prev_temp - min_prev_temp);



% y = (x - min) / (max - min)

comp_normalized_input = [norm_prev_load; norm_prev_temp; input(73:79)];
output = predict(netLSTMblf, comp_normalized_input);
newoutput = output*(max_prev_load - min_prev_load) + min_prev_load;

end 
