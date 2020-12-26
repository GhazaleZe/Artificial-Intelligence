var float : y1;
var float : y2;
var float : y3;
var float : y4;
var float : y5;
var float : y6;
var float : y7;
var float : y8; /*free*/

constraint -5 * y1 + 2 * y2 + -1 * y3 + -3 * y4 +  4 * y5 +  2 * y6 + -5 * y7 <= y8;
constraint -2 * y1 + 2 * y2 + -5 * y3 + -2 * y4 +  3 * y5 + -3 * y6 + -2 * y7 <= y8;
constraint  0 * y1 + 5 * y2 + -2 * y3 +  2 * y4 +  4 * y5 +  0 * y6 + -1 * y7 <= y8;
constraint  1 * y1 + 5 * y2 + -5 * y3 +  2 * y4 + -1 * y5 + -2 * y6 +  3 * y7 <= y8;
constraint  1 * y1 + 4 * y2 +  4 * y3 +  3 * y4 +  4 * y5 +  0 * y6 +  2 * y7 <= y8;

constraint y1 + y2 + y3 + y4 + y5 + y6 + y7=1;
constraint y1>=0;
constraint y2>=0;
constraint y3>=0;
constraint y4>=0;
constraint y5>=0;
constraint y6>=0;
constraint y7>=0;

solve minimize y8;
