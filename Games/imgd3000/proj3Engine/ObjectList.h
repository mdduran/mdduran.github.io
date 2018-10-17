#ifndef _OBJECTLIST_H_
#define _OBJECTLIST_H_
const int MAX_OBJECTS = 500;

#include "Object.h"
#include "ObjectListIterator.h"
namespace df{
	class Object;
	class ObjectListIterator;

	class ObjectList{
	private:
		int count; //Count of objects in list;
		Object *list[MAX_OBJECTS]; //Array of pointers to objects

	public:
		friend class ObjectListIterator;

		//default constructor
		ObjectList();

		//Insert object pointer in list
		//Return 0 if ok, else -1
		int insert(Object *p_o);

		//Removeobject pointer from list
		//Return 0 if found, else -1
		int remove(Object *p_o);

		//Clear list(setting count to 0)
		void clear();

		//Return count of number of objects in list
		int getCount() const;

		//Return true if list is empty, else false
		bool isEmpty() const;

		//Return true if list is full, else return false;
		bool isFull() const;
	};
}
#endif
