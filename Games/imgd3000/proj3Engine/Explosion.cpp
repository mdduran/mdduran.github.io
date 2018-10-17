//
// Explosion.cpp
//

// Engine includes.
#include "EventStep.h"
#include "GameManager.h"
#include "GraphicsManager.h"
#include "LogManager.h"
#include "WorldManager.h"

// Game includes.
#include "Explosion.h"
using namespace df;
// Define registerInterest in case engine does not.
static void registerInterest(std::string s) {};

Explosion::Explosion() {
  setType("Explosion");

  // Exit after about 6 steps.
  time_to_live =  6; 

  // Doesn't collide
  setSolidness(SPECTRAL);

  // Need step event to countdown.
  registerInterest(STEP_EVENT);
}

// Handle event.
// Return 0 if ignored, else 1.
int Explosion::eventHandler(const Event *p_e) {

  if (p_e->getType() == STEP_EVENT) {
    step();
    return 1;
  }

  // If get here, have ignored this event.
  return 0;
}

// Count down until explosion finished.
void Explosion::step() {
  time_to_live--;
  if (time_to_live <= 0){
    df::WorldManager &world_manager = df::WorldManager::getInstance();
    world_manager.markForDelete(this);
  }
}

void Explosion::draw() {
  df::GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
  graphics_manager.drawCh(getPosition(), '*', RED); 

  if (time_to_live < 4) {
    Position p1(getPosition().getX()-1, getPosition().getY()-1);
    Position p2(getPosition().getX()+1, getPosition().getY()-1);
    Position p3(getPosition().getX()-1, getPosition().getY()+1);
    Position p4(getPosition().getX()+1, getPosition().getY()+1);
    graphics_manager.drawCh(p1, '\\', RED); 
    graphics_manager.drawCh(p2, '/', RED); 
    graphics_manager.drawCh(p3, '/', RED); 
    graphics_manager.drawCh(p4, '\\', RED); 
  }
}
