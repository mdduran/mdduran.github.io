package mdduran;

import ks.common.games.Solitaire;
import ks.common.model.BuildablePile;
import ks.common.model.Card;
import ks.common.model.Column;
import ks.common.model.Move;

public class ReserveToTableauMove extends Move {
	Column reserve;
	BuildablePile tableau;
	Card cardBeingMoved;
	public ReserveToTableauMove(Column from, Card cardBeingMoved,  BuildablePile to) {
		super();
		this.reserve = from;
		this.tableau = to;
		this.cardBeingMoved = cardBeingMoved;
	}
	@Override
	public boolean doMove(Solitaire game) {
		if(!valid(game) || reserve.empty()){
			return false;
		}
		tableau.add(cardBeingMoved);
		return true;
		
	}
	@Override
	public boolean undo(Solitaire game) {
		if(tableau.empty()){
			return false;
		}
		reserve.add(tableau.get());
		return true;
	}
	@Override
	public boolean valid(Solitaire game) {
		boolean validation = false;
		if(tableau.empty() != false){
			validation = true;
		}
		if(!tableau.empty() && cardBeingMoved.getRank() < tableau.rank() && cardBeingMoved.getSuit() == tableau.suit() ){
			validation = true;
		}
		return validation;
	}
	
}
