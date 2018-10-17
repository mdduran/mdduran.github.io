//Source file for ObjectListIterator
#include "ObjectListIterator.h"
using namespace df;
df::ObjectListIterator::ObjectListIterator(){

}

df::ObjectListIterator::ObjectListIterator(const ObjectList *p_l){
	p_list = p_l;
	first();
}

//Set iterator to first item
void df::ObjectListIterator::first(){
	index = 0;
}

//Iterate to next item
void df::ObjectListIterator::next(){
	if (index < p_list->count){
		index++;
	}
}

//Return true if done iterating, else false
bool df::ObjectListIterator::isDone() const{
	return (index == p_list->count);
}

//Return current item
df::Object *df::ObjectListIterator::currentObject() const{
	if (!isDone()){
		return p_list->list[index];
	}
	else{
		return NULL;
	}
}

