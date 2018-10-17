//Event source file
#include "Event.h"
//Constructor
Event::Event(){
	event_type = UNDEFINED_EVENT;
}
//Destructor
Event::~Event(){

}

//Set type
void Event::setType(std::string new_type){
	event_type = new_type;
}

//Get event type
std::string Event::getType() const{
	return event_type;
}

