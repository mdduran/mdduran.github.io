//Keyboard event source file
#include "EventKeyboard.h"
using namespace df;
//Constructor
EventKeyboard::EventKeyboard(){
	setType(KEYBOARD_EVENT);
	key_val = Keyboard::UNDEFINED_KEY;
	keyboard_action = UNDEFINED_KEYBOARD_ACTION;
}

//Set key in event
void EventKeyboard::setKey(Keyboard::Key new_key){
	key_val = new_key;
}

//Get key from event
Keyboard::Key EventKeyboard::getKey() const{
	return key_val;
}

//Set keyboard event action.
void EventKeyboard::setKeyboardAction(EventKeyboardAction new_action){
	keyboard_action = new_action;
}

//Get keyboard action 
EventKeyboardAction EventKeyboard::getKeyboardAction() const{
	return keyboard_action;
}