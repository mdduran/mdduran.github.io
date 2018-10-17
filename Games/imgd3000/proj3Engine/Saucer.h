//
// Saucer.h
//
 
#include "EventCollision.h"
#include "Object.h"
 
#define SAUCER_CHAR 'O'
namespace df{
	class Saucer : public Object {

	private:
		void moveToStart();
		void out();
		void hit(const df::EventCollision *p_c);

	public:
		Saucer();
		int eventHandler(const Event *p_e);
		void draw();
	};
}
