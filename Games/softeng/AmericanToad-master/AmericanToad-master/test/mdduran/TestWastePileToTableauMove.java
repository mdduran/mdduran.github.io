package mdduran;

import junit.framework.TestCase;
import ks.client.gamefactory.GameWindow;
import ks.common.model.MultiDeck;
import ks.launcher.Main;

public class TestWastePileToTableauMove extends TestCase {
	public void testSimple(){
		AmericanToad americanToad = new AmericanToad();
		GameWindow gw = Main.generateWindow(americanToad, MultiDeck.OrderByRank);
		WastePileToTableauMove wptt = new WastePileToTableauMove(americanToad.wastePile, americanToad.wastePile.get(), americanToad.tableau6);
		assertTrue(wptt.valid(americanToad));
		assertTrue(wptt.doMove(americanToad));
		wptt.doMove(americanToad);
		assertEquals(americanToad.wastePile.count(), 0);
		wptt.undo(americanToad);
		assertEquals(americanToad.wastePile.count(), 1);
		//draw a card then add a card from the wastepile
		DrawCardMove dcm = new DrawCardMove(americanToad.deck, americanToad.wastePile);
		americanToad.tableau1.removeAll();
		dcm.doMove(americanToad);
		WastePileToTableauMove wptt1 = new WastePileToTableauMove(americanToad.wastePile, americanToad.wastePile.get(), americanToad.tableau1);
		assertTrue(wptt1.valid(americanToad));
		wptt1.doMove(americanToad);
		americanToad.tableau1.removeAll();
		assertFalse(wptt1.undo(americanToad));
		
	}
}
