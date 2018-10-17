// Hero.h
//

#include "EventKeyboard.h"
#include "EventMouse.h"
#include "Object.h"
#include "Reticle.h"

#define HERO_CHAR '>'
namespace df{
	class Hero : public Object {

	private:
		Reticle *p_reticle;
		int fire_slowdown;
		int fire_countdown;
		int nuke_count;
		void mouse(const df::EventMouse *p_mouse_event);
		void kbd(const df::EventKeyboard *keyboard_event);
		void move(int dy);
		void fire(Position target);
		void step();
		void nuke();

	public:
		Hero();
		~Hero();
		int eventHandler(const Event *p_e);
		void draw();
	};
}