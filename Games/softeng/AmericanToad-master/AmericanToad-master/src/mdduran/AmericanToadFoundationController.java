package mdduran;




import ks.common.model.BuildablePile;
import ks.common.model.Card;
import ks.common.model.Column;
import ks.common.model.Move;
import ks.common.model.Pile;
import ks.common.model.Stack;
import ks.common.view.CardView;
import ks.common.view.ColumnView;
import ks.common.view.Container;
import ks.common.view.PileView;
import ks.common.view.Widget;

public class AmericanToadFoundationController extends java.awt.event.MouseAdapter {

	/** The American Toad Game */
	protected AmericanToad theGame;
	/** The specific Foundation pileView being controlled. */
	protected PileView src;
	/**
	 * FoundationController constructor comment.
	 */
	public AmericanToadFoundationController(AmericanToad theGame, PileView foundation){
		super();
		
		this.theGame = theGame;
		this.src = foundation;
	}
	/**
	 * Coordinate reaction to the completion of a Drag Event.
	 * <p>
	 * Note: if cv is null, then it is assumed that the mouse was released on a non-ColumnView Widget
	 * and this is a sign that no move has been made by the user. When this happens, the card must
	 * be returned to the originating column from which it was dragged.
	 * <p>
	 * Note: uses KombatSolitaire v1.6 capability of having container remember drag source widget.
	 * <p>
	 * Creation date: (10/4/01 6:56:34 PM)
	 * @param cv edu.wpi.cs.solitaire.common.view.ColumnView
	 * @param me java.awt.event.MouseEvent
	 */
	public void mouseReleased (java.awt.event.MouseEvent me) {
		Container c = theGame.getContainer();

		/** Return if there is no card being dragged chosen. */
		Widget w = c.getActiveDraggingObject();
		if (w == Container.getNothingBeingDragged()){
			c.releaseDraggingObject();
			return;
		}
		
		

		/** Recover the From Column */
		Widget fromWidget = c.getDragSource();
		if (fromWidget == null) {
			System.err.println ("AmericanToad::releaseCardController(): somehow fromWidget is null.");
			return;
		}
		Stack from = (Stack) fromWidget.getModelElement();
		

		Pile toPile = (Pile) src.getModelElement();
		
		// Try to make the move
		//if frompile is a wastepile, try this move
		if(c.getDragSource().equals(theGame.wastePileView)){
			/** Must be the CardView widget. */
			CardView cardView = (CardView) w;
			Card theCard = (Card) cardView.getModelElement();
			
			if (theCard == null) {
				System.err.println ("AmericanToad::releaseCardController(): somehow CardView model element is null.");
				return;
			}
			Pile fromPile = (Pile) from;
			Move m = new WastePileToFoundationMove (fromPile, theCard, toPile, theGame);
			if (m.doMove (theGame)) {
				// Successful move!  
				// add move to our set of moves
				theGame.pushMove (m);
			} else {
				// Invalid move. Restore dragging widget to source
				fromWidget.returnWidget (w);
			}
		}
		else if(c.getDragSource().equals(theGame.reserveColumnView)){
			/** Must be the CardView widget. */
			CardView cardView = (CardView) w;
			Card theCard = (Card) cardView.getModelElement();
			
			if (theCard == null) {
				System.err.println ("AmericanToad::releaseCardController(): somehow CardView model element is null.");
				return;
			}
			Column fromReserve = (Column) from;
			Move m = new ReserveToFoundationMove (fromReserve, theCard, toPile, theGame);
			if (m.doMove (theGame)) {
				// Successful move!  
				// add move to our set of moves
				theGame.pushMove (m);
			} else {
				// Invalid move. Restore dragging widget to source
				fromWidget.returnWidget (w);
			}
		}
		else{
			BuildablePile fromTableau = (BuildablePile) from;
			/** Must be the ColumnView widget being dragged. */
			ColumnView columnView = (ColumnView) w;
			Column col = (Column) columnView.getModelElement();
			if (col == null) {
				System.err.println ("FoundationController::mouseReleased(): somehow ColumnView model element is null.");
				c.releaseDraggingObject();			
				return;
			}

			Move m = new TableauToFoundationMove (fromTableau, col.peek(), toPile, theGame.getRankOfFoundation());
			if (m.doMove (theGame)) {
				// Successful move!  
				// add move to our set of moves
				theGame.pushMove (m);
				if(fromTableau.empty()){

					Move autoReserveToTableau = new ReserveToTableauMove(theGame.reserveColumn, theGame.reserveColumn.get(), fromTableau);
					autoReserveToTableau.doMove(theGame);
					theGame.pushMove(autoReserveToTableau);
				}
				
			} else {
				// Invalid move. Restore dragging widget to source
				fromWidget.returnWidget (w);
			  }
		}
		c.releaseDraggingObject();    // also releases dragSource

		c.repaint();
	}
}
