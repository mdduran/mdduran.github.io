//
// Reticle.h
//

#include "Object.h"

#define RETICLE_CHAR '+'
namespace df{
	class Reticle : public Object {

	public:
		Reticle();
		void draw(void);
		int eventHandler(const Event *p_e);
	};
}
