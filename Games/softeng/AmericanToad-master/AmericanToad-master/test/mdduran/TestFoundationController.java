package mdduran;

import java.awt.event.MouseEvent;

import junit.framework.TestCase;
import ks.client.gamefactory.GameWindow;
import ks.common.games.Solitaire;
import ks.common.model.MultiDeck;
import ks.common.view.Widget;
import ks.launcher.Main;

public class TestFoundationController extends TestCase {
	public MouseEvent createPressed (Solitaire game, Widget view, int dx, int dy) {
		MouseEvent me = new MouseEvent(game.getContainer(), MouseEvent.MOUSE_PRESSED, 
				System.currentTimeMillis(), 0, 
				view.getX()+dx, view.getY()+dy, 0, false);
		return me;
	}
	
	/** (dx,dy) are offsets into the widget space. Feel Free to Use as Is. */
	public MouseEvent createReleased (Solitaire game, Widget view, int dx, int dy) {
		MouseEvent me = new MouseEvent(game.getContainer(), MouseEvent.MOUSE_RELEASED, 
				System.currentTimeMillis(), 0, 
				view.getX()+dx, view.getY()+dy, 0, false);
		return me;
	}
	
	public void testSimple(){
		AmericanToad at = new AmericanToad();
		GameWindow gw = Main.generateWindow(at, MultiDeck.OrderBySuit);
		
		MouseEvent press = createPressed(at, at.tableauView8, 0, 0);
		at.tableauView8.getMouseManager().handleMouseEvent(press);
		
		
		MouseEvent released = createReleased(at, at.foundationView2, 0, 0);
		at.foundationView2.getMouseManager().handleMouseEvent(released);
		
		
	}
}
