#ifndef _OBJECT_H_
#define _OBJECT_H_
//System includes
#include <string>

//Engine includes
#include "Position.h"
#include "Event.h"
namespace df{
	enum Solidness{
		HARD, //Object causes collisions
		SOFT, //Object causes collisions but doesn't impede
		SPECTRAL, //Object doesn't cause collisions
	};

	class Object{
	private:
		int id; //Unique Object identifier
		std::string type; //User defined identification
		Position pos; //Position in game world
		int altitude; //0 to MAX supported (lower drawn first)
		float x_velocity; //Horizontal speed in spaces per step
		float x_velocity_countdown;//Countdown to horizontal movement
		float y_velocity;//Vertical speed in spaces per step
		float y_velocity_countdown;//Countdown to vertical movement
		Solidness solidness; //Solidness of an object


	public:
		//Construct Object. Set default parameters and add to game world
		Object();

		//Destroy object
		//Remove from the game world
		virtual ~Object();

		//Set the object id
		void setId(int new_id);

		//Get Object id
		int getId() const;

		//Set type identifier of object
		void setType(std::string new_type);

		//Get type identifier of object
		std::string getType() const;

		//Set position of object
		void setPosition(Position new_pos);

		//Get position of object
		Position getPosition() const;


		//Handle event(default is to ignore everything)
		//Return 0 if ignored, else 1 if handled
		virtual int eventHandler(const Event *p_event);


		virtual void draw();

		//Set altitude of Object, with checks for range [0, MAX_ALTITUDE].
		//Return 0 if ok, else -1
		int setAltitude(int new_altitude);

		//Return altitude of Object.
		int getAltitude() const;

		//Get and set velocity(x,y)
		void setXVelocity(float new_x_velocity);//also sets countdown to 1
		float getXVelocity() const;
		void setYVelocity(float new_y_velocity);//also sets countdown to 1
		float getYVelocity() const;

		//Perform 1 step of velocity in horizontal direction
		//Return horizontal distance moved this step
		int getXVelocityStep();

		//Perform 1 step of velocity in vertical direction
		//Return vertical distance moved this step
		int getYVelocityStep();

		//True if Hard or Soft, else false
		bool isSolid() const;

		//Set object solidness, with checks for consistency.
		//Return 0 if ok, else -1;
		int setSolidness(Solidness new_solid);

		//Return object solidness
		Solidness getSolidness() const;
	};
}
#endif