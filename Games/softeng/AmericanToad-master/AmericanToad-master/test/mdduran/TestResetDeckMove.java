package mdduran;

import junit.framework.TestCase;
import ks.client.gamefactory.GameWindow;
import ks.common.model.MultiDeck;
import ks.launcher.Main;

public class TestResetDeckMove extends TestCase {
	public void testSimple(){
		AmericanToad americanToad = new AmericanToad();
		GameWindow gw = Main.generateWindow(americanToad, MultiDeck.OrderBySuit );
		DrawCardMove dcm = new DrawCardMove(americanToad.deck, americanToad.wastePile);
		while(americanToad.deck.empty() != true){
			dcm.doMove(americanToad);
		}
		ResetDeckMove rdm = new ResetDeckMove(americanToad.deck, americanToad.wastePile);
		assertTrue(rdm.valid(americanToad));
		rdm.doMove(americanToad);
		assertFalse(rdm.undo(americanToad));
	}
	public void testNonEmptyDeck(){
		AmericanToad americanToad = new AmericanToad();
		GameWindow gw = Main.generateWindow(americanToad, MultiDeck.OrderBySuit);
		ResetDeckMove rdm = new ResetDeckMove(americanToad.deck, americanToad.wastePile);
		assertFalse(rdm.valid(americanToad));
		assertFalse(rdm.doMove(americanToad));
	}
}
