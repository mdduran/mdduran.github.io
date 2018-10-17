package mdduran;

import ks.common.games.Solitaire;
import ks.common.model.BuildablePile;
import ks.common.model.Column;
import ks.common.model.Move;
import ks.common.model.Stack;


public class TableauToTableauMove extends Move{
	BuildablePile fromTableau;
	BuildablePile toTableau;
	int numCards;
	Column colBeingMoved;
	public TableauToTableauMove(BuildablePile from, Column colBeingMoved, BuildablePile to, int numCards){
		super();
		this.fromTableau = from;
		this.toTableau = to;
		this.colBeingMoved = colBeingMoved;
		this.numCards = numCards;
		
		
	}
	@Override
	public boolean doMove(Solitaire game) {
		if(!valid(game)){
			return false;
		}
//		if(colBeingMoved == null){
//			fromTableau.select(numCards);
//			Stack st = fromTableau.getSelected();
//			toTableau.push(st);
//		}
		//else{
			toTableau.push(colBeingMoved);
		//}
		
		return true;
	}
	@Override
	public boolean undo(Solitaire game) {
		if (toTableau.count() < numCards) return false;
		
		// We know the number of cards moved, so we select them, extract the
		// stack, and move them all back to the fromPile.
		toTableau.select (numCards);
		Stack st = toTableau.getSelected();
		fromTableau.push (st);
		return true;
	}
	@Override
	public boolean valid(Solitaire game) {
		boolean validation = false;
		//If move has not happened yet, we must extract the desired column to move.
		Column targetCol;
//		if(colBeingMoved == null){
//			targetCol = new Column();
//			for(int i = numCards; i >=1; i--){
//				targetCol.add(fromTableau.peek(fromTableau.count() - i));
//			}
//		}
		//else{
			targetCol = colBeingMoved;
		//}
		if(toTableau.empty() != false){
			validation = true;
		}
		else if(!toTableau.empty() && colBeingMoved.rank() < toTableau.rank() && colBeingMoved.suit() == toTableau.suit()){
			validation = true;
		}
		else{
			validation = false;
		}
		return validation;
	}
}
