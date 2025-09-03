import java.util.Scanner;

public class Shop
{
	public void open(Player player, Scanner input)
	{
		boolean inShop = true;

		while (inShop)
		{
			System.out.println("\n=== Shop ===");
			System.out.println("Gold: " + player.getGold());
			System.out.println("1) Buy Longsword (50 gold, 20 dmg)");
			System.out.println("2) Rest (+40 HP, max 100)");
			System.out.println("3) Leave Shop");
			System.out.println("Choose an option: ");

			String choice = input.nextLine();

			if (choice.equals("1"))
			{
				if (player.getGold() >= 50)
				{
					player.addGold(-50);
					player.setWeapon(new Weapon("Longsword", 20));
					System.out.println("You've upgraded to the Longsword. Use it well.");
				}
				else
				{
				    System.out.println("Not enough gold.");
				}
			}
			else if (choice.equals("2"))
			{
			    int before = player.getHp();
			    player.heal(40);
			    int after = player.getHp();
			    System.out.println("You rested. HP: " + before + " -> " + after);
			}
			else if (choice.equals("3"))
			{
			    inShop = false;
			}
			else
			{
			    System.out.println("Invalid option.");
			}
		}
	}
}