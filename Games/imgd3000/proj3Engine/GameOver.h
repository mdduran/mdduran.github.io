//
// GameOver.h
//

#include "Object.h"
namespace df{
	class GameOver : public Object {

	private:
		int time_to_live;
		void step();

	public:
		GameOver();
		~GameOver();
		int eventHandler(const Event *p_e);
		void draw();
	};
}