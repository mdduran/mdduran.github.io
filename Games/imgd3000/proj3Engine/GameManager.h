//GameManager.h
#ifndef _GAME_MANAGER_H_
#define _GAMEMANAGER_H_

#include "Manager.h"
//Default frame time (game loop time) in milliseconds (33 ms == 30 f/s).
const int FRAME_TIME_DEFAULT = 33;
namespace df{
	class GameManager : public Manager{
	private:
		GameManager(); //Private since it is a singleton.
		GameManager(GameManager const&);//Dont allow copy
		void operator = (GameManager const&); //Dont allow assignment
		bool game_over; //True, then game loop should stop
		int frame_time; //Target time per game loop, in milliseconds.
		int step_count;

	public:
		//Destructor
		~GameManager();
		//Get the singleton instance of the GameManager.
		static GameManager &getInstance();

		//Startup all GameManager services
		int startUp();

		//Shut down all GameManager services
		void shutDown();

		//Run game loop.
		void run();

		//Set game over status to indicated value.
		//If true (default), will stop game loop.
		void setGameOver(bool new_game_over = true);

		//Get game over status
		bool getGameOver() const;

		//Return frame time.
		//Frame time is target time for game loop, in milliseconds.
		int getFrameTime() const;
	};
}
#endif