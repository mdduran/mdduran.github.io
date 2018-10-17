
//Object source file
#include "Object.h"
#include "WorldManager.h"

#include <stdlib.h>
using namespace df;
static int next_id = 0;

//Constructor
df::Object::Object(){
	//Construct object. Set default parameters and add to game world
	id = next_id;
	next_id++;
	type = "undefined";
	pos.setXY(0, 0);
	altitude = 0;
	x_velocity = 0.0;
	x_velocity_countdown = 0.0;
	y_velocity = 0.0;
	y_velocity_countdown = 0.0;
	solidness = SOFT;
	//Add self to game world
	df::WorldManager &world_manager = df::WorldManager::getInstance();
	world_manager.insertObject(this);
}

//Destructor
df::Object::~Object(){
	//Remove from the game world

	df::WorldManager &world_manager = df::WorldManager::getInstance();
	world_manager.removeObject(this);
}

//Set the object id.
void df::Object::setId(int new_id){
	id = new_id;
}

//Get Object id
int df::Object::getId() const{
	return id;
}

//Set type identifier of object
void df::Object::setType(std::string new_type){
	type = new_type;
}

//Get type identifier of object
std::string df::Object::getType() const{
	return type;
}

//Set position of object
void df::Object::setPosition(Position new_pos){
	pos = new_pos;
}

//Get the position of the object
Position df::Object::getPosition() const{
	return pos;
}

int df::Object::eventHandler(const Event *p_e){
	return 0;
}

void df::Object::draw(){}

int df::Object::setAltitude(int new_altitude){
	if (new_altitude >= 0 && new_altitude <= MAX_ALTITUDE){
		altitude = new_altitude;
		return 0;
	}
	else{
		return -1;
	}
		
}

int df::Object::getAltitude() const{
	return altitude;
}

//Get and set velocity(x,y)
void df::Object::setXVelocity(float new_x_velocity){ //also sets countdown to 1
	x_velocity = new_x_velocity;
	x_velocity_countdown = 1;
}
float df::Object::getXVelocity() const{
	return x_velocity;
}
void df::Object::setYVelocity(float new_y_velocity){ //also sets countdown to 1
	y_velocity = new_y_velocity;
	y_velocity_countdown = 1;
}
float df::Object::getYVelocity() const{
	return y_velocity;
}

//Perform 1 step of velocity in horizontal direction
//Return horizontal distance moved this step
int df::Object::getXVelocityStep(){
	if (x_velocity == 0)
		return 0;//no velocity so no move
	
	//See if moving this step
	x_velocity_countdown = x_velocity_countdown - fabs(x_velocity);
	if (x_velocity_countdown > 0)
		return 0;//not time to move

	//Moving this step so figure out how far
	int spaces = (int)(floor(1 - x_velocity_countdown));
	x_velocity_countdown = (float)(1 + fmod(x_velocity_countdown, 1));

	//Return number of spaces to move.
	if (x_velocity > 0)
		return spaces;
	else
		return -1 * spaces;
}

//Perform 1 step of velocity in vertical direction
//Return vertical distance moved this step
int df::Object::getYVelocityStep(){
	if (y_velocity == 0)
		return 0;//no velocity so no move

	//See if moving this step
	y_velocity_countdown = y_velocity_countdown - fabs(y_velocity);
	if (y_velocity_countdown > 0)
		return 0;//not time to move

	//Moving this step so figure out how far
	int spaces = (int)floor(1 - y_velocity_countdown);
	y_velocity_countdown = (float)(1 + fmod(y_velocity_countdown, 1));

	//Return number of spaces to move.
	if (y_velocity > 0)
		return spaces;
	else
		return -1 * spaces;
}
//True if Hard or Soft, else false
bool df::Object::isSolid() const{
	if (solidness == HARD || solidness == SOFT){
		return true;
	}
	else{
		return false;
	}

}

//Set object solidness, with checks for consistency.
//Return 0 if ok, else -1;
int df::Object::setSolidness(Solidness new_solid){
	if (new_solid >= 0 && new_solid <= 2){
		solidness = new_solid;
		return 0;
	}
	else
	{
		return -1;
	}
}

//Return object solidness
Solidness df::Object::getSolidness() const{
	return solidness;
}
