package mdduran;

import junit.framework.TestCase;
import ks.client.gamefactory.GameWindow;
import ks.common.model.Card;
import ks.common.model.MultiDeck;
import ks.launcher.Main;

public class TestWastePileToFoundationMove extends TestCase {
	public void testSimple(){
		AmericanToad americanToad = new AmericanToad();
		GameWindow gw = Main.generateWindow(americanToad, MultiDeck.OrderBySuit);
		DrawCardMove dcm = new DrawCardMove(americanToad.deck, americanToad.wastePile);
		for(int i = 0; i < 12; i++){
			dcm.doMove(americanToad);
		}
		WastePileToFoundationMove wtfm = new WastePileToFoundationMove(americanToad.wastePile,americanToad.wastePile.get(), americanToad.foundation8, americanToad);
		assertTrue(americanToad.foundation8.empty());
		assertTrue(wtfm.valid(americanToad));
		wtfm.doMove(americanToad);
		assertEquals(63, americanToad.deck.count());
	
	}
	
	public void testaddToNonemptyFoundation(){
		AmericanToad americanToad = new AmericanToad();
		GameWindow gw = Main.generateWindow(americanToad, MultiDeck.OrderByRank);
		DrawCardMove dcm = new DrawCardMove(americanToad.deck, americanToad.wastePile);
		//48 times
		for(int i = 0; i < 47; i++){
			dcm.doMove(americanToad);
		}
		//add to empty wastepile
		WastePileToFoundationMove wtfm2 = new WastePileToFoundationMove(americanToad.wastePile, americanToad.wastePile.get(), americanToad.foundation1, americanToad);
		assertTrue(wtfm2.valid(americanToad));
		assertTrue(wtfm2.doMove(americanToad));
		assertTrue(!americanToad.foundation1.empty());
		//assertTrue(americanToad.wastePile.get().getRank() == americanToad.foundation1.peek().getRank()+1);
		wtfm2.doMove(americanToad);
		assertEquals(americanToad.foundation1.count(), 2);
	}
	
	public void testUndo(){
		AmericanToad americanToad = new AmericanToad();
		GameWindow gw = Main.generateWindow(americanToad, MultiDeck.OrderBySuit);
		DrawCardMove dcm = new DrawCardMove(americanToad.deck, americanToad.wastePile);
		for(int i = 0; i < 12; i++){
			dcm.doMove(americanToad);
		}
		WastePileToFoundationMove wtfm = new WastePileToFoundationMove(americanToad.wastePile,americanToad.wastePile.get(), americanToad.foundation8, americanToad);
		assertTrue(wtfm.valid(americanToad));
		assertTrue(wtfm.doMove(americanToad));
		
		wtfm.doMove(americanToad);
		assertTrue(wtfm.undo(americanToad));
		wtfm.undo(americanToad);
		assertEquals(americanToad.wastePile.count(), 13);
		
	}
	
	public void testAllCases(){
		AmericanToad at = new AmericanToad();
		GameWindow gw = Main.generateWindow(at, 0);
		Card fiveClub = new Card(Card.FIVE, Card.CLUBS);
		Card sixClub = new Card(Card.SIX, Card.CLUBS);
		at.foundation1.add(fiveClub);
		at.wastePile.add(sixClub);
		WastePileToFoundationMove wptf3 = new WastePileToFoundationMove(at.wastePile, at.wastePile.get(), at.foundation1, at);
		assertFalse(at.foundation1.empty());
		//assertEquals(at.wastePile.get().getRank(), at.foundation1.peek().getRank()+1);
		assertEquals(at.wastePile.get().getSuit(), at.foundation1.peek().getSuit());
		assertTrue(at.foundation1.count() <= 13);
		wptf3.doMove(at);

	}
	
	public void test5(){
		AmericanToad at = new AmericanToad();
		GameWindow gw = Main.generateWindow(at, 0);
		Card aceClub = new Card(Card.ACE, Card.CLUBS);
		Card kingClub = new Card(Card.KING, Card.CLUBS);
		at.wastePile.add(aceClub);
		at.foundation2.add(kingClub);
		assertEquals(at.wastePile.get().getRank(), Card.ACE);
		assertEquals(at.foundation2.get().getRank(), Card.KING);
		assertTrue(at.foundation2.count() <= 13);
		
		WastePileToFoundationMove wptf4 = new WastePileToFoundationMove(at.wastePile, at.wastePile.get(), at.foundation2, at);
		
		assertFalse(wptf4.valid(at));
		assertFalse(wptf4.doMove(at));
		wptf4.doMove(at);
	}
	
	public void test6(){
		AmericanToad at = new AmericanToad();
		GameWindow gw = Main.generateWindow(at, MultiDeck.OrderBySuit);
		Card aceD = new Card(Card.ACE, Card.DIAMONDS);
		Card kingD = new Card(Card.KING, Card.DIAMONDS);
		at.foundation1.add(kingD);
		at.wastePile.add(aceD);
		
		WastePileToFoundationMove wptf5 = new WastePileToFoundationMove(at.wastePile, at.wastePile.get(), at.foundation1, at);
		assertTrue(wptf5.valid(at));
		assertTrue(wptf5.doMove(at));
		
	}
}
