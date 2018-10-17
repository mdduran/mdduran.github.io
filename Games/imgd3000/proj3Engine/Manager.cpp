//Manager base class
#include "Manager.h"

#include "ObjectList.h"
#include "ObjectListIterator.h"
#include "WorldManager.h"
using namespace df;
//Contructor
Manager::Manager(){
	type = "";
	is_started = false;
}

//Destructor
Manager::~Manager(){
	shutDown();
}

//Sets the type to a manager
void Manager::setType(std::string type){
	type = "Manager";
}

//Get the type identifier of the manager
std::string Manager::getType() const{
	return Manager::type;
}

//Startup manager
//Return 0 if ok, else return a negative number
int Manager::startUp(){
	if (!is_started){
		is_started = true;
		return 0;
	}
	else{
		return -1;
	}
}

//Shutdown manager
void Manager::shutDown(){
	is_started = false;
}

//Returns true when startUp() was executed ok
bool Manager::isStarted() const{
	if (is_started){
		return true;
	}
	else{
		return false;
	}
}

//Send event to all objects.
//Return count of number of events sent
int Manager::onEvent(const Event *p_event) const{
	int count = 0;
	WorldManager &world_manager = WorldManager::getInstance();
	ObjectList allObjects = world_manager.getAllObjects();
	ObjectListIterator li(&allObjects);
	while (!li.isDone()){
		li.currentObject()->eventHandler(p_event);
		li.next();
		count++;
	}
	return count;
}



