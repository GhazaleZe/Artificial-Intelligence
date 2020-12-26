var float : x1;
var float : x2;
var float : x3;
var float : x4;
var float : x5;
var float : x6; /*free*/

constraint -5 * x1 + -2 * x2 + 0  * x3 + 1  * x4 + 1 * x5 >=x6; /*cloumn1*/
constraint  2 * x1 +  2 * x2 + 5  * x3 + 5  * x4 + 4 * x5 >=x6; /*cloumn2*/
constraint -1 * x1 + -5 * x2 + -2 * x3 + -5 * x4 + 4 * x5 >=x6; /*cloumn3*/
constraint -3 * x1 + -2 * x2 + 2  * x3 + 2  * x4 + 3 * x5 >=x6; /*cloumn4*/
constraint  4 * x1 +  3 * x2 + 4  * x3 + -1 * x4 + 4 * x5 >=x6; /*cloumn5*/
constraint  2 * x1 + -3 * x2 + 0  * x3 + -2 * x4 + 0 * x5 >=x6; /*cloumn6*/
constraint -5 * x1 + -2 * x2 + -1 * x3 + 3  * x4 + 2 * x5 >=x6; /*cloumn7*/
constraint x1 + x2 + x3 + x4 + x5=1;
constraint x1>=0;
constraint x2>=0;
constraint x3>=0;
constraint x4>=0;
constraint x5>=0;

solve maximize x6;