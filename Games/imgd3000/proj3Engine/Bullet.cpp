//
// Bullet.cpp
//

// Engine includes.
#include "GraphicsManager.h"
#include "LogManager.h"
#include "WorldManager.h"
#include "EventOut.h"

// Game includes.
#include "Bullet.h"
#include "Saucer.h"
using namespace df;
Bullet::Bullet(Position hero_pos) {

  // Set object properties.
  setType("Bullet");
  setXVelocity(1);		// move 1 space right every frame
  
  // Set starting location, based on hero's position passed in.
  Position pos(hero_pos.getX()+3, hero_pos.getY());
  setPosition(pos);
}

// Handle event.
// Return 0 if ignored, else 1.
int Bullet::eventHandler(const Event *p_e) {

  if (p_e->getType() == OUT_EVENT) {
    out();
    return 1;
  }

  if (p_e->getType() == COLLISION_EVENT) {
    const EventCollision *p_collision_event = static_cast <const df::EventCollision *> (p_e);
    hit(p_collision_event);
    return 1;
  }

  // If get here, have ignored this event.
  return 0;
}

// If bullet moves outside world, mark self for deletion.
void Bullet::out() {
  df::WorldManager &world_manager = df::WorldManager::getInstance();
  world_manager.markForDelete(this);
}

// If bullet hits Saucer, mark Saucer and bullet for deletion.
void Bullet::hit(const df::EventCollision *p_c) {
  df::WorldManager &world_manager = df::WorldManager::getInstance();
  world_manager.markForDelete(p_c->getObject1());
  world_manager.markForDelete(p_c->getObject2());
}

void Bullet::draw() {
  df::GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
  graphics_manager.drawCh(getPosition(), BULLET_CHAR, BLUE); 
}
