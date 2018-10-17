//Mouse event header
#ifndef _EVENTMOUSE_H_
#define _EVENTMOUSE_H_
#include "Event.h"
#include "Position.h"
#include <SFML/Graphics.hpp>

	const std::string MOUSE_EVENT = "df::mouse";
	namespace df{
		//Set of mouse buttons recognized by Dragonfly.
		enum EventMouseButton{
			UNDEFINED_MOUSE_BUTTON = -1,
			LEFT,
			RIGHT,
			MIDDLE,
		};

		//Set of mouse actions recognized by Dragonfly.
		enum EventMouseAction{
			UNDEINED_MOUSE_ACTION = -1,
			CLICKED,
			PRESSED,
			MOVED,
		};

		class EventMouse :public Event{

		private:
			EventMouseAction mouse_action; //Mouse action
			EventMouseButton mouse_button; //Mouse button
			Position mouse_xy;

		public:
			EventMouse();
			//Load mouse event's action.
			void setMouseAction(EventMouseAction new_mouse_action);
			//Get mouse event's action.
			EventMouseAction getMouseAction() const;
			//Set mouse event's button
			void setMouseButton(EventMouseButton new_mouse_button);
			//Get mouse event's button
			EventMouseButton getMouseButton() const;
			//Set mouse event's position
			void setMousePosition(Position new_mouse_xy);
			//Get mouse event's y position
			Position getMousePosition() const;

		};
	}
#endif