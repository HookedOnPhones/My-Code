import java.io.*;
import java.util.*;

public class SaveManager
{
    private String fileName;
    
    public SaveManager(String fileName)
    {
        this.fileName = fileName;
    }
    
    public void save(SaveData data)
    {
        try 
        {
            PrintWriter out = new PrintWriter(new FileWriter(fileName));
            out.println(data.playerName);
            out.println(data.playerHp);
            out.println(data.playerGold);
            out.println(data.weaponName);
            out.println(data.weaponDamage);
            out.println(data.currentEnemyIndex);
            out.println(data.goblinHp);
            out.println(data.wizardHp);
            out.println(data.mirrorHp);
            out.close();
        } 
        catch(IOException e) 
        {
            System.out.println("Error saving game.");
        }
    }
    
    public SaveData load()
    {
        File f = new File(fileName);
        if (!f.exists() || !f.isFile())
        {
            return null;
        }
        
        try
        {
            Scanner sc = new Scanner(f);
            SaveData d = new SaveData();
            
            if (sc.hasNextLine())
            {
                d.playerName = sc.nextLine();
            }
            else
            {
                sc.close();
                return null;
            }
            
            if (sc.hasNextInt())
            {
                d.playerHp = sc.nextInt();
            }
            else
            {
                sc.close();
                return null;
            }
            
            if (sc.hasNextInt())
            {
                d.playerGold = sc.nextInt();
            }
            else
            {
                sc.close();
                return null;
            }
            
            sc.nextLine();
            
            if (sc.hasNextLine())
            {
                d.weaponName = sc.nextLine();
            }
            else
            {
                sc.close();
                return null;
            }
            
            if (sc.hasNextInt())
            {
                d.weaponDamage = sc.nextInt();
            }
            else
            {
                sc.close();
                return null;
            }
            
            if (sc.hasNextInt())
            {
                d.currentEnemyIndex = sc.nextInt();
            }
            else
            {
                sc.close();
                return null;
            }
            
            if (sc.hasNextInt())
            {
                d.goblinHp = sc.nextInt();
            }
            else
            {
                sc.close();
                return null;
            }
            
            if (sc.hasNextInt())
            {
                d.wizardHp = sc.nextInt();
            }
            else
            {
                sc.close();
                return null;
            }
            
            if (sc.hasNextInt())
            {
                d.mirrorHp = sc.nextInt();
            }
            else
            {
                sc.close();
                return null;
            }
            
            sc.close();
            return d;
        }
        catch (Exception e)
        {
            System.out.println("Could not read save file.");
            return null;
        }
    }
    
    public void deleteSave()
    {
        File f = new File(fileName);
        if (f.exists())
        {
            f.delete();
        }
    }
}






















































