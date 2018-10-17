package mdduran;

import ks.common.games.Solitaire;
import ks.common.model.Card;
import ks.common.model.Move;
import ks.common.model.MultiDeck;
import ks.common.model.Pile;
/**
 * Move cards from top of deck to top of waste pile
 * @author Marco Duran
 *
 */
public class DrawCardMove extends Move {
	MultiDeck deck;
	Pile wastePile;
	
	public DrawCardMove(MultiDeck deck, Pile wastePile){
		this.deck = deck;
		this.wastePile = wastePile;
	}
	
	@Override
	public boolean doMove(Solitaire game) {
		if(!valid(game)){ return false;}
		
		Card card = deck.get();
		wastePile.add(card);
		game.updateNumberCardsLeft(-1);
		return true;
	}

	@Override
	public boolean undo(Solitaire game) {
		Card c = wastePile.get();
		deck.add(c);
		game.updateNumberCardsLeft(+1);
		return true;
	}

	@Override
	public boolean valid(Solitaire game) {
		return !deck.empty();
	}

}
