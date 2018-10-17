package mdduran;

import ks.common.games.Solitaire;
import ks.common.model.Deck;
import ks.common.model.Pile;

/**
 * Represents the reset of the deck.
 * <p>
 * Note that this move cannot be undone.
 * <p> *
 * 
 * @author Marco Duran
 *
 */
public class ResetDeckMove extends ks.common.model.Move {
	/** The deck */
	protected Deck deck;
	
	/** Tableau Piles */
	protected Pile tableauPile1;
	protected Pile tableauPile2;
	protected Pile tableauPile3;
	protected Pile tableauPile4;
	protected Pile tableauPile5;
	protected Pile tableauPile6;
	protected Pile tableauPile7;
	protected Pile tableauPile8;
	
	/** Foundation Piles */
	protected Pile foundationPile1;
	protected Pile foundationPile2;
	protected Pile foundationPile3;
	protected Pile foundationPile4;
	protected Pile foundationPile5;
	protected Pile foundationPile6;
	protected Pile foundationPile7;
	protected Pile foundationPile8;
	
	/** Waste Pile */
	protected Pile wastePile;
	
	/** Reserve Pile */
	protected Pile reservePile;
	
	/**
	 * ResetDeckMove constructor
	 */
	public ResetDeckMove(Deck d, Pile waste){
		super();
		
		this.deck = d;
		this.wastePile = waste;
	}
	
	public boolean doMove(Solitaire theGame){
		if(valid(theGame) == false){
			return false;
		}
		//Execute:
		
	
		while(!wastePile.empty()){
			deck.add(wastePile.get());
			
		}
		//finally update the total number
		
		return true;
	}	
	
	public boolean undo(ks.common.games.Solitaire game){
		//cannot undo this move
		return false;
	}
	
	//Validate this move
	public boolean valid(ks.common.games.Solitaire game){
		boolean validation = false;
		
		if(deck.empty()){
			validation = true;
		}
		else{
			validation = false;
		}
		return validation;
	}
}
