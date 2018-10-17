//EventStep header file
#ifndef _EVENTSTEP_H_
#define _EVENTSTEP_H_

#include "Event.h"
const std::string STEP_EVENT = "df::step";

class EventStep : public Event{
	private:
		int step_count; //iterate number of game loops

	public:
		//Default constructor
		EventStep();

		//Constructor with initial step count
		EventStep(int init_step_count);

		//Set step count
		void setStepCount(int new_step_count);

		//Get step count
		int getStepCount() const;
};

#endif