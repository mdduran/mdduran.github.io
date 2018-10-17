//InputManager source file
#include "InputManager.h"
#include "GraphicsManager.h"
#include "LogManager.h"
#include "WorldManager.h"
#include "ObjectListIterator.h"
#include "EventKeyboard.h"
#include "EventMouse.h"

using namespace df;

//Constructor
InputManager::InputManager(){
	setType("InputManager");
}

//Get the one and only instance of the input manager
InputManager &InputManager::getInstance(){
	static InputManager input_manager;
	return input_manager;
}

//Get window ready to capture input
//Return 0 if ok, else return negative number
int InputManager::startUp(){
	GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
	if (!graphics_manager.isStarted()){
		return -1;
	}
	
	graphics_manager.getWindow();
	graphics_manager.getWindow()->setKeyRepeatEnabled(false);
	Manager::startUp();
	return 0;
}

//Revert back to normal window mode
void InputManager::shutDown(){
	GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
	graphics_manager.getWindow()->setKeyRepeatEnabled(true);
	Manager::shutDown();
}

//GetInput from the keyboard and mouse
//Pass event along to all objects
void InputManager::getInput(){
	GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
	LogManager &log_manager = df::LogManager::getInstance();
	//Check past window events.
	sf::Event event;
	//Keyboard::Key key;
	
	sf::RenderWindow *p_window = graphics_manager.getWindow();
	
	while (p_window->pollEvent(event)){
		//key was pressed
			if (event.type == sf::Event::KeyPressed){
				EventKeyboard e_keyboard;
				for (int i = sf::Keyboard::Key::Unknown; i < sf::Keyboard::KeyCount; i++){
					if (sf::Keyboard::isKeyPressed((sf::Keyboard::Key)i)){
						e_keyboard.setKey(convertSFKey((sf::Keyboard::Key)i));
					//	if (event.KeyPressed)
							e_keyboard.setKeyboardAction(EventKeyboardAction::KEY_PRESSED);
						log_manager.writeLog("Key:%d is down", i);
					}
				}
				onEvent(&e_keyboard);
			}

			else if (event.type == sf::Event::KeyReleased){
				EventKeyboard e_keyboard;
				for (int i = sf::Keyboard::Key::Unknown; i < sf::Keyboard::KeyCount; i++){
					
					if (sf::Keyboard::isKeyPressed((sf::Keyboard::Key)i)){
						e_keyboard.setKey(convertSFKey((sf::Keyboard::Key)i));
						if (event.KeyReleased)
							e_keyboard.setKeyboardAction(EventKeyboardAction::KEY_RELEASED);
						log_manager.writeLog("Key:%d is down", i);
					}
				}
				onEvent(&e_keyboard);
			}
		else if (event.type == sf::Event::MouseMoved){
			//Do mouse moved stuff
			 EventMouse e_mouse;
			 Position new_mouse_pos(event.mouseMove.x, event.mouseMove.y);
				e_mouse.setMouseAction(EventMouseAction::MOVED);
				e_mouse.setMousePosition(pixelsToSpaces(new_mouse_pos));

				onEvent(&e_mouse);

				log_manager.writeLog("Mouse is moved");
			
		}
		else if (event.type == sf::Event::MouseButtonPressed){
			EventMouse e_mouse;
			//Position new_mouse_pos(event.mouseMove.x, event.mouseMove.y);
			if (event.mouseButton.button == sf::Mouse::Right){
				e_mouse.setMouseButton(EventMouseButton::RIGHT);
				e_mouse.setMouseAction(EventMouseAction::PRESSED);
			//	e_mouse.setMousePosition(pixelsToSpaces(new_mouse_pos));
				onEvent(&e_mouse);
				log_manager.writeLog("Right mouse clicked");
			}
			//do left clicked stuff
			e_mouse.setMouseButton(EventMouseButton::LEFT);
			e_mouse.setMouseAction(EventMouseAction::PRESSED);
		//	e_mouse.setMousePosition(pixelsToSpaces(new_mouse_pos));
			onEvent(&e_mouse);
			log_manager.writeLog("Left mouse clicked");
		}

	}//end while
	//Check current key press events for each key
	//Keyboard::Key key;
	//sf::Keyboard::Key sf_key;
	//sf::Keyboard kb;
	EventKeyboard e_keyboard;
	for (int i = sf::Keyboard::Key::Unknown; i < sf::Keyboard::KeyCount; i++){
		if (sf::Keyboard::isKeyPressed((sf::Keyboard::Key)i)){
			e_keyboard.setKey(convertSFKey((sf::Keyboard::Key)i));
			if (event.KeyPressed)
			e_keyboard.setKeyboardAction(EventKeyboardAction::KEY_DOWN);
			log_manager.writeLog("Key:%d is down", i);
		}
	}
	onEvent(&e_keyboard);
	//mouse presses
	//sf::Mouse mouse;
	
	if (sf::Mouse::isButtonPressed(sf::Mouse::Button::Left)){
		 EventMouse e_mouse;
		 Position new_mouse_pos(event.mouseMove.x, event.mouseMove.y);
		e_mouse.setMouseButton(convertSFMouseButton(sf::Mouse::Button::Left));
		e_mouse.setMouseAction(EventMouseAction::CLICKED);
		e_mouse.setMousePosition(pixelsToSpaces(new_mouse_pos));
		log_manager.writeLog("Left mouse pressed");
		onEvent(&e_mouse);
	}
	if (sf::Mouse::isButtonPressed(sf::Mouse::Button::Right)){
		EventMouse e_mouse;
		Position new_mouse_pos(event.mouseMove.x, event.mouseMove.y);
		e_mouse.setMouseButton(convertSFMouseButton(sf::Mouse::Button::Right));
		e_mouse.setMouseAction(EventMouseAction::CLICKED);
		e_mouse.setMousePosition(pixelsToSpaces(new_mouse_pos));
		log_manager.writeLog("Right mouse pressed");
		onEvent(&e_mouse);
	}
	if (sf::Mouse::isButtonPressed(sf::Mouse::Button::Middle)){
		EventMouse e_mouse;
		Position new_mouse_pos(event.mouseMove.x, event.mouseMove.y);
		e_mouse.setMouseButton(convertSFMouseButton(sf::Mouse::Button::Middle));
		e_mouse.setMouseAction(EventMouseAction::CLICKED);
		e_mouse.setMousePosition(pixelsToSpaces(new_mouse_pos));
		log_manager.writeLog("Middle mouse pressed");
		onEvent(&e_mouse);
	}
}

//Return the df key version of the sf key
Keyboard::Key InputManager::convertSFKey(sf::Keyboard::Key k) {
	switch (k) {
	case sf::Keyboard::Key::A:
		return Keyboard::Key::A;
		break;
	case sf::Keyboard::Key::B:
		return Keyboard::Key::B;
		break;
	case sf::Keyboard::Key::C:
		return Keyboard::Key::C;
		break;
	case sf::Keyboard::Key::D:
		return Keyboard::Key::D;
		break;
	case sf::Keyboard::Key::F:
		return Keyboard::Key::F;
		break;
	case sf::Keyboard::Key::G:
		return Keyboard::Key::G;
		break;
	case sf::Keyboard::Key::H:
		return Keyboard::Key::H;
		break;
	case sf::Keyboard::Key::I:
		return Keyboard::Key::I;
		break;
	case sf::Keyboard::Key::J:
		return Keyboard::Key::J;
		break;
	case sf::Keyboard::Key::K:
		return Keyboard::Key::K;
		break;
	case sf::Keyboard::Key::L:
		return Keyboard::Key::L;
		break;
	case sf::Keyboard::Key::M:
		return Keyboard::Key::M;
		break;
	case sf::Keyboard::Key::N:
		return Keyboard::Key::N;
		break;
	case sf::Keyboard::Key::O:
		return Keyboard::Key::O;
		break;
	case sf::Keyboard::Key::P:
		return Keyboard::Key::P;
		break;
	case sf::Keyboard::Key::Q:
		return Keyboard::Key::Q;
		break;
	case sf::Keyboard::Key::R:
		return Keyboard::Key::R;
		break;
	case sf::Keyboard::Key::S:
		return Keyboard::Key::S;
		break;
	case sf::Keyboard::Key::T:
		return Keyboard::Key::T;
		break;
	case sf::Keyboard::Key::U:
		return Keyboard::Key::U;
		break;
	case sf::Keyboard::Key::V:
		return Keyboard::Key::V;
		break;
	case sf::Keyboard::Key::W:
		return Keyboard::Key::W;
		break;
	case sf::Keyboard::Key::X:
		return Keyboard::Key::X;
		break;
	case sf::Keyboard::Key::Y:
		return Keyboard::Key::Y;
		break;
	case sf::Keyboard::Key::Z:
		return Keyboard::Key::Z;
		break;
	case sf::Keyboard::Key::Num0:
		return Keyboard::Key::NUM0;
		break;
	case sf::Keyboard::Key::Num1:
		return Keyboard::Key::NUM1;
		break;
	case sf::Keyboard::Key::Num2:
		return Keyboard::Key::NUM2;
		break;
	case sf::Keyboard::Key::Num3:
		return Keyboard::Key::NUM3;
		break;
	case sf::Keyboard::Key::Num4:
		return Keyboard::Key::NUM4;
		break;
	case sf::Keyboard::Key::Num5:
		return Keyboard::Key::NUM5;
		break;
	case sf::Keyboard::Key::Num6:
		return Keyboard::Key::NUM6;
		break;
	case sf::Keyboard::Key::Num7:
		return Keyboard::Key::NUM7;
		break;
	case sf::Keyboard::Key::Num8:
		return Keyboard::Key::NUM8;
		break;
	case sf::Keyboard::Key::Num9:
		return Keyboard::Key::NUM9;
		break;
	case sf::Keyboard::Key::Space:
		return Keyboard::Key::SPACE;
		break;
	case sf::Keyboard::Key::Return:
		return Keyboard::Key::RETURN;
		break;
	case sf::Keyboard::Key::Escape:
		return Keyboard::Key::ESCAPE;
		break;
	case sf::Keyboard::Key::Tab:
		return Keyboard::Key::TAB;
		break;
	case sf::Keyboard::Key::Left:
		return Keyboard::Key::LEFTARROW;
		break;
	case sf::Keyboard::Key::Right:
		return Keyboard::Key::RIGHTARROW;
		break;
	case sf::Keyboard::Key::Up:
		return Keyboard::Key::UPARROW;
		break;
	case sf::Keyboard::Key::Down:
		return Keyboard::Key::DOWNARROW;
		break;
	case sf::Keyboard::Key::Pause:
		return Keyboard::Key::PAUSE;
		break;
	case sf::Keyboard::Key::Subtract:
		return Keyboard::Key::MINUS;
		break;
	case sf::Keyboard::Key::Add:
		return Keyboard::Key::PLUS;
		break;
	case sf::Keyboard::Key::Tilde:
		return Keyboard::Key::TILDE;
		break;
	case sf::Keyboard::Key::Period:
		return Keyboard::Key::PERIOD;
		break;
	case sf::Keyboard::Key::Comma:
		return Keyboard::Key::COMMA;
		break;
	case sf::Keyboard::Key::Slash:
		return Keyboard::Key::SLASH;
		break;
	case sf::Keyboard::Key::LControl:
		return Keyboard::Key::LEFTCONTROL;
		break;
	case sf::Keyboard::Key::RControl:
		return Keyboard::Key::RIGHTCONTROL;
		break;
	case sf::Keyboard::Key::LShift:
		return Keyboard::Key::LEFTSHIFT;
		break;
	case sf::Keyboard::Key::RShift:
		return Keyboard::Key::RIGHTSHIFT;
		break;
	case sf::Keyboard::Key::F1:
		return Keyboard::Key::F1;
		break;
	case sf::Keyboard::Key::F2:
		return Keyboard::Key::F2;
		break;
	case sf::Keyboard::Key::F3:
		return Keyboard::Key::F3;
		break;
	case sf::Keyboard::Key::F4:
		return Keyboard::Key::F4;
		break;
	case sf::Keyboard::Key::F5:
		return Keyboard::Key::F5;
		break;
	case sf::Keyboard::Key::F6:
		return Keyboard::Key::F6;
		break;
	case sf::Keyboard::Key::F7:
		return Keyboard::Key::F7;
		break;
	case sf::Keyboard::Key::F8:
		return Keyboard::Key::F8;
		break;
	case sf::Keyboard::Key::F9:
		return Keyboard::Key::F9;
		break;
	case sf::Keyboard::Key::F10:
		return Keyboard::Key::F10;
		break;
	case sf::Keyboard::Key::F11:
		return Keyboard::Key::F11;
		break;
	case sf::Keyboard::Key::F12:
		return Keyboard::Key::F12;
		break;
	default:
		return Keyboard::Key::UNDEFINED_KEY;
		break;
	}
}

//Return the df Mouse button version of the sf Mouse button
EventMouseButton InputManager::convertSFMouseButton(sf::Mouse::Button b){
	switch (b) {
	case sf::Mouse::Button::Left:
		return EventMouseButton::LEFT;
		break;
	case sf::Mouse::Button::Right:
		return EventMouseButton::RIGHT;
		break;
	case sf::Mouse::Button::Middle:
		return EventMouseButton::MIDDLE;
		break;
	default:
		return EventMouseButton::UNDEFINED_MOUSE_BUTTON;
		break;
	}
}