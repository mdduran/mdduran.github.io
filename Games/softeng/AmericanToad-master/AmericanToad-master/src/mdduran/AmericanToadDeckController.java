package mdduran;


import ks.common.controller.SolitaireReleasedAdapter;
import ks.common.model.Move;
import ks.common.model.MultiDeck;
import ks.common.model.Pile;

public class AmericanToadDeckController extends SolitaireReleasedAdapter {
	/** The game. */
	protected AmericanToad theGame;

	/** The WastePile of interest. */
	protected Pile wastePile;

	/** The Deck of interest. */
	protected MultiDeck deck;

	/**
	 * AmericanToadDeckController constructor comment.
	 */
	public AmericanToadDeckController(AmericanToad theGame, MultiDeck d, Pile wastePile) {
		super(theGame);

		this.theGame = theGame;
		this.wastePile = wastePile;
		this.deck = d;
	}

	/**
	 * Coordinate reaction to the beginning of a Drag Event. In this case,
	 * no drag is ever achieved, and we simply deal upon the press.
	 */
	public void mousePressed (java.awt.event.MouseEvent me) {
		if(!deck.empty()){
			// Attempting a DrawCardMove
			Move m = new DrawCardMove (deck, wastePile);
			if (m.doMove(theGame)) {
				theGame.pushMove (m);     // Successful Draw Move
				theGame.refreshWidgets(); // refresh updated widgets.
			}
		}
		else{
			Move m = new ResetDeckMove(deck, wastePile);
			if(m.doMove(theGame)){
				theGame.pushMove(m);
				theGame.refreshWidgets();
			}
		}
		
	}

}
