//Source file for Clock
//Engine Includes
#include "Clock.h"
//System includes
#include <Windows.h>

Clock::Clock(){
	//set previous time to current time
	SYSTEMTIME current_st;
	GetSystemTime(&current_st);
	long current_microsec = (current_st.wMinute * 60 *1000)
		+ (current_st.wSecond * 1000)
		+ (current_st.wMilliseconds);
	//set the previous time to the current time
	previous_time = current_microsec;
}

//Returns time elapsed since delta() was called, -1 if error
//Units are in microseconds
long int Clock::delta(void){
	if (previous_time != 0){
		SYSTEMTIME after_st;
		//Do stuff...
		GetSystemTime(&after_st);
		//Compute Elapsed time in microseconds
		long after_microsec = (after_st.wMinute * 60 * 1000)
			+ (after_st.wSecond * 1000)
			+ (after_st.wMilliseconds);
		long int elapsed_time = after_microsec - previous_time;
		//sets previous time to the current time
		previous_time = after_microsec;
		//returns the delta value
		return elapsed_time;
	}
	else{
		return -1;
	}
}

//Return time elapsed since delta() was called, -1 if error.
//Units are in microseconds
long int Clock::split(void) const {
	if (previous_time != 0){
		SYSTEMTIME after_st;
		//Do stuff...
		GetSystemTime(&after_st);
		//Compute Elapsed time in microseconds
		long after_microsec = (after_st.wMinute * 60 * 1000)
			+ (after_st.wSecond * 1000)
			+ (after_st.wMilliseconds);
		long int elapsed_time = after_microsec - previous_time;
		//returns the delta value
		return elapsed_time;
	}
	else{
		return -1;
	}
}