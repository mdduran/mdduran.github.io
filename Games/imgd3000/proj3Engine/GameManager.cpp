//Game Manager source file
#include "GameManager.h"
#include "LogManager.h"
#include "WorldManager.h"
#include "GraphicsManager.h"
#include "InputManager.h"
#include "ResourceManager.h"
#include "EventStep.h"
#include "Clock.h"

//System includes
#include <Windows.h>

using namespace df;

//constructor
GameManager::GameManager(){
	setType("GameManager");
	game_over = false;
	frame_time = 33;
	step_count = 0;
}

//destructor
GameManager::~GameManager(){
	shutDown();
}

//get the one and only instance of the game manager
GameManager &GameManager::getInstance(){
	static GameManager game_manager;
	return game_manager;
}

//Start up the game manager and all of its services
int GameManager::startUp(){
	Manager::startUp();
	LogManager &log_manager = df::LogManager::getInstance();
	log_manager.startUp();
	GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
	graphics_manager.startUp();
	InputManager &input_manager = InputManager::getInstance();
	input_manager.startUp();
	WorldManager &world_manager = df::WorldManager::getInstance();
	world_manager.startUp();
	ResourceManager &rm = df::ResourceManager::getInstance();
	
	if (&Manager::isStarted){
		timeBeginPeriod(1);
		return 0;
	}
	else{
		return -1;
	}
}

//Shut down the game manager services
void GameManager::shutDown(){
	Manager::shutDown();
	ResourceManager &resource_manager = df::ResourceManager::getInstance();
	InputManager &input_manager = df::InputManager::getInstance();
	GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
	LogManager &log_manager = df::LogManager::getInstance();
	WorldManager &world_manager = df::WorldManager::getInstance();
	world_manager.shutDown();
	resource_manager.shutDown();
	input_manager.shutDown();
	graphics_manager.shutDown();
	log_manager.shutDown();
	setGameOver();
	timeEndPeriod(1);
}

//Run the game loop
void GameManager::run(){
	Clock *clock = new Clock;
	long int loop_time = 0;
	LogManager &log_manager = LogManager::getInstance();
	WorldManager &world_manager = WorldManager::getInstance();
	GraphicsManager &graphics_manager = GraphicsManager::getInstance();
	InputManager &input_manager = InputManager::getInstance();
	//int loop_counter = 0;
	while (!game_over){
		clock->delta();
		//get all inputs and whatnot
		input_manager.getInput();
		//update game world
		EventStep s(step_count);
		onEvent(&s);
		world_manager.update();
		//draw scene to back buffer
		world_manager.draw();
		//log_manager.writeLog("Draw is supposedly complete");
		//swap back buffer with current buffer
		graphics_manager.swapBuffers();

		loop_time = clock->split();
		if (FRAME_TIME_DEFAULT - loop_time > 0){
			Sleep(FRAME_TIME_DEFAULT - loop_time);
		}
		
		//loop_counter++;
		step_count ++;
	}
	printf("Loop ran.");
}

void GameManager::setGameOver(bool new_game_over){
	game_over = new_game_over;
}

bool GameManager::getGameOver() const{
	return game_over;
}

int GameManager::getFrameTime() const{
	return FRAME_TIME_DEFAULT;
}