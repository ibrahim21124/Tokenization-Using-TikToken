#include <catch2/catch_test_macros.hpp>
#include "rectangle.h"

TEST_CASE("Colliding rectangles") {
  Rectangle rect1 = {0, 0, 10, 10};
  Rectangle rect2 = {5, 5, 10, 10};
  
  REQUIRE(isColliding(rect1, rect2));
}

TEST_CASE("Non-colliding rectangles") {
  Rectangle rect1 = {0, 0, 10, 10};
  Rectangle rect2 = {20, 20, 10, 10};
  
  REQUIRE_FALSE(isColliding(rect1, rect2));  
}

TEST_CASE("Partially overlapping rectangles") {
  Rectangle rect1 = {0, 0, 10, 10};
  Rectangle rect2 = {5, 0, 10, 10};
  
  REQUIRE(isColliding(rect1, rect2));
}

TEST_CASE("Touching rectangles") {
  Rectangle rect1 = {0, 0, 10, 10};
  Rectangle rect2 = {10, 0, 10, 10};
  
  REQUIRE_FALSE(isColliding(rect1, rect2));
}
