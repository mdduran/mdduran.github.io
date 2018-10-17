#ifndef _WORLDMANAGER_H_
#define _WORLDMANAGER_H_
#include "Manager.h"
#include "ObjectList.h"
#include "ObjectListIterator.h"

const int MAX_ALTITUDE = 4;
namespace df{

	class WorldManager : public Manager{
	private:
		WorldManager(); //Private (a singleton)
		WorldManager(WorldManager const&); //Don't allow copy
		void operator =(WorldManager const&); //Don't allow assignment

		ObjectList updates;  //All objects in world to update
		ObjectList deletions; //All Objects in world to delete

	public:
		//Get the one and only instance of the WorldManager
		static WorldManager &getInstance();

		//Startup game world (initialize everything to empty)
		//Return 0
		int startUp();

		//Shutdown game world (delete all game world objects).
		void shutDown();

		//Add object to world. Return 0 if ok, else -1
		int insertObject(Object *p_o);

		//Remove object from world. Return 0 if ok, else -1
		int removeObject(Object *p_o);

		//Return list of all Objects
		ObjectList getAllObjects(void) const;

		//Update world
		//Delete objects marked for deletion
		void update();

		//Indicate object is to be deleted at the end of current game loop
		//Return 0 if ok, else -1
		int markForDelete(Object *p_o);

		//Draw objects in the world
		virtual void draw();

		// Return list of Objects collided with at Position `where'.
		// Collisions only with solid Objects.
		// Does not consider if p_o is solid or not.
		ObjectList isCollision(Object *p_o, Position where) const;

		// Move Object.
		// If no collision with solid, move ok else don't move.
		// If p_go is Spectral, move ok.
		// Return 0 if move ok, else -1 if collision with solid.
		int moveObject(Object *p_o, Position where);

		

	};
}

#endif
