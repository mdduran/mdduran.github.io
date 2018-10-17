//Engine includes
#include "LogManager.h"
#include "GameManager.h"
#include "GraphicsManager.h"
#include "WorldManager.h"
#include "InputManager.h"
#include "ObjectList.h"
#include "Position.h"
#include "Object.h"
#include "ObjectListIterator.h"
#include "Clock.h"

//System include
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <Windows.h>


using namespace df;

int testInput();

int main(int argc, char *argv[]){
	LogManager &log_manager = df::LogManager::getInstance();
	GameManager &game_manager = df::GameManager::getInstance();
	WorldManager &world_manager = df::WorldManager::getInstance();
	GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
	InputManager &input_manager = df::InputManager::getInstance();
	//start up graphics manager
	graphics_manager.startUp();
	//start up game manager
	game_manager.startUp();
	if (game_manager.isStarted())
		log_manager.writeLog("Game Manager has started up\n");
	world_manager.startUp();
	if (world_manager.isStarted())
		log_manager.writeLog("World Manager has started up.\n");
	//set flush of log file
	log_manager.setFlush(true);
	//test log output with one argument
	log_manager.writeLog(
		"Test 1 has been completed\n");
	//test log output with two arguments
	log_manager.writeLog(
		" Play with %s\n", "one variable");
	//test log output with three arguments
	log_manager.writeLog(
		"In the y axis there are %d units and in the x axis there are %f units\n", 20, 15.52);

	//testing clock by getting time
	Clock *clock = new Clock;
	clock->delta();
	//see time here with log
	log_manager.writeLog(
		"First Time: %ld \n", clock->delta());
	int sleep_time;
	sleep_time = 20;//sleep for 200 microseconds, or 20 ms
	long int loop_time;
	loop_time = clock->split();
	Sleep(sleep_time - loop_time);
	//see next time here with log
	log_manager.writeLog(
		"Second Time: %ld \n", clock->delta());

	

	//Test creation of position
	Position testPos;
	testPos.setX(5);
	testPos.setY(6);
	log_manager.writeLog(
		"The x position is %d and the y position is %d\n",
		testPos.getX(), testPos.getY());
	//see if setXY works
	testPos.setXY(10, 5);
	log_manager.writeLog("The new x pos is %d and the new y pos is %d\n",
		testPos.getX(), testPos.getY());
	//Test creation of object
	Object testObj;
	testObj.setId(12);
	testObj.setPosition(testPos);
	testObj.setType("test");
	log_manager.writeLog("Object id is %d, Object x is %d, Object Y is %d, and Object type is '%s' \n",
		testObj.getId(), testObj.getPosition().getX(), testObj.getPosition().getY(), testObj.getType().c_str());
	//Test adding to object list
	ObjectList testList;
	Object *p_testobj = new Object;
	p_testobj->setId(42);
	p_testobj->setPosition(testPos);
	p_testobj->setType("object");
	testList.insert(p_testobj);//it actually adds
	if (testList.insert(p_testobj) == 0){
		log_manager.writeLog("Added object successfully\n");
	}
	//Create more objects to fill list
	Object *p_testobj2 = new Object;
	Object *p_testobj3 = new Object;
	Object *p_testobj4 = new Object;
	Object *p_testobj5 = new Object;
	p_testobj2->setId(21);
	p_testobj2->setPosition(testPos);
	p_testobj2->setType("object2");

	//obj 3
	p_testobj3->setId(22);
	p_testobj3->setPosition(testPos);
	p_testobj3->setType("object3");
	//obj 4
	p_testobj4->setId(23);
	p_testobj4->setPosition(testPos);
	p_testobj4->setType("object4");
	//obj 5
	p_testobj5->setId(24);
	p_testobj5->setPosition(testPos);
	p_testobj5->setType("object5");

	//see if you can add another object to the list
	Object *p_testobj6 = new Object;
	testList.insert(p_testobj2);
	testList.insert(p_testobj3);
	testList.insert(p_testobj4);
	testList.insert(p_testobj5);
	testList.insert(p_testobj6); //should fail
	if (testList.insert(p_testobj6) == -1){
		log_manager.writeLog("Failed to insert obj 6\n");
	}
	//Test removing from the object list
	testList.remove(p_testobj);
	if (testList.remove(p_testobj) == 0){
		log_manager.writeLog("Removed object successfully\n");
	}

	//Test creation of object list iterator
	ObjectListIterator testIterator(&testList);
	while (!testIterator.isDone()){
		log_manager.writeLog("On %s\n", testIterator.currentObject()->getType().c_str());
		testIterator.next();
	}

	//Test Event creation
	Event e;
	e.setType("TestEvent");
	log_manager.writeLog("The event type is %s\n", e.getType().c_str());
	//See if null event returns undefined event
	Event e2;
	log_manager.writeLog("The event type is %s\n", e2.getType().c_str());
	
	ObjectList allObjects = world_manager.getAllObjects();
	ObjectListIterator checkWorldObjects(&allObjects);

	for (checkWorldObjects.first(); !checkWorldObjects.isDone(); checkWorldObjects.next()){
		log_manager.writeLog("Iterated through %s\n", checkWorldObjects.currentObject()->getType().c_str());
	}


	//test to see if graphics manager functionality is working
	graphics_manager.drawCh(Position(10, 5), '*', WHITE);
	graphics_manager.swapBuffers();
	Sleep(100);
	graphics_manager.shutDown();
	
	//testing input manager
	
	testInput();

	//game_manager.run();
	
	//game_manager.shutDown();



}
//return true if works, return false if it does not
int testInput(){
	LogManager &log_manager = df::LogManager::getInstance();
	GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
	InputManager &input_manager = df::InputManager::getInstance();
	GameManager &game_manager = df::GameManager::getInstance();
	game_manager.startUp();
	if (graphics_manager.startUp() == 1 && input_manager.startUp() == 1){
		log_manager.writeLog("All managers have started");
	}
	EventKeyboard ek;
	EventMouse em;
	Event go;
	Object game_over = Object::Object();
//	game_over.eventHandler(go);
	
	game_manager.run();
	//if ()
	log_manager.writeLog("Type of events sent: %s\n", ek.getType().c_str());//should be keyboard
	log_manager.writeLog("Key last pressed: %d\n", ek.getKey());
	log_manager.writeLog("Type of events sent: %s\n", em.getType().c_str());//should be mouse
	log_manager.writeLog("Key last pressed: %d\n", em.getMouseButton());
	game_manager.shutDown(); 
	return 0;


}