//
// Star.h
//

#include "Object.h"

#define STAR_CHAR '.'
namespace df{
	class Star : public Object {

	private:
		void out();

	public:
		Star();
		void draw(void);
		int eventHandler(const Event *p_e);
	};
}