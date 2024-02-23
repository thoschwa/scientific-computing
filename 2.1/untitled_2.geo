// Gmsh project created on Thu Feb 22 15:18:07 2024
SetFactory("OpenCASCADE");
//+
Point(1) = {-1, -0, 0, 1.0};
//+
Point(2) = {1, -0, 0, 1.0};
//+
Point(3) = {1, 1, 0, 1.0};
//+
Point(4) = {-1, 1, 0, 1.0};
//+
Point(5) = {0.2, -1, 0, 1.0};
//+
Point(6) = {0, 1.5, 0, 1.0};
//+
Recursive Delete {
  Point{5}; 
}
//+
Line(1) = {4, 6};
//+
Line(2) = {6, 3};
//+
Line(3) = {2, 3};
//+
Line(4) = {1, 4};
//+
Line(5) = {1, 2};
//+
Physical Curve("surface", 6) = {1, 2, 3, 5, 4};
//+
Curve Loop(1) = {1, 2, -3, -5, 4};
//+
Plane Surface(1) = {1};
//+
Physical Surface("surface", 7) = {1};
