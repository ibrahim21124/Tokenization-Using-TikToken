#include "rectangle.h"


Rectangle::Rectangle(int x, int y, int width, int height) :  mX(x)
                                                            ,mY(y)
                                                            ,mWidth(width)
                                                            ,mHeight(height)
{
}

Rectangle::~Rectangle()
{
}

bool Rectangle::isColliding(const Rectangle& rect2)
{
    return (mX < rect2.mX + rect2.mWidth &&
            mX + mWidth > rect2.mX &&
            mY < rect2.mY + rect2.mHeight &&
            mY + mHeight > rect2.mY);
}

