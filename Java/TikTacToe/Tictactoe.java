import java.awt.event.*;
import javax.swing.*;
import java.util.*;
import java.awt.*;

class Game extends JFrame implements ActionListener{

	static Random rand = new Random();
	static JButton[] buttons = new JButton[9];
	static int count = 0;
	static int[][] winningChances = {{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}};
	static int[] userChances = {-1,-1,-1};
	static int[] botChances = {-1,-1,-1};
	static boolean result=false,flag = true;

	Game(){
		JFrame frame = new JFrame("TIC TAC TOE");
		for (int i=0;i<9;i++) {
			buttons[i] = new JButton();
			buttons[i].addActionListener(this);
			frame.add(buttons[i]);
		}

		frame.setLayout(new GridLayout(3,3));
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(400,300);
		frame.setVisible(true);
	}

	public int botChoice(int[] userChances){
		boolean botVal = true;
		int val=-1;
		while(botVal){
			val = Math.abs(rand.nextInt()%9);
			if (!checkDuplicate(val,userChances) && !checkDuplicate(val,botChances) )
				botVal=false;
		}
		return val;

	}

	public boolean result(int[] aRR){
		Arrays.sort(aRR);
		for(int[] test:winningChances){
			if (Arrays.equals(test,aRR)){
				return true;
			}
		}
		return false;
	}

	public boolean checkDuplicate(int num,int[] arr){
		for (int i=0;i<arr.length;i++)
			if (arr[i]==num)
				return true;
		return false;
	}

	public void restart(){
		try{
			Thread.sleep(5);

		}
		catch(Exception InterruptedException){}
		
		for (int i=0;i<9;i++)
			buttons[i].setLabel("");
		for (int j=0;j<3;j++) {
			userChances[j]=-1;
			botChances[j]=-1;
		}
		count = 0;
		result=false;flag = true;
	}
	public void actionPerformed(ActionEvent e){

		for (int i=0;i<9 && flag;i++) {
			if(e.getSource()==buttons[i]){
				if (!checkDuplicate(i,userChances)){
					buttons[i].setLabel("X");
					userChances[count]=i;
					int randBot= botChoice(userChances);
					buttons[randBot].setLabel("O");
					botChances[count]=randBot;
					count++;
					if (count==3){
						if (result(userChances))
							JOptionPane.showMessageDialog(this,"You Won!");
						if (result(botChances))
							JOptionPane.showMessageDialog(this,"Bot Won!");
						if (!result(userChances) && !result(botChances))
							JOptionPane.showMessageDialog(this,"Tied");
						flag = false;
						restart();
						JOptionPane.showMessageDialog(this,"Game Restarted");
					}
				}
			}	
		}

	}
}

public class Tictactoe {
	public static void main(String[] args) {
		new Game();
	}
}
