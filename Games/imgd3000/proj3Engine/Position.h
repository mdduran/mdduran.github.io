#ifndef _POSITION_H_
#define _POSITION_H_
namespace df{
	class Position{
	private:
		int x; //Horizontal coordinate in 2d world
		int y; //Vertical coordinate in 2d world

	public:
		//Create an object at 2d location (x,y)
		Position(int init_x, int init_y);

		//Default 2d (x,y) location is (0,0)
		Position();

		//Get/set horizontal coordinate
		void setX(int new_x);
		int getX() const;

		//Get/set vertical coordinate 
		void setY(int new_y);
		int getY() const;

		//Set horizontal & vertical coordinates
		void setXY(int new_x, int new_y);
	};
}
#endif