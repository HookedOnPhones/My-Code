public class Mirror extends Enemy
{
    private int fixedDamage;
    
    public Mirror(int playerStarterDamage)
    {
        super("Mirror", 100, 5, 15, 100, "Ha! There's a Spiderman meme which would be appropriate here!");
        fixedDamage = playerStarterDamage;
    }
    
    @Override
    public int getAttackDamage()
    {
        return fixedDamage;
    }
}