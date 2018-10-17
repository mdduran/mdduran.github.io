package mdduran;

import junit.framework.TestCase;
import ks.client.gamefactory.GameWindow;
import ks.common.model.Card;
import ks.common.model.MultiDeck;
import ks.launcher.Main;

public class TestReserveToFoundationMove extends TestCase {
	public void testEmpty(){
		AmericanToad at = new AmericanToad();
		GameWindow gw = Main.generateWindow(at, MultiDeck.OrderBySuit);
		Card testQueen = new Card(Card.QUEEN, Card.CLUBS);
		at.reserveColumn.removeAll();
		at.reserveColumn.add(testQueen);
		ReserveToFoundationMove rtfm = new ReserveToFoundationMove(at.reserveColumn, at.reserveColumn.peek(),at.foundation2, at );
		assertTrue(rtfm.valid(at));
		assertTrue(rtfm.doMove(at));
		rtfm.doMove(at);
		assertTrue(rtfm.undo(at));
		
		at.foundation2.removeAll();
		assertFalse(rtfm.undo(at));
	}
	
	public void test2(){
		AmericanToad at = new AmericanToad();
		GameWindow gw = Main.generateWindow(at, MultiDeck.OrderBySuit);
		Card testAce = new Card(Card.ACE, Card.DIAMONDS);
		Card testKing = new Card(Card.KING, Card.DIAMONDS);
		at.reserveColumn.removeAll();
		at.reserveColumn.add(testAce);
		at.foundation1.add(testKing);
		ReserveToFoundationMove rtfm2 = new ReserveToFoundationMove(at.reserveColumn, at.reserveColumn.peek(), at.foundation1, at);
		assertTrue(rtfm2.valid(at));
		assertTrue(rtfm2.doMove(at));
		
	}
	
	public void test3(){
		AmericanToad at = new AmericanToad();
		GameWindow gw = Main.generateWindow(at, MultiDeck.OrderBySuit);
		Card testAce = new Card(Card.ACE, Card.DIAMONDS);
		Card testKing = new Card(Card.KING, Card.DIAMONDS);
		at.reserveColumn.removeAll();
		at.reserveColumn.add(testAce);
		at.reserveColumn.add(testKing);
		ReserveToFoundationMove rtfm2 = new ReserveToFoundationMove(at.reserveColumn, at.reserveColumn.peek(), at.foundation1, at);
		assertTrue(rtfm2.valid(at));
		assertTrue(rtfm2.doMove(at));
		
	}
	

}
