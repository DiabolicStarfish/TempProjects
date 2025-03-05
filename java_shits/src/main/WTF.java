package java_shits.src.main;

import java.util.Arrays;
import java.util.Scanner;

public class WTF
{
    private String numbers;
    private int[] integers;


    public void sort_numbers()
    {
        Arrays.sort(integers);
    }

    public void get_integer_list()
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a comma-separated list of integers: ");
        numbers = input.nextLine();
        input.close();
        numbers.trim();

        String[] stringNumbers = numbers.split(",");

        integers = new int[stringNumbers.length];

        for(int i=0; i<stringNumbers.length; i++)
        {
            try{
                integers[i] = Integer.parseInt(stringNumbers[i]);
            }
            catch(NumberFormatException e)
            {
                System.err.println("This is an invalid input: " + stringNumbers[i]);
            }
        }
    }

    public int sum_of_first_and_second()
    {
        return (integers[0] + integers[1]);
    }

    public int product_of_third_and_fourth()
    {
        return (integers[2] + integers[3]);
    }

    public String quotient_of_fifth()
    {
        double quotient = (sum_of_first_and_second() + product_of_third_and_fourth()) / integers[4];
        String output = String.format("%.2f", quotient);
        return output;
    }

    public void process_and_display()
    {
        get_integer_list();
        sort_numbers();

        System.out.println("Sorted integer list: " + integers);
        System.out.println("Sum of first and second: " + sum_of_first_and_second());
        System.out.println("Product of third and fourth: " + product_of_third_and_fourth());
        System.out.println("Quotient of fifth: " + quotient_of_fifth() + quotient_of_fifth());
    }
}