package mdduran;

import ks.common.games.Solitaire;
import ks.common.model.Card;
import ks.common.model.Move;
import ks.common.model.Pile;

/**
 * Move card from top of the waste pile to the top of the foundation pile
 * @author Marco
 *
 */
public class WastePileToFoundationMove extends Move {
	Pile wastePile;
	Card cardBeingDragged;
	Pile foundation;
	AmericanToad theGame;
	
	public WastePileToFoundationMove(Pile from,Card cardBeingDragged, Pile to, AmericanToad theGame){
		super();
		this.wastePile = from;
		this.cardBeingDragged = cardBeingDragged;
		this.foundation = to;
		this.theGame = theGame;
	}
	@Override
	public boolean doMove(Solitaire game) {
		if(!valid(game)){return false;}
		
		foundation.add(cardBeingDragged);
		game.updateScore(+1);
		return true;
		//move on to top of foundation
		
		
		
	}

	@Override
	public boolean undo(Solitaire game) {
		if(foundation.empty()){
			return false;
		}
		
		wastePile.add(foundation.get());
		game.updateScore(-1);
		return true;
	}

	@Override
	public boolean valid(Solitaire game) {
		boolean validation = false;
		if(foundation.empty() && cardBeingDragged.getRank() == theGame.getRankOfFoundation()){
			validation = true;
		}
		else if(!foundation.empty() && foundation.rank() == 13 && cardBeingDragged.getRank() == 1
				&& foundation.count() <= 13){
			validation = true;
		}
		else if(!foundation.empty() && cardBeingDragged.getRank() == foundation.peek().getRank()+1 
				&& cardBeingDragged.getSuit() == foundation.peek().getSuit() && foundation.count() <= 13){
			validation = true;
		}
		
		return validation;
		
	}

}
