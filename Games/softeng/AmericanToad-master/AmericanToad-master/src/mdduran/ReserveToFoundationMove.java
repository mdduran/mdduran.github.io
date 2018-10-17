package mdduran;

import ks.common.games.Solitaire;
import ks.common.model.Card;
import ks.common.model.Column;
import ks.common.model.Move;
import ks.common.model.Pile;

public class ReserveToFoundationMove extends Move{
	Column reserveColumn;
	Pile foundation;
	Card cardBeingMoved;
	AmericanToad theGame;
	public ReserveToFoundationMove(Column from, Card cardBeingMoved, Pile to, AmericanToad theGame) {
		super();
		this.reserveColumn = from;
		this.foundation = to;
		this.cardBeingMoved = cardBeingMoved;
		this.theGame = theGame;
	}
	@Override
	public boolean doMove(Solitaire game) {
		if(!valid(game)){
			return false;
		}
		foundation.add(cardBeingMoved);
		return true;
		
	}
	@Override
	public boolean undo(Solitaire game) {
		if(foundation.empty()){
			return false;
		}
		//undo
		reserveColumn.add(foundation.get());
		return true;
	}
	@Override
	public boolean valid(Solitaire game) {
		boolean validation = false;
		if(foundation.empty() && cardBeingMoved.getRank() ==  theGame.getRankOfFoundation()){
			validation = true;
		}
		else if(!foundation.empty() && foundation.rank() == 13 && cardBeingMoved.getRank() == 1 && foundation.count() <= 13){
			validation = true;
		}
		else if(!foundation.empty() && cardBeingMoved.getSuit() == foundation.suit() && cardBeingMoved.getRank() == foundation.rank()+1
				&& foundation.count() <= 13){
			validation = true;
		}
		//if there is a full foundation pile, return false
		
		return validation;
	}

}
