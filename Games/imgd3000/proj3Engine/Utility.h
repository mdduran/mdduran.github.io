#ifndef _UTILITY_H_
#define _UTILITY_H_


//System includes
#include <stdio.h>

//Engine includes
#include "Position.h"

namespace df{
	class Utility{
	public:
		Utility();
		~Utility();
		//Return a nicely-formatted time string: HH:MM:SS
		char *getTimeString();

		//Return true if two positions intersect
		bool positionsIntersect(Position p1, Position p2);
	};
}
#endif