//Soruce file for the position class
#include "Position.h"
using namespace df;
//Create an object in a 2d location (x,y)
Position::Position(int init_x, int init_y){
	x = init_x;
	y = init_y;
}
//Default 2d location (x,y) location is (0,0)
Position::Position(){
	x = 0;
    y = 0;
}

//Get/set horizontal coordinate
void Position::setX(int new_x){
	x = new_x;
}

int Position::getX() const{
	return x;
}

//Get/set vertical coordinate
void Position::setY(int new_y){
	y = new_y;
}
int Position::getY() const{
	return y;
}

//Set horizontal and vertical coordinates
void Position::setXY(int new_x, int new_y){
	x = new_x;
	y = new_y;
}



