# Generated by Django 5.0.4 on 2024-05-09 21:52

from django.db import migrations
from ..models.trading import CoinType, TypeType, MinerType, ResourceType

def populate_data(apps, schema_editor):
    Team = apps.get_model('main', 'Team')
    Team.objects.create(name="Team 1")
    Team.objects.create(name="Team 2")

    Item = apps.get_model('main', 'Item')
    for resource in ResourceType:
        for coin in CoinType:
            item = Item.objects.create(name=resource, currency=coin, type=TypeType.RESOURCE)

    for miner in MinerType:
        for coin in CoinType:
            item = Item.objects.create(name=miner, currency=coin, type=TypeType.MINER)
            
    for coin_name in CoinType:
        item = Item.objects.create(name=coin_name, currency=coin_name, type=TypeType.COIN)



    Mine = apps.get_model('main', 'Mine')
    TeamMine = apps.get_model('main', 'TeamMine')
    TeamMineItem = apps.get_model('main', 'TeamMineItem')
    for coin in CoinType:
        mine = Mine.objects.create(name=coin, currency=coin)
        for team in Team.objects.all():
            team_mine = TeamMine.objects.create(team=team, mine=mine, money=100)

    for team_mine in TeamMine.objects.all():
        for miner in MinerType:
            item = Item.objects.get(name=miner, currency=team_mine.mine.currency)
            if item:
                TeamMineItem.objects.create(team_mine=team_mine, item=item, amount=0)


    Post = apps.get_model('main', 'Post')
    for resource in ResourceType:
        for coin in CoinType:
            Post.objects.create(name=f"{resource.label} winkel", type="RESOURCE", sells=Item.objects.get(name=resource, currency=coin), sell_amount=1)

    for miner in MinerType:
        for coin in CoinType:
            Post.objects.create(name=f"{miner.label} winkel", type="MINER", sells=Item.objects.get(name=miner, currency=coin), sell_amount=1)


    PostRecipe = apps.get_model('main', 'PostRecipe')
    for post in Post.objects.all():
        if post.sells.type == TypeType.RESOURCE:
            for ct in CoinType:
                if ct != post.sells.currency:
                    PostRecipe.objects.create(post=post, price=15, item=Item.objects.get(name=ct, type=TypeType.COIN, currency=ct))

        if post.sells.type == TypeType.MINER:
            if post.sells.name == MinerType.A:
                PostRecipe.objects.create(post=post, price=1, item=Item.objects.get(currency=post.sells.currency, name=ResourceType.A))
            if post.sells.name == MinerType.B:
                PostRecipe.objects.create(post=post, price=1, item=Item.objects.get(currency=post.sells.currency, name=ResourceType.A))
                PostRecipe.objects.create(post=post, price=1, item=Item.objects.get(currency=post.sells.currency, name=ResourceType.B))
            if post.sells.name == MinerType.C:
                PostRecipe.objects.create(post=post, price=1, item=Item.objects.get(currency=post.sells.currency, name=ResourceType.A))
                PostRecipe.objects.create(post=post, price=1, item=Item.objects.get(currency=post.sells.currency, name=ResourceType.B))
                PostRecipe.objects.create(post=post, price=1, item=Item.objects.get(currency=post.sells.currency, name=ResourceType.C))

    Player = apps.get_model('main', 'Player')
    player = Player.objects.create(name="Peter", section="COM", team=Team.objects.get(name="Team 1"))

    PlayerItem = apps.get_model('main', 'PlayerItem')
    for item in Item.objects.all():
        PlayerItem.objects.create(player=player, item=item, amount=20)


    GameSettings = apps.get_model('main', 'GameSettings')
    GameSettings.objects.create(mode="trading")







class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_data),
    ]
