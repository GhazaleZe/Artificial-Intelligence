% question1
int: teacher = 3;
% 1=A , 2=B ,3=C
var 3..3: c1;  
var 2..3: c2;  
var 1..3: c3; 
var 1..3: c4;
var 2..3: c5; 

constraint c1 != c2;
constraint c2 != c3;
constraint c2 != c4;
constraint c3 != c4;
constraint c3 != c5;
constraint c4 != c5;

solve satisfy;

output ["course1=", show(c1), "\ncourse2=", show(c2), 
        "\ncourse3=", show(c3), "\n", "course4=", show(c4),  
        "\ncourse5=", show(c5), "\n"];
