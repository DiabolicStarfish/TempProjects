import javax.swing.JOptionPane;

public class Exception2
{
	public static void main(String args[])
	{
		int dividend,divisor, quotient;
		String inpStr;

		try
		{
			inpStr = JOptionPane.showInputDialog("Enter the dividend: ");
			dividend = Integer.parseInt(inpStr);

			inpStr = JOptionPane.showInputDialog("Enter the divisor: ");
			divisor = Integer.parseInt(inpStr);
			quotient = dividend/divisor;

			JOptionPane.showMessageDialog(null, "Dividend= "+dividend +"\nDivisor= "+ divisor+ "\nQuotient= "+quotient, "Quotient", JOptionPane.INFORMATION_MESSAGE);
			System.out.println("Quotient = " + quotient);
		}
		catch (ArithmeticException aeRef)
		{
			JOptionPane.showMessageDialog(null, "Exception "+ aeRef.toString(), "ArithmeticException", JOptionPane.ERROR_MESSAGE);
		}
		catch (NumberFormatException nfeRef)
		{
			JOptionPane.showMessageDialog(null, "Exception "+ nfeRef.toString(), "NumberFormatException", JOptionPane.ERROR_MESSAGE);
		}
		System.exit(0);
	}
}