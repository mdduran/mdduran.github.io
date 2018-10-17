package mdduran;

import ks.common.games.Solitaire;
import ks.common.model.BuildablePile;
import ks.common.model.Card;
import ks.common.model.Column;
import ks.common.model.Move;
import ks.common.model.Pile;


public class WastePileToTableauMove extends Move {
	Pile wastePile;
	BuildablePile tableau;
	Card cardBeingMoved;
	public WastePileToTableauMove(Pile wastePile, Card cardBeingMoved, BuildablePile tableau) {
		this.wastePile = wastePile;
		this.cardBeingMoved = cardBeingMoved;
		this.tableau = tableau;
	}
	@Override
	public boolean doMove(Solitaire game) {
		if(!valid(game)){return false;}
		//take card off of the top of the stack
		tableau.add(cardBeingMoved);
		return true;
	}

	@Override
	public boolean undo(Solitaire game) {
		if(tableau.empty()){return false;}
		wastePile.add(tableau.get());
		return true;
	}

	@Override
	public boolean valid(Solitaire game) {
		boolean validation = false;
		if(!tableau.empty() && cardBeingMoved.getRank() == tableau.rank()-1 && cardBeingMoved.getSuit() == tableau.suit()){
			validation = true;
		}
		else if(tableau.empty()){
			validation = true;
		}
		
		return validation;
	}
	
}
