package mdduran;

import java.awt.Dimension;

import ks.common.controller.SolitaireMouseMotionAdapter;
import ks.common.games.Solitaire;
import ks.common.games.SolitaireUndoAdapter;
import ks.common.model.BuildablePile;
import ks.common.model.Column;
import ks.common.model.MultiDeck;
import ks.common.model.Pile;
import ks.common.view.BuildablePileView;
import ks.common.view.CardImages;
import ks.common.view.ColumnView;
import ks.common.view.DeckView;
import ks.common.view.IntegerView;
import ks.common.view.PileView;
import ks.launcher.Main;

public class AmericanToad extends Solitaire {
	MultiDeck deck;
	DeckView deckView;
	Pile wastePile;
	PileView wastePileView;
	Pile foundation1,foundation2,foundation3,foundation4,foundation5,foundation6,foundation7,foundation8; //Foundation piles
	PileView foundationView1, foundationView2, foundationView3, foundationView4, foundationView5, foundationView6, foundationView7, foundationView8;//foundation pile views 
	BuildablePile tableau1, tableau2, tableau3, tableau4, tableau5, tableau6, tableau7, tableau8;//tableau
	BuildablePileView tableauView1, tableauView2,tableauView3, tableauView4, tableauView5, tableauView6, tableauView7, tableauView8;
	Column reserveColumn;
	ColumnView reserveColumnView;
	int rankOfFoundation;
	int numDeckPasses;

	IntegerView scoreView;
	
	@Override
	public String getName(){
		return "mdduran-AmericanToad";
	}

	@Override
	public boolean hasWon() {//if your score is equal to 103 this occurs when you put all of the cards in the foundation piles
		if(score.getValue() == 103){
			return true;
		}
		return false;
	}

	@Override
	public void initialize() {
		initializeModel(getSeed());
		initializeView();
		initializeControllers();
		
		//make a for loop to deal cards to reserve piles
		for(int i = 0; i <= 18; i++){
			reserveColumn.add(deck.get());
		}
		
		//deal one card to each of the tableau piles
		tableau1.add(deck.get());
		tableau2.add(deck.get());
		tableau3.add(deck.get());
		tableau4.add(deck.get());
		tableau5.add(deck.get());
		tableau6.add(deck.get());
		tableau7.add(deck.get());
		tableau8.add(deck.get());
		//deal one card to the first foundation pile
		foundation1.add(deck.get());
		this.setRankOfFoundation();
		//deal one card to the waste pile
		wastePile.add(deck.get());
		
		updateScore(0);
		
	}

	private void initializeView() {
		CardImages ci = getCardImages();
		container.setDoubleBuffered(true);
		//Shows the deck
		deckView = new DeckView(deck);
		deckView.setBounds(40+ci.getWidth(), 20, ci.getWidth(), ci.getHeight());
		container.addWidget(deckView);
		//Shows the waste pile
		wastePileView = new PileView(wastePile);
		wastePileView.setBounds(60+(2 *ci.getWidth()), 20, ci.getWidth(), ci.getHeight());
		container.addWidget(wastePileView);
		//Shows the reserve column
		reserveColumnView = new ColumnView(reserveColumn);
		reserveColumnView.setBounds(20, 20, ci.getWidth(), ci.getHeight()*19);
		container.addWidget(reserveColumnView);
		//Shows the ScoreView
		scoreView = new IntegerView(score);
		scoreView.setBounds(180+(8 * ci.getWidth()), 20, ci.getWidth(), ci.getHeight());
		container.addWidget(scoreView);
		//Shows the foundation piles
		foundationView1 = new PileView(foundation1);
		foundationView2 = new PileView(foundation2);
		foundationView3 = new PileView(foundation3);
		foundationView4 = new PileView(foundation4);
		foundationView5 = new PileView(foundation5);
		foundationView6 = new PileView(foundation6);
		foundationView7 = new PileView(foundation7);
		foundationView8 = new PileView(foundation8);
		foundationView1.setBounds(40+ci.getWidth(), 40 + ci.getHeight(), ci.getWidth(), ci.getHeight());
		foundationView2.setBounds(60+(2 * ci.getWidth()), 40 + ci.getHeight(), ci.getWidth(), ci.getHeight());
		foundationView3.setBounds(80+(3 * ci.getWidth()), 40 + ci.getHeight(), ci.getWidth(), ci.getHeight());
		foundationView4.setBounds(100+(4 * ci.getWidth()), 40 + ci.getHeight(), ci.getWidth(), ci.getHeight());
		foundationView5.setBounds(120+(5 * ci.getWidth()), 40 + ci.getHeight(), ci.getWidth(), ci.getHeight());
		foundationView6.setBounds(140+(6 * ci.getWidth()), 40 + ci.getHeight(), ci.getWidth(), ci.getHeight());
		foundationView7.setBounds(160+(7 * ci.getWidth()), 40 + ci.getHeight(), ci.getWidth(), ci.getHeight());
		foundationView8.setBounds(180+(8 * ci.getWidth()), 40 + ci.getHeight(), ci.getWidth(), ci.getHeight());
		container.addWidget(foundationView1);
		container.addWidget(foundationView2);
		container.addWidget(foundationView3);
		container.addWidget(foundationView4);
		container.addWidget(foundationView5);
		container.addWidget(foundationView6);
		container.addWidget(foundationView7);
		container.addWidget(foundationView8);
		//Shows the tableau piles 
		tableauView1 = new BuildablePileView(tableau1);
		tableauView2 = new BuildablePileView(tableau2);
		tableauView3 = new BuildablePileView(tableau3);
		tableauView4 = new BuildablePileView(tableau4);
		tableauView5 = new BuildablePileView(tableau5);
		tableauView6 = new BuildablePileView(tableau6);
		tableauView7 = new BuildablePileView(tableau7);
		tableauView8 = new BuildablePileView(tableau8);
		tableauView1.setBounds(40 + ci.getWidth(), 50 + (2 * ci.getHeight()), ci.getWidth(), ci.getHeight()*13);
		tableauView2.setBounds(60+(2 * ci.getWidth()), 50 + (2 * ci.getHeight()), ci.getWidth(), ci.getHeight()*13);
		tableauView3.setBounds(80+(3 * ci.getWidth()), 50 + (2 * ci.getHeight()), ci.getWidth(), ci.getHeight()*13);
		tableauView4.setBounds(100+(4 * ci.getWidth()), 50 + (2 * ci.getHeight()), ci.getWidth(), ci.getHeight()*13);
		tableauView5.setBounds(120+(5 * ci.getWidth()), 50 + (2 * ci.getHeight()), ci.getWidth(), ci.getHeight()*13);
		tableauView6.setBounds(140+(6 * ci.getWidth()), 50 + (2 * ci.getHeight()), ci.getWidth(), ci.getHeight()*13);
		tableauView7.setBounds(160+(7 * ci.getWidth()), 50 + (2 * ci.getHeight()), ci.getWidth(), ci.getHeight()*13);
		tableauView8.setBounds(180+(8 * ci.getWidth()), 50 + (2 * ci.getHeight()), ci.getWidth(), ci.getHeight()*13);
		container.addWidget(tableauView1);
		container.addWidget(tableauView2);
		container.addWidget(tableauView3);
		container.addWidget(tableauView4);
		container.addWidget(tableauView5);
		container.addWidget(tableauView6);
		container.addWidget(tableauView7);
		container.addWidget(tableauView8);
		
		
		
	}

	private void initializeControllers() {
		//deck controllers
		deckView.setMouseAdapter(new AmericanToadDeckController(this, deck, wastePile));
		deckView.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		deckView.setUndoAdapter(new SolitaireUndoAdapter(this));
		//wastepile controllers
		wastePileView.setMouseAdapter(new AmericanToadWastePileController (this,wastePileView));//at point 15:10 of rb video 3
		wastePileView.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		wastePileView.setUndoAdapter(new SolitaireUndoAdapter(this));
//		//reserve column controllers
		reserveColumnView.setMouseAdapter(new AmericanToadReserveController (this, reserveColumnView));
		reserveColumnView.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		reserveColumnView.setUndoAdapter(new SolitaireUndoAdapter(this));
//		//foundation pile controllers
		foundationView1.setMouseAdapter(new AmericanToadFoundationController(this, foundationView1));
		foundationView2.setMouseAdapter(new AmericanToadFoundationController(this, foundationView2));
		foundationView3.setMouseAdapter(new AmericanToadFoundationController(this, foundationView3));
		foundationView4.setMouseAdapter(new AmericanToadFoundationController(this, foundationView4));
		foundationView5.setMouseAdapter(new AmericanToadFoundationController(this, foundationView5));
		foundationView6.setMouseAdapter(new AmericanToadFoundationController(this, foundationView6));
		foundationView7.setMouseAdapter(new AmericanToadFoundationController(this, foundationView7));
		foundationView8.setMouseAdapter(new AmericanToadFoundationController(this, foundationView8));
		foundationView1.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		foundationView2.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		foundationView3.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		foundationView4.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		foundationView5.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		foundationView6.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		foundationView7.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		foundationView8.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		foundationView1.setUndoAdapter(new SolitaireUndoAdapter(this));
		foundationView2.setUndoAdapter(new SolitaireUndoAdapter(this));
		foundationView3.setUndoAdapter(new SolitaireUndoAdapter(this));
		foundationView4.setUndoAdapter(new SolitaireUndoAdapter(this));
		foundationView5.setUndoAdapter(new SolitaireUndoAdapter(this));
		foundationView6.setUndoAdapter(new SolitaireUndoAdapter(this));
		foundationView7.setUndoAdapter(new SolitaireUndoAdapter(this));
		foundationView8.setUndoAdapter(new SolitaireUndoAdapter(this));
//		//tableau column controllers
		tableauView1.setMouseAdapter(new AmericanToadTableauController(this, tableauView1));
		tableauView2.setMouseAdapter(new AmericanToadTableauController(this, tableauView2));
		tableauView3.setMouseAdapter(new AmericanToadTableauController(this, tableauView3));
		tableauView4.setMouseAdapter(new AmericanToadTableauController(this, tableauView4));
		tableauView5.setMouseAdapter(new AmericanToadTableauController(this, tableauView5));
		tableauView6.setMouseAdapter(new AmericanToadTableauController(this, tableauView6));
		tableauView7.setMouseAdapter(new AmericanToadTableauController(this, tableauView7));
		tableauView8.setMouseAdapter(new AmericanToadTableauController(this, tableauView8));
		tableauView1.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		tableauView2.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		tableauView3.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		tableauView4.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		tableauView5.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		tableauView6.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		tableauView7.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		tableauView8.setMouseMotionAdapter(new SolitaireMouseMotionAdapter(this));
		tableauView1.setUndoAdapter(new SolitaireUndoAdapter(this));
		tableauView2.setUndoAdapter(new SolitaireUndoAdapter(this));
		tableauView3.setUndoAdapter(new SolitaireUndoAdapter(this));
		tableauView4.setUndoAdapter(new SolitaireUndoAdapter(this));
		tableauView5.setUndoAdapter(new SolitaireUndoAdapter(this));
		tableauView6.setUndoAdapter(new SolitaireUndoAdapter(this));
		tableauView7.setUndoAdapter(new SolitaireUndoAdapter(this));
		tableauView8.setUndoAdapter(new SolitaireUndoAdapter(this));
	}
	public Dimension getPreferredSize() {//overrides parent method
		// default starting dimensions...
		return new Dimension(880, 766);
	}

	private void initializeModel(int seed) {
		
		this.getPreferredSize();
		deck = new MultiDeck("deck", 2);
		deck.create(seed);
		model.addElement(deck);
		
		//add foundation piles
		foundation1 = new Pile("foundation1");
		model.addElement(foundation1);
		foundation2 = new Pile("foundation2");
		model.addElement(foundation2);
		foundation3 = new Pile("foundation3");
		model.addElement(foundation3);
		foundation4 = new Pile("foundation4");
		model.addElement(foundation4);
		foundation5 = new Pile("foundation5");
		model.addElement(foundation5);
		foundation6 = new Pile("foundation6");
		model.addElement(foundation6);
		foundation7 = new Pile("foundation7");
		model.addElement(foundation7);
		foundation8 = new Pile("foundation8");
		model.addElement(foundation8);
		
		//add waste pile
		wastePile = new Pile("waste");
		model.addElement(wastePile);
		
		//add tableau columns
		tableau1 = new BuildablePile("tableau1");
		model.addElement(tableau1);
		tableau2 = new BuildablePile("tableau2");
		model.addElement(tableau2);
		tableau3 = new BuildablePile("tableau3");
		model.addElement(tableau3);
		tableau4 = new BuildablePile("tableau4");
		model.addElement(tableau4);
		tableau5 = new BuildablePile("tableau5");
		model.addElement(tableau5);
		tableau6 = new BuildablePile("tableau6");
		model.addElement(tableau6);
		tableau7 = new BuildablePile("tableau7");
		model.addElement(tableau7);
		tableau8 = new BuildablePile("tableau8");
		model.addElement(tableau8);
		//add reserve column
		reserveColumn = new Column("reserve");
		model.addElement(reserveColumn);
		
		updateNumberCardsLeft(104);
		updateScore(0);
	}
	
	/**Sets the initial rank of the foundation*/
	public void setRankOfFoundation(){
		this.rankOfFoundation = foundation1.peek().getRank();
	}
	
	/**Gets the initial rank of the foundation*/
	public int getRankOfFoundation(){
		return this.rankOfFoundation;
	}
	
	/** Code to launch solitaire variation */
	public static void main(String[] args){
		//Seed is to ensure we get the same initial cards every time.
		//Here the seed is to "order by rank"
		Main.generateWindow(new AmericanToad(), MultiDeck.OrderByRank);
		
	}
}
