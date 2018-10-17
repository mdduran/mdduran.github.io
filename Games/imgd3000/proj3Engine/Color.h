#ifndef _COLOR_H_
#define _COLOR_H_
//Colors Dragonfly recognizes
enum Color{
	BLACK = 0, 
	RED,
	GREEN,
	YELLOW,
	BLUE,
	MAGENTA,
	CYAN,
	WHITE,
};

//If color not specified, will use this.
const Color COLOR_DEFAULT = WHITE;
#endif