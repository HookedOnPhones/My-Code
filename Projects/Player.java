public class Player
{
    private String name;
    private int hp;
    private int maxHp;
    private int gold;
    private Weapon weapon;
    private int startingDamage;
    
    public Player(String name)
    {
        this.name = name;
        this.maxHp = 100;
        this.hp = 100;
        this.gold = 50;
        this.weapon = new Weapon("Starter Sword", 15);
        this.startingDamage = 15;
    }
    
    public String getName()
    {
        return name;
    }
    
    public int getHp()
    {
        return hp;
    }
    
    public int getGold()
    {
        return gold;
    }
    
    public Weapon getWeapon()
    {
        return weapon;
    }
    
    public void setWeapon(Weapon w)
    {
        this.weapon = w;
    }
    
    public void setHp(int value)
    {
        hp = value;
        if (hp < 0)
        {
            hp = 0;
        }
        if (hp > maxHp)
        {
            hp = maxHp;
        }
    }
    
    public void setGold(int value)
    {
        if (value < 0)
        {
            gold = 0;
        }
        else
        {
            gold = value;
        }
    }
    
    public void addGold(int amount)
    {
        gold = gold + amount;
    }
    
    public void heal(int amount)
    {
        setHp(hp + amount);
    }
    
    public void takeDamage(int amount)
    {
        setHp(hp - amount);
    }
    
    public int getMaxHp()
    {
        return maxHp;
    }
    
    public int getStartingDamage()
    {
        return startingDamage;
    }
}































