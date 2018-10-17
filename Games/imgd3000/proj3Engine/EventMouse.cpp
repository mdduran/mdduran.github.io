//Mouse event source file 
#include "EventMouse.h"
using namespace df;
//Constructor 
EventMouse::EventMouse(){
	setType(MOUSE_EVENT); 
	mouse_action = UNDEINED_MOUSE_ACTION;
	mouse_button = UNDEFINED_MOUSE_BUTTON;
	mouse_xy = Position(0, 0);
}

//Load mouse event's action.
void EventMouse::setMouseAction(EventMouseAction new_mouse_action){
	mouse_action = new_mouse_action;
}
//Get mouse event's action.
EventMouseAction EventMouse::getMouseAction() const{
	return mouse_action;
}
//Set mouse event's button
void EventMouse::setMouseButton(EventMouseButton new_mouse_button){
	mouse_button = new_mouse_button;
}
//Get mouse event's button
EventMouseButton EventMouse::getMouseButton() const{
	return mouse_button;
}
//Set mouse event's position
void EventMouse::setMousePosition(Position new_mouse_xy){
	mouse_xy = new_mouse_xy;
}
//Get mouse event's y position
Position EventMouse::getMousePosition() const{
	return mouse_xy;
}