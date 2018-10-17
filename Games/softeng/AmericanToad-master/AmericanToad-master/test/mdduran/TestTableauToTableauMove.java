package mdduran;

import junit.framework.TestCase;
import ks.client.gamefactory.GameWindow;
import ks.common.model.Card;
import ks.common.model.Column;
import ks.common.model.MultiDeck;
import ks.launcher.Main;

public class TestTableauToTableauMove extends TestCase {
	public void testSimple(){
		AmericanToad at = new AmericanToad();
		GameWindow gw = Main.generateWindow(at, 0);
		Card testSev = new Card(Card.SEVEN, Card.CLUBS);
		Card testEight = new Card(Card.EIGHT, Card.CLUBS);
		at.tableau8.removeAll();
		at.tableau4.removeAll();
		
		at.tableau8.add(testSev);
		at.tableau4.add(testEight);
		Column newcol = new Column();
		newcol.add(testSev);
		assertEquals(at.tableau8.rank(), testSev.getRank());
		TableauToTableauMove ttfm = new TableauToTableauMove(at.tableau8,newcol , at.tableau4, at.tableau8.count());
		assertTrue(ttfm.valid(at));
		assertTrue(ttfm.doMove(at));
		ttfm.doMove(at);
		assertFalse(at.tableau4.count() < newcol.count());
		assertTrue(ttfm.undo(at));
	}
	
	public void testEmpty(){
		AmericanToad at = new AmericanToad();
		GameWindow gw = Main.generateWindow(at, 0);
		Card testSev = new Card(Card.SEVEN, Card.CLUBS);
		at.tableau8.removeAll();
		at.tableau4.removeAll();
		at.tableau8.add(testSev);
		Column newcol = new Column();
		newcol.add(testSev);
		TableauToTableauMove ttfm = new TableauToTableauMove(at.tableau8,newcol , at.tableau4, at.tableau8.count());
		assertTrue(ttfm.valid(at));
		assertTrue(ttfm.doMove(at));
		ttfm.doMove(at);
		at.tableau4.removeAll();
		assertFalse(ttfm.undo(at));
		
	}
	
	
}
