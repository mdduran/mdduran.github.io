package mdduran;

import ks.common.model.BuildablePile;
import ks.common.model.Card;
import ks.common.model.Column;
import ks.common.model.Move;
import ks.common.model.Pile;
import ks.common.model.Stack;
import ks.common.view.BuildablePileView;
import ks.common.view.CardView;
import ks.common.view.ColumnView;
import ks.common.view.Container;
import ks.common.view.Widget;

public class AmericanToadTableauController extends java.awt.event.MouseAdapter {
	//American toad game
	protected AmericanToad theGame;
	
	//Specific  tableau column view being controlled
	protected BuildablePileView src;
	
	//TableauController constructor
	public AmericanToadTableauController(AmericanToad theGame, BuildablePileView tableau){
		super();
		this.theGame = theGame;
		this.src = tableau;
	}
	
	/**
	 * Coordinate reaction to the beginning of a Drag Event.
	 * <p>
	 * Note: There is no way to differentiate between a press that
	 *       will become part of a double click vs. a click that will
	 *       be held and dragged. Only releaseCardController will be
	 *       able to help us out with that one.
	 * <p>
	 * Note: uses KombatSolitaire v1.6 capability of having container remember drag source widget.
	 * <p>
	 * Creation date: (10/4/01 6:05:55 PM)
	 * @param me java.awt.event.MouseEvent
	 */
	public void mousePressed (java.awt.event.MouseEvent me) {
		Container c = theGame.getContainer();

		/** Return if there is no card to be chosen. */
		BuildablePile bigCol = (BuildablePile) src.getModelElement();
		if (bigCol.count() == 0) {
			return;
		}

//		// Could be something! Verify that the user clicked on the TOP card in the Column.
//		// Note that this method will alter the model for columnView if the condition is met.
//		CardView cardView = src.getCardViewForTopCard(me);
//		if (cardView == null) {
//			return;
//		}
		
		//Also will have a column view 
		ColumnView colView = src.getColumnView(me);
		if(colView == null){
			return;
		}
		//Check conditions
		Column column = (Column) colView.getModelElement();
		if(column == null){
			System.err.println("AmericanToad::pressCardController(): Unexpectedly encountered a Dragging Object during a Mouse press. ");
			return;
		}
		
		//verify that column has american toad qualities
		if((column.count() <= 0)){
			bigCol.push(column);
			java.awt.Toolkit.getDefaultToolkit().beep();
			return;
		}
		
		// If we get here, then the user has indeed clicked on the top card in the ColumnView and
		// we are able to now move it on the screen at will. For smooth action, the bounds for the
		// cardView widget reflect the original card location on the screen.
		Widget w = c.getActiveDraggingObject();
		if (w != Container.getNothingBeingDragged()) {
			System.err.println ("AmericanToad::pressCardController(): Unexpectedly encountered a Dragging Object during a Mouse press.");
			return;
		}

		// Tell container which object is being dragged, and where in that widget the mouse was clicked.
		
		c.setActiveDraggingObject (colView, me);

		// Have container remember who initiated the drag
		c.setDragSource (src);

		// we simply redraw our source pile to avoid flicker,
		// rather than refreshing all widgets...
		src.redraw();
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

//		/** Must be the CardView widget. */
//		CardView cardView = (CardView) w;
//		Card theCard = (Card) cardView.getModelElement();
//		if (theCard == null) {
//			System.err.println ("AmericanToad::releaseCardController(): somehow CardView model element is null.");
//			return;
//		}

		/** Recover the From Column or wastePile */
		Widget fromWidget = c.getDragSource();
		if (fromWidget == null) {
			System.err.println ("AmericanToad::releaseCardController(): somehow fromWidget is null.");
			c.releaseDraggingObject();
			return;
		}
		Stack from = (Stack) fromWidget.getModelElement();
		

		BuildablePile toColumn = (BuildablePile) src.getModelElement();
		// Try to make the move
		//if frompile is a wastepile, try this move
		if(c.getDragSource().equals(theGame.wastePileView)){
			CardView cardView = (CardView) w;
			Card theCard = (Card) cardView.getModelElement();
			if (theCard == null) {
				System.err.println ("AmericanToad::releaseCardController(): somehow CardView model element is null.");
				return;
			}
			
			Pile fromPile = (Pile) from;
			Move m = new WastePileToTableauMove (fromPile, theCard, toColumn);
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
			CardView cardView = (CardView) w;
			Card theCard = (Card) cardView.getModelElement();
			if (theCard == null) {
				System.err.println ("AmericanToad::releaseCardController(): somehow CardView model element is null.");
				return;
			}
			
			Column fromReserve = (Column) from;
			Move m = new ReserveToTableauMove (fromReserve, theCard, toColumn);
			if (m.doMove (theGame)) {
				// Successful move!  
				// add move to our set of moves
				theGame.pushMove (m);
			} else {
				// Invalid move. Restore dragging widget to source
				fromWidget.returnWidget (w);
			}
		}
		else if (fromWidget instanceof BuildablePileView){
			ColumnView columnView = (ColumnView) w;
			Column column = (Column) columnView.getModelElement();
			if(column == null){
				System.err.println("AmericanToad::releaseColumnController():: somehow ColumnView model element is null.");
				return;
			}
			if(fromWidget == src){
				toColumn.push(column);
			} else{
				BuildablePile fromTableau = (BuildablePile) from;
				Move m = new TableauToTableauMove (fromTableau, column, toColumn, column.count());
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
					// Invalid move. Restore to original column
					fromTableau.push(column);
				}
			}
			
		}
		c.releaseDraggingObject();    // also releases dragSource

		c.repaint();
	}
	
	
}