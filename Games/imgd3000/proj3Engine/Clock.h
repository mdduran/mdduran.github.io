#ifndef _CLOCK_H_
#define _CLOCK_H_


//The clock, for timing(such as in the game loop)
class Clock{
	private:
		long int previous_time;//Previous time delta() called (in microseconds)
	public:
		//Sets previous time to current time
		Clock();

		//Returns time elapsed since delta() was called, -1 if error
		//Units are in microseconds
		long int delta(void);

		//Return time elapsed since delta() was called, -1 if error.
		//Units are in microseconds
		long int split(void) const;
};
#endif