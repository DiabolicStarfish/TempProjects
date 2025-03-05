public class FindArray
{
	public static void main(String args[])
	{		
		int [] array = {0,1,2,3,4};
		int array2[] = null;
		
			try
			{
				for(int i=0; i<2; i++)
				{
				System.out.print(array2[i]);	
				}						
			}
			catch(NullPointerException ae)
			{
				System.out.print("Exception: NullPointerException\n");
			}

			try
			{
				for(int i=0; i<6; i++)
				{
					System.out.print(array[i]+" ");
				}
			}
			catch(ArrayIndexOutOfBoundsException e)
			{
				System.out.print("Exception: ArrayIndexOutOfBoundsException\n");
			}

			try
			{
				for(int i=0; i<7; i++)
				{
					System.out.print(array[i]+" ");
				}
			}
			catch(RuntimeException a)
			{
				System.out.print("Exception: RuntimeException");
			}
	}
}