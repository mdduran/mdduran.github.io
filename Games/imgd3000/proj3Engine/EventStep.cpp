//Event step source code
#include "EventStep.h"
//Default constructor 
EventStep::EventStep(){
	Event::setType(STEP_EVENT);
}

//Constructor with initial step count 
EventStep::EventStep(int init_step_count){
	Event::setType(STEP_EVENT);
	step_count = init_step_count;
}

//Set step count
void EventStep::setStepCount(int new_step_count){
	step_count = new_step_count;
}

//Get step count
int EventStep::getStepCount() const{
	return step_count;
}