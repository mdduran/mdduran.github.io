#include "WorldManager.h"
#include "GraphicsManager.h"
#include "Utility.h"
#include "EventOut.h"
#include "EventStep.h"
#include "EventCollision.h"

using namespace df;
//helper function for detecting world boundary
//checks to see if the object is placed within the world boundary
bool inWorldXBoundary(Object *p_o);
bool inWorldYBoundary(Object *p_o);
//constructor 
WorldManager::WorldManager(){
	setType("WorldManager");
	//start up is called in game manager
}

WorldManager &WorldManager::getInstance(){
	static WorldManager world_manager;
	return world_manager;
}

//Startup game world (initialize everything to empty)
int WorldManager::startUp(){
	Manager::startUp();
	if (&Manager::isStarted){
		return 0;
	}
	else{
		return -1;
	}
}
//Shutdown game world (delete all game world objects)
void WorldManager::shutDown(){
	Manager::shutDown();	
	ObjectList ol = updates; //copy list so can delte during iteration
	ObjectListIterator li(&ol);
	for (li.first(); !li.isDone(); li.next()){
		markForDelete(li.currentObject());
	}
}

//Add object to world. Return 0 if ok, else -1
int WorldManager::insertObject(Object *p_o){
	if (!updates.isFull()){
		updates.insert(p_o);
		return 0;
	}
	else{
		return -1;
	}

}

//Remove object from world. Return 0 if ok, else -1
int WorldManager::removeObject(Object *p_o){
	if (!updates.isEmpty()){
		updates.remove(p_o);
		markForDelete(p_o);
		return 0;
	}
	else{
		return 1;
	}
}

//Return list of all objects
ObjectList WorldManager::getAllObjects() const{
	return updates;
}

//Indicate object is to be deleted at the end of current game loop
//Return 0 if ok, else -1
int WorldManager::markForDelete(Object *p_o){
	if (p_o != NULL){
		ObjectListIterator li(&deletions);
		while (!li.isDone()){
			if (li.currentObject() == p_o){//Object is already in the list
				return 0;
			}
			li.next();
		}
		//Object is not in list, so add
		deletions.insert(p_o);
		return 0;
	}
	else{
		return -1;
	}
}

//Update world
//Delete objects marked for deletion
void WorldManager::update(){

	//Update object positions based on their velocities
	//Iterate through all objects
	ObjectListIterator i(&updates);
	while (!i.isDone()){
		int x = i.currentObject()->getXVelocityStep();
		int y = i.currentObject()->getYVelocityStep();
		if (x != 0 || y != 0){ //object has moved
			Position old_position = i.currentObject()->getPosition();
			Position new_position(old_position.getX() + x, old_position.getY() + y);
			//Move object to new_position
			moveObject(i.currentObject(), new_position);
		}
		i.next();
	}
	ObjectListIterator li(&deletions);
	while (!li.isDone()){
		updates.remove(li.currentObject());
		delete li.currentObject();
		li.next();
	}
	deletions.clear();
}

//Draw all objects in the world
void WorldManager::draw(){
	ObjectListIterator li(&updates); //all game objects
	for (int alt = 0; alt <= MAX_ALTITUDE; alt++){
		while (!li.isDone()){
			if (li.currentObject()->getAltitude() == alt){
				li.currentObject()->draw();
			}
			li.next();
			
		}
		li.first();
	}
}

// Return list of Objects collided with at Position `where'.
// Collisions only with solid Objects.
// Does not consider if p_o is solid or not.
ObjectList WorldManager::isCollision(Object *p_o, Position where) const{
	
	//Make empty list
	ObjectList collision_list;
	Utility u;
	//Iterate through all objects
	ObjectListIterator i(&updates);
	while (!i.isDone()){
		Object *p_temp_o = i.currentObject();

		if (p_temp_o != p_o){ //Do not consider self
			//Same location and both solid?
			if (u.positionsIntersect(p_temp_o->getPosition(), where) && p_temp_o->isSolid()){
				collision_list.insert(p_temp_o);
			}
		}
		i.next();
	}
	return collision_list;
}
//if the objects x position is not within the game world, return false
bool inWorldXBoundary(Object *p_o){
	GraphicsManager &graphics_manager = GraphicsManager::getInstance();
	if ((p_o->getPosition().getX() <= graphics_manager.getHorizontal()) &&
		(p_o->getPosition().getX() >= 0)){
		return true;
	}
	else
		return false;
}

//if the object's y position is not within the game world, return false
bool inWorldYBoundary(Object *p_o){
	GraphicsManager &graphics_manager = GraphicsManager::getInstance();
	if ((p_o->getPosition().getY() <= graphics_manager.getVertical()) &&
		(p_o->getPosition().getY() >= 0)){
		return true;
	}
	else
		return false;
}
// Move Object.
// If no collision with solid, move ok else don't move.
// If p_go is Spectral, move ok.
// Return 0 if move ok, else -1 if collision with solid.
int WorldManager::moveObject(Object *p_o, Position where){
	bool do_move = true;
	GraphicsManager &graphics_manager = GraphicsManager::getInstance();
	//Need to be solid for collisions
	if (p_o->isSolid()){
		//Get collisions
		ObjectList list = isCollision(p_o, where);
		if (!list.isEmpty()){

			//Iterate over list
			ObjectListIterator i(&list);
			while (!i.isDone()){
				Object *p_temp_o = i.currentObject();

				//Create collision event 
				const EventCollision c(p_o, p_temp_o, where);
				//Send to both objects
				p_o->eventHandler(&c);
				p_temp_o->eventHandler(&c);

				//If both hard, then cannot move
				if ((p_o->getSolidness() == HARD) && (p_temp_o->getSolidness() == HARD)){
					do_move = false;
				}
				i.next();
			}//end iterate

			if (do_move == false){
				return -1;
			}
		}
	}
	bool wasInWorld = false;
	wasInWorld = inWorldXBoundary(p_o) && inWorldYBoundary(p_o);
	p_o->setPosition(where);
	if ((!inWorldXBoundary(p_o) || !inWorldYBoundary(p_o)) && wasInWorld) {
		EventOut ov;
		p_o->eventHandler(&ov);
	}
	return 0;
}
