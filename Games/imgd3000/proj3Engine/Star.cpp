//
// Star.cpp
//

#include <stdlib.h>		// for rand()

// Engine includes.
#include "EventOut.h"
#include "GraphicsManager.h"
#include "LogManager.h"

// Game includes.
#include "Star.h"
using namespace df;
Star::Star() {
  setType("Star");
  setSolidness(SPECTRAL);
  setXVelocity((float) (-1.0 / (rand()%10 + 1)));
  setAltitude(0);	// Make them in the background.
  df::GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
  Position pos(rand()%graphics_manager.getHorizontal(),
	       rand()%graphics_manager.getVertical());
  setPosition(pos);
}

void Star::draw() {
  df::GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
  graphics_manager.drawCh(getPosition(), STAR_CHAR, WHITE); 
}

// Handle event.
// Return 0 if ignored, else 1.
int Star::eventHandler(const Event *p_e) {
  if (p_e->getType() == OUT_EVENT) {
    out();
    return 1;
  }
  // If get here, have ignored this event.
  return 0;
}

// If Star moved off screen, move back to far right.
void Star::out() {
  df::GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
  Position pos(graphics_manager.getHorizontal() + rand()%20,
	       rand() % graphics_manager.getVertical());
  setPosition(pos);
  setXVelocity((float)(-1.0 / (rand() % 10 + 1)));
}
