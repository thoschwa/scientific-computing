//+
Point(1) = {0, 2, 0, 1.0};
//+
Point(2) = {0, 0, 0, 1.0};
//+
Point(3) = {2, 0, 0, 1.0};
//+
Point(4) = {2, 2, 0, 1.0};
//+
Point(5) = {0.5, 0.5, 0, 1.0};
//+
Point(6) = {0.5, 1.5, 0, 1.0};
//+
Point(7) = {1.5, 1.5, 0, 1.0};
//+
Point(8) = {1.5, 0.5, -0, 1.0};
//+
Bezier(1) = {5, 6, 7};
//+
Line(2) = {8, 5};
//+
Line(3) = {7, 8};
//+
Line(4) = {2, 3};
//+
Line(5) = {2, 1};
//+
Line(6) = {1, 4};
//+
Line(7) = {3, 4};
//+
Curve Loop(1) = {5, 6, -7, -4};
//+
Curve Loop(2) = {2, 1, 3};
//+
Plane Surface(1) = {1, 2};
//+
Physical Curve("top", 8) = {6};
//+
Physical Curve("left", 9) = {5};
//+
Physical Curve("right", 10) = {7};
//+
Physical Curve("bottom", 11) = {4};
//+
Physical Curve("interior", 12) = {1, 3, 2};
//+
MeshSize {6} = 0.05;
