//
// Explosion.h
//

#include "Object.h"
namespace df{

	class Explosion : public Object {

	private:
		int time_to_live;
		void step();

	public:
		Explosion();
		int eventHandler(const Event *p_e);
		void draw();
	};
}
