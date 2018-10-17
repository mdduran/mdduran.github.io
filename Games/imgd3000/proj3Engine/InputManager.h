//Input Manager header file
#ifndef _INPUT_MANAGER_H_
#define _INPUTMANAGER_H_

#include "Manager.h"
#include "EventKeyboard.h"
#include "EventMouse.h"



namespace df{
	class InputManager : public Manager{

	private:
		InputManager();//private (a singleton)
		InputManager(InputManager const&); //don't allow copy
		void operator=(InputManager const&);//Don't allow assignment


	public:
		//Get the one and only instance of the input manager
		static InputManager &getInstance();

		//Get window ready to capture input
		//Return 0 if ok, else return negative number
		int startUp();

		//Revert back to normal window mode
		void shutDown();

		//GetInput from the keyboard and mouse
		//Pass event along to all objects
		void getInput();

		//Return the df key version of the sf key
		 Keyboard::Key convertSFKey(sf::Keyboard::Key k);

		//Return the df Mouse button version of the sf Mouse button
		EventMouseButton convertSFMouseButton(sf::Mouse::Button b);
	};
}
#endif