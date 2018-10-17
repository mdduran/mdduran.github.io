//Collision event source file
#include "EventCollision.h"

using namespace df;

//Create collision event at (0,0) with obj1 and obj2 NULL
EventCollision::EventCollision(){
	setType(COLLISION_EVENT);
	pos.setXY(0,0);
	p_obj1 = NULL;
	p_obj2 = NULL;
}

//Create collision event between o1 and o2 at position p.
//Object o1 'caused' collision by moving object o2.
EventCollision::EventCollision(Object *p_o1, Object *p_o2, Position p){
	setType(COLLISION_EVENT);
	pos = p;
	p_obj1 = p_o1;
	p_obj2 = p_o2;
}

//Return object that caused collision
Object *EventCollision::getObject1() const{
	return p_obj1;
}

//Set object that caused collision.
void EventCollision::setObject1(Object *p_new_o1){
	p_obj1 = p_new_o1;
}

//Return object that was collided with
Object *EventCollision::getObject2() const{
	return p_obj2;
}

//Set object that was collided with
void EventCollision::setObject2(Object *p_new_o2){
	p_obj2 = p_new_o2;
}

//Return position of the collision
Position EventCollision::getPosition() const{
	return pos;
}

//Set position of collision
void EventCollision::setPosition(Position new_pos){
	pos = new_pos;
}