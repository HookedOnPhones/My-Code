import java.util.Random;

public class Enemy
{
    private String name;
    private int hp;
    private int minDamage;
    private int maxDamage;
    private int rewardGold;
    private String catchPhrase;
    private boolean spoke;
    
    public Enemy(String name, int hp, int minDamage, int maxDamage, int rewardGold, String catchPhrase)
    {
        this.name = name;
        this.hp = hp;
        this.minDamage = minDamage;
        this.maxDamage = maxDamage;
        this.rewardGold = rewardGold;
        this.catchPhrase = catchPhrase;
        this.spoke = false;
    }
    
    public String getName()
    {
        return name;
    }
    
    public int getHp()
    {
        return hp;
    }
    
    public void setHp(int value)
    {
        hp = value;
        if (hp < 0)
        {
            hp = 0;
        }
    }
    
    public int getRewardGold()
    {
        return rewardGold;
    }
    
    public void sayCatchPhrase()
    {
        System.out.println(name + ": \"" + catchPhrase + "\"");
        spoke = true;
    }
    
    public boolean hasSpoken()
    {
        return spoke;
    }
    
    public void takeDamage(int amount)
    {
        setHp(hp - amount);
    }
    
    public int getAttackDamage()
    {
        Random r = new Random();
        int range = maxDamage - minDamage + 1;
        int dmg = r.nextInt(range) + minDamage;
        return dmg;
    }
}



























