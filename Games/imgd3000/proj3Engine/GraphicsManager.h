#ifndef _GRAPHICSMANAGER_H_
#define _GRAPHICSMANAGER_H_
//System Includes
#include <SFML/Graphics.hpp>

//Engine includes
#include "Manager.h"
#include "Position.h"
#include "Color.h"



//Defaults for SFML window
const int WINDOW_HORIZONTAL_PIXELS_DEFAULT = 1024;
const int WINDOW_VERTICAL_PIXELS_DEFAULT = 768;
const int WINDOW_HORIZONTAL_CHARS_DEFAULT = 80;
const int WINDOW_VERTICAL_CHARS_DEFAULT = 24;
const int WINDOW_STYLE_DEFAULT = sf::Style::Titlebar;
const sf::Color WINDOW_BACKGROUND_COLOR_DEFAULT = sf::Color::Black;
const std::string WINDOW_TITLE_DEFAULT = "Dragonfly";
const std::string FONT_FILE_DEFAULT = "df-font.ttf";

enum Justification{
	LEFT_JUSTIFIED,
	CENTER_JUSTIFIED,
	RIGHT_JUSTIFIED,

};

//Compute character height, based on window size and font.
float charHeight(void);

//Compute character width, based on window size and font.
float charWidth(void);

//Convert ASCII spaces (x,y) to window pixels (x,y).
df::Position spacesToPixels(df::Position spaces);

//Convert window pixels (x,y) to ASCII spaces (x,y).
df::Position pixelsToSpaces(df::Position pixels);
namespace df{
	class GraphicsManager : public Manager{
	private:
		GraphicsManager();//Private (a singleton)
		GraphicsManager(GraphicsManager const&);//Don't allow copy.
		void operator =(GraphicsManager const&);//Don't allow assignment
		sf::Font font;//Font used for ASCII graphics
		sf::RenderWindow *p_window; //Pointer to SFML window
		int window_horizontal_pixels;//Horizontal pixels in window
		int window_vertical_pixels;//Vertical pixels in window
		int window_horizontal_chars;//Horizontal ASCII spaces in window
		int window_vertical_chars;//Vertical ASCII spaces in window
		sf::Color window_background_color;//Background color of the window

	public:
		//Get the one and only instance of the Graphics Manager
		static GraphicsManager &getInstance();
		//Open graphics window ready for text-based display.
		//Return 0 is ok, else -1
		int startUp();

		//Close graphics window.
		void shutDown();

		//Draw character at screen location (x,y) with color.
		//Return 0 if ok, else -1
		int drawCh(Position world_pos, char ch, Color color) const;

		//Return window's horizontal maximum(in characters)
		int getHorizontal() const;

		//Return window's vertical maximum(in characters)
		int getVertical() const;

		//Return window's horizontal maximum (in pixels)
		int getHorizontalPixels() const;

		//Return window's vertical maximum (in pixeks)
		int getVerticalPixels() const;

		//Render current window buffer
		//Return 0 if ok, else -1
		int swapBuffers();

		//Return pointer to SFML drawing window.
		sf::RenderWindow *getWindow(void) const;

		//Draw string at window location(x,y) with default color
		//Justified left, center, or right.
		//Return 0 if ok, else -1
		int drawString(Position pos, std::string str, Justification just, Color color) const;

		//Set default background color. Return true if ok, else false.
		bool setBackgroundColor(int new_color);
	};
}
#endif