//Utility.cpp
#include "Utility.h"
#include <time.h>

using namespace df;
Utility::Utility(){}
Utility::~Utility(){}
//Return a nicely-formatted time string: HH:MM:SS
char *Utility::getTimeString(){
	//String to return, made 'static' so it persists
	static char time_str[30];

	//System calls to get time
	time_t now;
	time(&now);
	struct tm *p_time = localtime(&now);

	//'02' gives two digits, '%d' for integers.
	sprintf(time_str, "%02d:%02d:%02d", p_time->tm_hour, p_time->tm_min, p_time->tm_sec);
	return time_str;
}

//Return true if two positions intersect
bool Utility::positionsIntersect(Position p1, Position p2){
	bool isIntersect = false;
	if ((p1.getX() == p2.getX()) && (p1.getY() == p2.getY())){
		isIntersect = true;
		return isIntersect;
	}
	else
		return isIntersect;
}