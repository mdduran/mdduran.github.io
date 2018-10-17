//Object list source file
#include "ObjectList.h"
using namespace df;
//constructor
ObjectList::ObjectList(){
	count = 0;

}

//Insert object pointer in list
//Return 0 if ok, else -1
int ObjectList::insert(Object *p_o){
	if (!isFull()){
		list[count] = p_o;
		count++;
		return 0;
	}
	for (int i = 0; i < count; i++){
		if (list[i] == p_o){
			return 0;
		}
	}
	return -1;
}

//Remove object pointer from list
//Return 0 if ok, else -1
int ObjectList::remove(Object *p_o){
	for (int i = 0; i < count; i++){
		if (list[i] == p_o){//if found...
			//remove object
		//	list[i] = NULL; //check
			for (int j = i; j < count - 1; j++){//scoot over
				list[j] = list[j + 1];
			}
			
			count--;
			return 0;//found
		}
	}
	return -1; //not found
}

//Clear list
void ObjectList::clear(){
	count = 0;
}

//Return count of number of objects in list
int ObjectList::getCount() const{
	return count;
}

//Return true if list is empty, else false
bool ObjectList::isEmpty() const{
	if (count == 0){
		return true;
	}
	else{
		return false;
	}
}

//Return true of list is full, else false
bool ObjectList::isFull() const{
	if (count == MAX_OBJECTS){
		return true;
	}
	else{
		return false;
	}
}