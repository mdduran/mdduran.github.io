#ifndef _EVENTOUT_H_
#define _EVENTOUT_H_
#include "Event.h"

namespace df {

	const std::string OUT_EVENT = "df::out";

	class EventOut : public Event{

	public:
		EventOut();
	};
}
#endif