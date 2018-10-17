//Graphics Manager source file
#include "GraphicsManager.h"
#include "LogManager.h"
#include <stdio.h>
#include <iostream>

using namespace df;
//Constructor
GraphicsManager::GraphicsManager(){
	setType("GraphicsManager");
	font.loadFromFile(FONT_FILE_DEFAULT);
	window_horizontal_pixels = WINDOW_HORIZONTAL_PIXELS_DEFAULT;
	window_vertical_pixels = WINDOW_VERTICAL_PIXELS_DEFAULT;
	window_horizontal_chars = WINDOW_HORIZONTAL_CHARS_DEFAULT;
	window_vertical_chars = WINDOW_VERTICAL_CHARS_DEFAULT;
	window_background_color = WINDOW_BACKGROUND_COLOR_DEFAULT;

}

//get the one and only instance of the graphics manager
GraphicsManager &GraphicsManager::getInstance(){
	static GraphicsManager graphics_manager;
	return graphics_manager;
}

int GraphicsManager::startUp(){
	LogManager &log_manager = LogManager::getInstance();
	//If window already created, do nothing
	if (p_window != NULL){
		return 0;
	}
	//load font file
	if (font.loadFromFile(FONT_FILE_DEFAULT) == false){
		std::cout << "Error unable to load font" << FONT_FILE_DEFAULT << "." << std::endl;
		log_manager.writeLog("GraphicsManager()::Error loading font.");
		return -1;
	}

	p_window =
		new sf::RenderWindow(sf::VideoMode(window_horizontal_pixels, window_vertical_pixels), WINDOW_TITLE_DEFAULT);
	p_window->setMouseCursorVisible(false);
	p_window->setVerticalSyncEnabled(true);
	
	if (Manager::startUp()){
		return -1;
	}
	log_manager.writeLog("GraphicsManager has started up.");
	return 0;
	
}

void GraphicsManager::shutDown(){
	p_window->close();
	Manager::shutDown();
}

//Return window's horizontal maximum(in characters)
int GraphicsManager::getHorizontal() const{
	return window_horizontal_chars;
}

//Return window's vertical maximum(in characters)
int GraphicsManager::getVertical() const{
	return window_vertical_chars;
}

//Return window's horizontal maximum (in pixels)
int GraphicsManager::getHorizontalPixels() const{
	return window_horizontal_pixels;
}

//Return window's vertical maximum (in pixeks)
int GraphicsManager::getVerticalPixels() const{
	return window_vertical_pixels;
}

//Compute character height, based on window size and font.
float charHeight(){
	GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
	return (float)graphics_manager.getVerticalPixels() / graphics_manager.getVertical();
}

//Compute character width, based on window size and font.
float charWidth(){
	GraphicsManager &graphics_manager = df::GraphicsManager::getInstance();
	return (float)graphics_manager.getHorizontalPixels() / graphics_manager.getHorizontal();
}

//Return pointer to SFML drawing window.
sf::RenderWindow *GraphicsManager::getWindow() const{
	return p_window;
}

//Convert ASCII spaces (x,y) to window pixels (x,y).
df::Position spacesToPixels(Position spaces){
	Position sToPixel;
	//sToPixel.setX(spaces.getX() *(int)charWidth());
	//sToPixel.setY(spaces.getY() * (int)charHeight());
	sToPixel.setXY((spaces.getX() *(int)charWidth()), (spaces.getY() * (int)charHeight()));
	return sToPixel;
}

//Convert window pixels (x,y) to ASCII spaces (x,y).
df::Position pixelsToSpaces(Position pixels){
	Position pToSpaces;
	//pToSpaces.setX(pixels.getX() / (int)charWidth());
	//pToSpaces.setY(pixels.getY() / (int)charHeight());
	pToSpaces.setXY((pixels.getX() / (int)charWidth()), (pixels.getY() / (int)charHeight()));
	return pToSpaces;
}

//Draw character at screen location (x,y) with color.
//Return 0 if ok, else -1
int GraphicsManager::drawCh(Position world_pos, char ch, Color color)const{
	//Get instance of Log Manager
	LogManager &log_manager = LogManager::getInstance();
	//make sure window is allocated 
	if (p_window == NULL){
		return -1;
	}

	//Convert spaces (x,y) to pixels(x,y)
	Position pixels_pos = spacesToPixels(world_pos);

	//Draw background rectangle since text is "see through" in SFML.
	sf::RectangleShape rectangle;
	rectangle.setSize(sf::Vector2f(charWidth(), charHeight() - 1));
	rectangle.setFillColor(WINDOW_BACKGROUND_COLOR_DEFAULT);
	rectangle.setPosition(((pixels_pos.getX() + charWidth()) / 2 - 5),
						  ((pixels_pos.getY() + charHeight()) / 2 - 12));
	p_window->draw(rectangle);

	//Create character text to draw
	static sf::Text text("", font);
	text.setString(ch);
	text.setStyle(sf::Text::Bold); //Make bold since it looks better

	//Scale to the right size
	if (charWidth() < charHeight()){
		text.setCharacterSize((int)charWidth() * 2);
	}
	else{
		text.setCharacterSize((int)charHeight() * 2);
	}

	//Set SFML color based on Dragonfly color
	switch (color){
	case YELLOW:
		text.setColor(sf::Color::Yellow);
		break;
	case RED:
		text.setColor(sf::Color::Red);
		break;
	case BLUE:
		text.setColor(sf::Color::Blue);
		break;
	case MAGENTA:
		text.setColor(sf::Color::Magenta);
		break;
	case CYAN:
		text.setColor(sf::Color::Cyan);
		break;
	case WHITE:
		text.setColor(sf::Color::White);
		break;
	case BLACK:
		text.setColor(sf::Color::Black);
		break;
	case GREEN:
		text.setColor(sf::Color::Green);
		break;

	}

	//Set position
	text.setPosition((float)pixels_pos.getX(), (float)pixels_pos.getY());
	//log_manager.writeLog("Position of the text is set");

	//Draw character
	p_window->draw(text);
	//log_manager.writeLog("Text has been drawn to the window");
	return 0;
}

//Render current window buffer
//Return 0 if ok, else -1
int GraphicsManager::swapBuffers(){
	//Get instance of Log Manager
	LogManager &log_manager = LogManager::getInstance();
	//Make sure window is allocated
	if (p_window == NULL){
		return -1;
	}

	//Display current window
	p_window->display();
	//log_manager.writeLog("Window has been displayed");
	

	//Clear window to get ready for next draw
	p_window->clear(window_background_color);
	//log_manager.writeLog("Window has been cleared");

	return 0;//Success
}

//Draw string at window location(x,y) with default color
//Justified left, center, or right.
//Return 0 if ok, else -1
int GraphicsManager::drawString(Position pos, std::string str, Justification just, Color color) const{
	//Get starting position
	Position starting_pos = pos;
	switch (just){
	case CENTER_JUSTIFIED:
		starting_pos.setX(pos.getX() - str.size() / 2);
		break;
	case RIGHT_JUSTIFIED:
		starting_pos.setX(pos.getX() - str.size());
		break;
	case LEFT_JUSTIFIED:
	default:
		break;
	}

	//Draw string character by character
	for (int i = 0; i < (int)str.size(); i++){
		Position temp_pos(starting_pos.getX() + i, starting_pos.getY());
		drawCh(temp_pos, str[i], color);
	}
	return 0;
}

bool GraphicsManager::setBackgroundColor(int new_color){
	//Set SFML color based on Dragonfly color
	switch (new_color){
	case YELLOW:
		window_background_color = window_background_color.Yellow;
		return true;
		break;
	case RED:
		window_background_color = window_background_color.Red;
		return true;
		break;
	case BLUE:
		window_background_color = window_background_color.Blue;
		return true;
		break;
	case MAGENTA:
		window_background_color = window_background_color.Magenta;
		return true;
		break;
	case CYAN:
		window_background_color = window_background_color.Cyan;
		return true;
		break;
	case WHITE:
		window_background_color = window_background_color.White;
		return true;
		break;
	case BLACK:
		window_background_color = window_background_color.Black;
		return true;
		break;
	case GREEN:
		window_background_color = window_background_color.Green;
		return true;
		break;
	}

	return false;
}

