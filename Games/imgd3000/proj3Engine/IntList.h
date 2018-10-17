const int MAX = 100;

class IntList{
	private:
		int list[MAX];
		int count;

	public:
		IntList(){
			count = 0;
		}
		//Clear list
		void clear(){
			count = 0;
		}

		//Add item to list
		bool insert(int x){
			if (count == MAX) //check if there is enough room
				return false;
			list[count] = x;
			count++;
			return true;
		}

		//Remove item from list
		bool remove(int x){
			for (int i = 0; i < count; i++){
				if (list[i] == x){
					for (int j = i; j < count - 1; j++)
						list[j] = list[j + 1];
					count--;
					return true;
				}
			}
			return false;
		}

};