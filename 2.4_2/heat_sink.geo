//+
Point(1) = {0, -0, 0, 1.0};
//+
Point(2) = {0, 3, 0, 1.0};
//+
Point(3) = {0.5, 3, 0, 1.0};
//+
Point(4) = {0.5, 0.7, 0, 1.0};
//+
Point(5) = {1.5, 0.7, 0, 1.0};
//+
Point(6) = {1.5, 3, 0, 1.0};
//+
Point(7) = {2, 3, 0, 1.0};
//+
Point(8) = {2, 0.7, 0, 1.0};
//+
Point(9) = {3, 0.7, 0, 1.0};
//+
Point(10) = {3, 3, 0, 1.0};
//+
Point(11) = {3.5, 3, 0, 1.0};
//+
Point(12) = {3.5, 0.7, 0, 1.0};
//+
Point(13) = {4.5, 0.7, 0, 1.0};
//+
Point(14) = {4.5, 3, 0, 1.0};
//+
Point(15) = {5, 3, 0, 1.0};
//+
Point(16) = {5, 0.7, 0, 1.0};
//+
Point(17) = {6, 0.7, 0, 1.0};
//+
Point(18) = {6, 3, 0, 1.0};
//+
Point(19) = {6.5, 3, 0, 1.0};
//+
Point(20) = {6.5, 0.7, 0, 1.0};
//+
Point(21) = {7.5, 0.7, 0, 1.0};
//+
Point(22) = {7.5, 3, 0, 1.0};
//+
Point(23) = {8, 3, 0, 1.0};
//+
Point(24) = {8, 0.7, 0, 1.0};
//+
Point(25) = {9, 0.7, 0, 1.0};
//+
Point(26) = {9, 3, 0, 1.0};
//+
Point(27) = {9.5, 3, 0, 1.0};
//+
Point(28) = {9.5, -0, 0, 1.0};
//+
Line(1) = {1, 2};
//+
Line(2) = {2, 3};
//+
Line(3) = {3, 4};
//+
Line(4) = {4, 5};
//+
Line(5) = {5, 6};
//+
Line(6) = {6, 7};
//+
Line(7) = {7, 8};
//+
Line(8) = {8, 9};
//+
Line(9) = {9, 10};
//+
Line(10) = {10, 11};
//+
Line(11) = {11, 12};
//+
Line(12) = {12, 13};
//+
Line(13) = {13, 14};
//+
Line(14) = {14, 15};
//+
Line(15) = {15, 16};
//+
Line(16) = {16, 17};
//+
Line(17) = {17, 18};
//+
Line(18) = {18, 19};
//+
Line(19) = {19, 20};
//+
Line(20) = {20, 21};
//+
Line(21) = {21, 22};
//+
Line(22) = {22, 23};
//+
Line(23) = {23, 24};
//+
Line(24) = {24, 25};
//+
Line(25) = {25, 26};
//+
Line(26) = {26, 27};
//+
Line(27) = {27, 28};
//+
Line(28) = {1, 28};
//+
Physical Curve("bottom", 29) = {28};
//+
Physical Curve("left", 30) = {1};
//+
Physical Curve("right", 31) = {27};
//+
Physical Curve("top", 32) = {2, 6, 10, 14, 18, 22, 26, 4, 8, 12, 16, 20, 24};
//+
Physical Curve("inner", 33) = {3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25};
//+
Curve Loop(1) = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, -28};
//+
Plane Surface(1) = {1};