package mdduran;

import junit.framework.TestCase;
import ks.client.gamefactory.GameWindow;
import ks.common.model.Card;
import ks.common.model.MultiDeck;
import ks.launcher.Main;

public class TestReserveToTableau extends TestCase {
	public void testSimple(){
		AmericanToad at = new AmericanToad();
		GameWindow gw = Main.generateWindow(at, MultiDeck.OrderBySuit);
		//top card on column is 9 diamonds
		at.tableau1.removeAll();
		ReserveToTableauMove rttm = new ReserveToTableauMove(at.reserveColumn, at.reserveColumn.get(), at.tableau1 );
		assertTrue(rttm.valid(at));
		assertTrue(rttm.doMove(at));
		rttm.doMove(at);
		assertTrue(rttm.undo(at));
		
	}
	public void test2(){
		AmericanToad at = new AmericanToad();
		GameWindow gw = Main.generateWindow(at, MultiDeck.OrderByRank);
		Card testFive = new Card(Card.FIVE, Card.CLUBS);
		Card testFour = new Card(Card.FOUR, Card.CLUBS);
		at.reserveColumn.removeAll();
		at.tableau1.removeAll();
		at.reserveColumn.add(testFour);
		at.tableau1.add(testFive);
		ReserveToTableauMove rttm = new ReserveToTableauMove(at.reserveColumn, at.reserveColumn.get(), at.tableau1 );
		assertTrue(rttm.valid(at));
		rttm.doMove(at);
		at.tableau1.removeAll();
		assertFalse(rttm.undo(at));
		
	}
}
