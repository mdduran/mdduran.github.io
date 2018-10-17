package mdduran;

import ks.common.games.Solitaire;
import ks.common.model.BuildablePile;
import ks.common.model.Card;
import ks.common.model.Column;
import ks.common.model.Move;
import ks.common.model.Pile;


public class TableauToFoundationMove extends Move {
	Pile foundation;
	BuildablePile tableauColumn;
	Card cardBeingMoved;
	AmericanToad theGame;
	int rank;
	public TableauToFoundationMove(BuildablePile from, Card cardBeingMoved, Pile to, int rank) {
		super();
		this.tableauColumn = from;
		this.foundation = to;
		this.cardBeingMoved = cardBeingMoved;
		this.rank = rank;
	}
	@Override
	public boolean doMove(Solitaire game) {
		if(!valid(game)){
			return false;
		}
		foundation.add(cardBeingMoved);
		game.updateScore(+1);
		return true;
	}
	@Override
	public boolean undo(Solitaire game) {
		if(foundation.empty()){
			return false;
		}
		tableauColumn.add(foundation.get());
		game.updateScore(-1);
		return true;
	}
	@Override
	public boolean valid(Solitaire game) {
		boolean validation = false;
		if(foundation.empty() && cardBeingMoved.getRank() == this.rank){
			validation = true;
		}
		else if(!foundation.empty() && foundation.rank() == Card.KING && cardBeingMoved.getRank() == Card.ACE && cardBeingMoved.getSuit() == foundation.suit()
				&& foundation.count() <= 13){
			validation = true;
		}
		else if(!foundation.empty() && cardBeingMoved.getSuit() == foundation.suit() && cardBeingMoved.getRank() == foundation.rank()+1
				&& foundation.count() <= 13){
			validation = true;
		}
		else{validation = false;}
		
		return validation;
	}

}
