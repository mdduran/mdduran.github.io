//Event header file
#ifndef _EVENT_H_
#define _EVENT_H_
#include <string>
const std::string UNDEFINED_EVENT = "df::undefined";

class Event{
	private:
		std::string event_type;//Holds event type

	public:
		//Create base event
		Event();
		//Destructor
		virtual ~Event();

		//Set type
		void setType(std::string new_type);

		//Get event type
		std::string getType() const;
};
#endif