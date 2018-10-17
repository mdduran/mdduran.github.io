package mdduran;

import java.awt.event.MouseEvent;

import junit.framework.TestCase;
import ks.client.gamefactory.GameWindow;
import ks.common.games.Solitaire;
import ks.common.model.Card;
import ks.common.model.MultiDeck;
import ks.common.view.Widget;
import ks.launcher.Main;

public class TestTableauController extends TestCase {
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
		
		at.tableau1.removeAll();
		at.tableau2.removeAll();
		at.tableau3.removeAll();
		at.tableau4.removeAll();
		at.tableau5.removeAll();
		at.tableau6.removeAll();
		at.tableau7.removeAll();
		at.tableau8.removeAll();
		
		Card testOne = new Card(Card.ACE, Card.CLUBS);
		Card testTwo = new Card(Card.TWO, Card.CLUBS);
		Card testThree = new Card(Card.THREE, Card.CLUBS);
		Card testFour = new Card(Card.FOUR, Card.CLUBS);
		Card testFive = new Card(Card.FIVE, Card.CLUBS);
		Card testSix = new Card(Card.SIX, Card.CLUBS);
		Card testSeven = new Card(Card.SEVEN, Card.CLUBS);
		Card testEight = new Card(Card.EIGHT, Card.CLUBS);
		
		at.tableau1.add(testOne);
		at.tableau2.add(testTwo);
		at.tableau3.add(testThree);
		at.tableau4.add(testFour);
		at.tableau5.add(testFive);
		at.tableau6.add(testSix);
		at.tableau7.add(testSeven);
		at.tableau8.add(testEight);
		
		MouseEvent press = createPressed(at, at.tableauView1, 0, 0);
		at.tableauView1.getMouseManager().handleMouseEvent(press);
		//assertEquals(testOne, at.tableau1.peek());
		//assertEquals(testTwo, at.tableau2.peek());
		
		
		
		MouseEvent release = createReleased(at, at.tableauView2, 0, 0);
		at.tableauView2.getMouseManager().handleMouseEvent(release);
		System.out.println(at.tableauView1.getX());
		System.out.println(at.tableauView2.getX());
		System.out.println(at.tableauView1.getY());
		System.out.println(at.tableauView2.getY());
		assertEquals(at.tableauView1.getX(), 113);
		System.out.println(press.toString());
		System.out.println(release.toString());
		System.out.println(at.tableau2.get().toString());
		//assertEquals(testOne, at.tableau2.peek());
		
		gw.dispose();
	}
	
	public void testWastePileController(){
		AmericanToad at = new AmericanToad();
		GameWindow gw = Main.generateWindow(at, MultiDeck.OrderBySuit);
		//at.wastePile.removeAll();
		
		MouseEvent press = createPressed(at, at.wastePileView, 0, 0);
		at.wastePileView.getMouseManager().handleMouseEvent(press);
		
	}
	
	public void testReserveController(){
		AmericanToad at = new AmericanToad();
		GameWindow gw = Main.generateWindow(at, MultiDeck.OrderBySuit);
		//at.wastePile.removeAll();
		
		MouseEvent press = createPressed(at, at.reserveColumnView, 0, 0);
		at.reserveColumnView.getMouseManager().handleMouseEvent(press);
		
		
	}
}
