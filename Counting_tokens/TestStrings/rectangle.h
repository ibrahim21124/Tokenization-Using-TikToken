#ifndef RECTANGLE_H
#define RECTANGLE_H
#include <iostream>


class Rectangle
{
private:
     int mX;
     int mY; 
     int mWidth; 
     int mHeight;

public:
    Rectangle(int x, int y, int width, int height);
    ~Rectangle();

    bool isColliding(const Rectangle& rect1);
};



#endif