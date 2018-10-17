//
// game.cpp
// 

#define VERSION 1.0

// Engine includes.
#include "GameManager.h"
#include "LogManager.h"
#include "GraphicsManager.h"
#include "Utility.h"
#include "ResourceManager.h"

 
// Game includes.
#include "Hero.h"
#include "Star.h"
#include "Saucer.h"
using namespace df;
// Function prototypes.
void populateWorld(void);
void testDisplayObjects(void);
void testPositionIntersect(void);

 
/*int main(int argc, char *argv[]) {
  df::LogManager &log_manager = df::LogManager::getInstance();
  df::ResourceManager &resource_manager = df::ResourceManager::getInstance();
  // Start up game manager.
  df::GameManager &game_manager = df::GameManager::getInstance();
  if (game_manager.startUp())  {
    log_manager.writeLog("Error starting game manager!");
    game_manager.shutDown();
    return 0;
  }

  // Write game version information to logfile.
  log_manager.writeLog("Saucer Shoot Naiad, version %0.1f", VERSION);

  // Set flush of logfile during development (when done, make false).
  log_manager.setFlush(true);

  //load sounds
  //resource_manager.loadSound("sounds/fire.wav", "fire");
 // resource_manager.loadSound("sounds/nuke.wav", "nuke");
  //resource_manager.loadSound("sounds/explosion.wav", "explosion");
  //resource_manager.loadSound("sounds/game-over.wav", "game_over");

  
  // Setup some objects.
  populateWorld();
  //testDisplayObjects();
  //testPositionIntersect();
 
  // Run game (this blocks until game loop is over).
  game_manager.run();
  
 
  // Shut everything down.
  game_manager.shutDown();
}
 */
// Populate world with some objects.
void populateWorld(void) {
	GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
	//LogManager &log_manager = df::LogManager::getInstance();
	ResourceManager &resource_manager = df::ResourceManager::getInstance();
	//Turn background blue
	
	graphics_manager.setBackgroundColor(CYAN);
  // Spawn some Stars.
  for (int i=0; i<16; i++) 
    new Star;
 
  // Create hero.
  //new Hero;
  new Hero;
  //log_manager.writeLog("Object ID:%d Position X:%d PositionY:%d Altitude:%d\n", h->getId(), h->getPosition().getX(), h->getPosition().getY(), h->getAltitude());

  // Spawn some saucers to shoot.
  for (int i=0; i<16; i++)
    new Saucer;

  //load sounds
  resource_manager.loadSound("sounds/fire.wav", "fire");
  resource_manager.loadSound("sounds/nuke.wav", "nuke");
  resource_manager.loadSound("sounds/explosion.wav", "explosion");
  resource_manager.loadSound("sounds/game-over.wav", "gameover");

  //load music
  resource_manager.loadMusic("sounds/start-music.wav", "startmusic");
  

}

void testDisplayObjects(void){
	//GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
	LogManager &log_manager = df::LogManager::getInstance();

	new Saucer;
	//log_manager.writeLog("Object ID:%d Position X:%d PositionY:%d Altitude:%d\n", s->getId(), s->getPosition().getX(), s->getPosition().getY(), s->getAltitude());
}

void testPositionIntersect(void){
	Utility u;
	LogManager &log_manager = df::LogManager::getInstance();
	Hero *h = new Hero;
	Position initial = Position(0,0);
	h->setPosition(initial);
	Saucer *s = new Saucer;
	s->setPosition(initial);
	if (u.positionsIntersect(s->getPosition(), h->getPosition())){
		log_manager.writeLog("The positions intesect");
	}

}
