#ifndef _MANAGER_H_
#define _MANAGER_H_

#include <string>
#include "Event.h"

namespace df{
	class Manager{
	private:
		std::string type;//Manager type identifier
		bool is_started;//True when started successfully

	protected:
		//Set type identifier of manager
		void setType(std::string type);

	public:
		Manager();
		virtual ~Manager();

		//Get type identifier of Manager
		std::string getType() const;

		//Startup Mnaager
		//Return 0 if ok, else return a negative number
		virtual int startUp();

		//Shutdown manager
		virtual void shutDown();

		//Return true when startUp() was executed ok
		bool isStarted() const;

		//Send event to all objects
		//Return count of number of events sent.
		int onEvent(const Event *p_event) const;
	};
}
#endif