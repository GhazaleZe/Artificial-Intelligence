% Use this editor as a MiniZinc scratch book
int: n;                                 % The number of queens.

array [1..n] of var 1..n: queen;

include "alldifferent.mzn";

constraint alldifferent(queen); 
constraint alldifferent(i in 1..n)(queen[i] + i);
constraint alldifferent(i in 1..n)(queen[i] - i);


solve satisfy;

output	[	if fix(queen[i]) = j then "Q " else "# " endif ++
 	           if j = n then "\n" else "" endif |	i, j in 1..n];