#ifndef _OBJECTLISTITERATOR_H_
#define _OBJECTLISTITERATOR_H_
#include "ObjectList.h"
namespace df{
	class Object;
	class ObjectList;

	class ObjectListIterator{

	private:
		ObjectListIterator();  //Must be given list when created
		int index;  //Index into list
		const ObjectList *p_list; //List iterating over

	public:
		//Create iterator, over indicated list
		ObjectListIterator(const ObjectList *p_l);

		void first();  //Set iterator to first item in list.
		void next();  //Set iterator to next item in list.
		bool isDone() const;  //Return true if at end of the list.

		//Return pointer to current Object, NULL if done/empty.
		Object *currentObject() const;
	};
}
#endif