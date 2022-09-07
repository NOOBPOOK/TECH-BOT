import nextcord
from nextcord.ui import Button, View 
from nextcord.utils import get
from nextcord.ext import commands
import os
from dotenv import load_dotenv
import wikipedia
import smtplib
import datetime
import webbrowser
import youtube_dl
import humanfriendly
import time
import random
import asyncio
import asyncpraw

reddit = asyncpraw.Reddit(client_id= "rlxZ8ONX4K12gG28bslAQw",
                     client_secret = "SeclhK30B2TG7ndn7V4gRB6yQs5bmg",
                     username = "Advanced_Daikon756",
                     password = "#noobpookveduki1234",
                     user_agent = "scrbot")

intents=nextcord.Intents(messages = True, message_content=True, guilds = True)
client = commands.Bot(command_prefix="^", help_command=None, intents=intents)

gameOver = True
cricket_p1 = ""
cricket_p2 = ""
player1 = ""
player2 = ""
turn = ""
tic_time = 0
gameOver = True
GameOver = True
board = []

winningConditions = [
    [ 0, 1, 2],
    [ 3, 4, 5],
    [ 6, 7, 8],
    [ 0, 3, 6],
    [ 1, 4, 7],
    [ 2, 5, 8],
    [ 0, 4, 8],
    [ 2, 4, 6]
]

@client.event
async def on_ready():
    print("Bot just landed on the server!")
    
@client.event
async def on_member_join(member):
    author = member
    myEmbed = nextcord.Embed(title="TECH CENTER", description=f"This a server where you chill and have fun talking about Tech and all!", color=0xffff00)
    myEmbed.add_field(name="***WELCOME TO THE SERVER!***",value = f"Here we have a new member to our server!\n Welcome to the server {member.mention}!")
    myEmbed.set_thumbnail(url=f"{member.display_avatar}")
    myEmbed.set_footer(text="Explore outside while sitting inside!\n#DISCORD")
    myEmbed.set_author(name="Tech Bot#6446")
    chn = client.get_channel(867924730034917476)
    await chn.send(embed=myEmbed)
    
@client.event
async def on_member_remove(member):
    mem_rol = member.roles
    myEmbed = nextcord.Embed(title="TECH CENTER", description=f"Our friend has just left the server!", color=0xffff00)
    myEmbed.add_field(name = f"**{member}**", value = "👋")
    myEmbed.set_thumbnail(url = f"{member.display_avatar}")
    myEmbed.set_author(name="Tech Bot#6446")
    chn = client.get_channel(979263187029479444)
    await chn.send(embed=myEmbed)

@client.command()
async def private(ctx):
    myEmbed = nextcord.Embed(title = "Tech Center", description=f"Hello there In Private! **{ctx.author}**\nHow may I help you?", color=0xffff00)
    myEmbed.set_thumbnail(url=ctx.author.display_avatar)
    myEmbed.set_author(name="Tech Bot#6446")
    await ctx.author.send(embed=myEmbed)
    
@client.command()
async def wiki(ctx, *, arg):
    mes_1 = await ctx.reply("Searching Google!")
    try:
        results = wikipedia.page(arg)
        url = results.url
        content = results.content
        await mes_1.edit(content=f"According to Tech Bot, {url}")
    except Exception as e:
        await mes_1.edit(content="Could not get what you were looking for!")
        
@client.command()
async def luckyroles(ctx, give_role: nextcord.Role):
    user_give = ctx.author
    user_rol = get(user_give.guild.roles, id=859450535211565076)#Emperor Role
    if user_rol in user_give.roles or user_give == await client.fetch_user(763676643356835840):
        guild_mem = user_give.guild
        mem_list = []
        
        for member in guild_mem.members:
            mem_list.append(member)
            
        try:
            giveaway_mem = random.choice(mem_list)
            await giveaway_mem.add_roles(give_role)
            give_embed = nextcord.Embed(title="Tech Center", description = f"**{giveaway_mem}** \n You have just won the giveaway held by **{ctx.author}**\n You have got the **{give_role} Role** !🎆🎊🎉*", color=0xffff00)
            give_embed.set_image(url = giveaway_mem.display_avatar)
            await ctx.reply(embed=give_embed)
            try:
                await giveaway_mem.send(embed=give_embed)
            except:
                return
        except:
            await ctx.reply("The Bot is unable to give the role due to Less Permissions!")
    else:
        await ctx.reply(f"You don't have the necessary role to perform a giveaway!\n You should have **{user_rol}** to perform giveaway in the server!")
        
@client.command()
async def admin(ctx, pas:int , chn_id:int, *, arg):
    if pas == 6446:
        try:
            chn = client.get_channel(chn_id)
            admin_ctx = await ctx.author.send("Sending your message!")
            await chn.send(arg)
            await admin_ctx.edit(content=f"Your message has been sent successfully to this channel {chn.mention}")
        except Exception as e:
            await admin_ctx.edit(content=f"Your message could not be delivered to the channel!\n Here is why {e}")
    else:
        await ctx.send(f"The above password is Wrong!{ctx.author.mention}!\nTry again!")
        
@client.command()
async def selfrole(ctx):
    button = Button(label="L Bonzo", style=nextcord.ButtonStyle.green, emoji="👋")
    button2 = Button(label="Bump Reminder", style=nextcord.ButtonStyle.red, emoji="🔔")
    button3 = Button(label="Tech Noobie", style=nextcord.ButtonStyle.blurple, emoji="💾")
    button4 = Button(label="Server Helper", style=nextcord.ButtonStyle.blurple, emoji="👨‍💻")
    view = View(timeout=10)
    view.add_item(button)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    main = ctx.author
    author = ctx.author
    role = get(main.guild.roles, id=952282281031110787)#L Bonzo
    role2 = get(main.guild.roles, id=979726085598105600)#Bump Reminder
    role3 = get(main.guild.roles, id=979726295229427732)#Tech Noobie
    role4 = get(main.guild.roles, id=979726956385931345)#Server Helper
    async def button_callback(interaction):
        author = interaction.user
        await interaction.user.add_roles(role)
        if role2 in author.roles:
            await interaction.user.remove_roles(role2)
        elif role3 in author.roles:
            await interaction.user.remove_roles(role3)
        elif role4 in author.roles:
            await interaction.user.remove_roles(role4)
        Rembed = nextcord.Embed(title = "Tech Center", description=f"{interaction.user.mention} have got for the **{role}** in the server!", color=0xffff00)
        await interaction.response.send_message(embed=Rembed)
    button.callback = button_callback 
    async def button_callback(interaction):
        await interaction.user.add_roles(role2)
        if role in author.roles:
            await interaction.user.remove_roles(role)
        elif role3 in author.roles:
            await interaction.user.remove_roles(role3)
        elif role4 in author.roles:
            await interaction.user.remove_roles(role4)
        Rembed = nextcord.Embed(title = "Tech Center", description=f"{interaction.user.mention} have got for the **{role2}** in the server!", color=0xffff00)
        await interaction.response.send_message(embed=Rembed)
    button2.callback = button_callback 
    async def button_callback(interaction):
        author = interaction.user
        await interaction.user.add_roles(role3)
        if role2 in author.roles:
            await interaction.user.remove_roles(role2)
        elif role in author.roles:
            await interaction.user.remove_roles(role)
        elif role4 in author.roles:
            await interaction.user.remove_roles(role4)
        Rembed = nextcord.Embed(title = "Tech Center", description=f"{interaction.user.mention} have got for the **{role3}** in the server!", color=0xffff00)
        await interaction.response.send_message(embed=Rembed)
    button3.callback = button_callback 
    async def button_callback(interaction):
        author = interaction.user
        await interaction.user.add_roles(role4)
        if role2 in author.roles:
            await interaction.user.remove_roles(role2)
        elif role3 in author.roles:
            await interaction.user.remove_roles(role3)
        elif role in author.roles:
            await interaction.user.remove_roles(role)
        Rembed = nextcord.Embed(title = "Tech Center", description=f"{interaction.user.mention} have got for the **{role4}** in the server!", color=0xffff00)
        await interaction.response.send_message(embed=Rembed)
    button4.callback = button_callback
    await ctx.reply("Here are the various roles! \n Choose What you want to be!", view=view)
    
@client.command()
async def pfp(ctx, user: nextcord.Member):
    pembed = nextcord.Embed(title = "TECH CENTER", description=f"**{user}** profile picture!", color = 0x992d22)
    pembed.set_image(url = user.display_avatar)
    await ctx.reply(embed=pembed)
    
@client.command()
async def addrol(ctx , p1:nextcord.Member , role:nextcord.Role):
    mod_mem = ctx.author
    mod_rol = get(mod_mem.guild.roles, id=859450535211565076)#Emperor Role
    if mod_rol in mod_mem.roles or mod_mem == await client.fetch_user(763676643356835840):
        try:
            await p1.add_roles(role)
            rembed = nextcord.Embed(title=f"**Role Updated for the User {p1}!**", description=f"Added the role **{role}**!", color=0x992d22)
            rembed.set_thumbnail(url = f"{p1.display_avatar}")
            rembed.set_author(name = "Tech Bot#6446")
            await ctx.reply(embed = rembed)
        except Exception as e:
            await ctx.reply(f"The bot cannot give this role to **{p1}** due to less permissions!")
            print(str(e))
    else:
        await ctx.reply(f"You cannot Give/Remove Roles as you don't have the **{mod_rol}** role!")
    
@client.command()
async def remrol(ctx , p1:nextcord.Member , role:nextcord.Role):
    mod_mem = ctx.author
    mod_rol = get(mod_mem.guild.roles, id=859450535211565076)#Emperor Role
    if mod_rol in mod_mem.roles or mod_mem == await client.fetch_user(763676643356835840):
        try:
            await p1.remove_roles(role)
            rembed = nextcord.Embed(title=f"**Role Updated for the User {p1}!**", description=f"Removed the role **{role}**!", color=0x992d22)
            rembed.set_thumbnail(url = f"{p1.display_avatar}")
            rembed.set_author(name = "Tech Bot#6446")
            await ctx.reply(embed = rembed)
        except Exception as e:
            print(str(e))
            await ctx.reply(f"The bot cannot remove this role from **{p1}** due to less permissions!")
    else:
        await ctx.reply(f"You cannot Give/Remove Roles as you don't have the **{mod_rol}** role!")
    
@client.command()
async def meme(ctx):
    all_subs = []
    subreddit = await reddit.subreddit("memes")
    top_red = subreddit.top("day", limit=50)
    async for top_hot in top_red:
        all_subs.append(top_hot)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    memEmbed = nextcord.Embed(title= name)
    memEmbed.set_thumbnail(url = "https://static-prod.adweek.com/wp-content/uploads/2021/06/Reddit-Avatar-Builder-Hero-1280x680.png")
    memEmbed.set_image(url = url)
    ctx_mem = await ctx.reply(embed = memEmbed)
    await meme_but(ctx,ctx_mem)
        
async def meme_but(ctx,ctx_mem):
    button = Button(label="Another One!", style=nextcord.ButtonStyle.blurple, emoji="🤚")
    view = View(timeout=100)
    view.add_item(button)
    async def button_callback(interaction):
        await mem_rep(ctx,ctx_mem)
    button.callback = button_callback
    await ctx.reply(view = view)
        
async def mem_rep(ctx,ctx_mem):
    all_subs = []
    subreddit = await reddit.subreddit("memes")
    top_red = subreddit.top("day", limit=50)
    async for top_hot in top_red:
        all_subs.append(top_hot)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    memEmbed = nextcord.Embed(title= name)
    memEmbed.set_thumbnail(url = "https://static-prod.adweek.com/wp-content/uploads/2021/06/Reddit-Avatar-Builder-Hero-1280x680.png")
    memEmbed.set_image(url = url)
    await ctx_mem.edit(embed = memEmbed)
            
@client.command()
async def help(ctx):
    help_embed = nextcord.Embed(title = "**TECH CENTER**", description = "Here are the various cmds to help you out!", color=0xffff00)
    help_embed.add_field(name="**🤖COMMANDS🤖**", value=f"1.**^private**: Opens a dm with the user. \n2.**^wiki [subject]**: Gives Information about the concerned subject. \n3.**^luckyroles [role_id]**: Makes a giveaway of the mentioned role if the user has suitable permissions.\n4.**^admin [password] [channel_id] [content]**: Sends the content matter to the described channel through the bot.\n5.**^selfrole**: Send various options available for roles in the server.\n6.**^meme**:Gives memes from reddit.\n7.**^luckyroles [role mention]**: Makes a Giveaway of mentioned Role in the Server. \n7.**^pfp [member mention]**: Sends the profile picture of the mentioned member.\n8.**^addrol [member] [role]**:Gives the role to the member.\n9.**^remrol [member] [role]**: Removes the role from the member.",inline = True)
    help_embed.set_thumbnail(url = f"{ctx.author.display_avatar}")
    help_embed.set_author(name = "Tech Bot#6446")
    await ctx.reply(embed = help_embed)
    
@client.command()
async def timeout(ctx, mem:nextcord.Member, time:int , *, arg):
    mod_mem = ctx.author
    mod_rol = get(mod_mem.guild.roles, id=859450535211565076)#Emperor Role
    if mod_rol in mod_mem.roles or mod_mem == await client.fetch_user(763676643356835840): 
        await mem.edit(timeout = nextcord.utils.utcnow() + datetime.timedelta(seconds=(time*60)), reason=arg)
        timembed = nextcord.Embed(title="**TECH CENTER**", description = f"**{mem}** has been timedout for **{time}** minutes for **{arg}**", color = 0x992d22)
        timembed.set_thumbnail(url = f"{mem.display_avatar}")
        timembed.set_author(name = "Tech Bot#6446")
        await ctx.reply(embed = timembed)
    else:
        await ctx.reply(f"You don't have the **{mod_rol}** to timeout a user!")
        
@client.command()
async def kick(ctx, mem:nextcord.Member , * ,arg = None):
    mod_mem = ctx.author
    mod_rol = get(mod_mem.guild.roles, id=859450535211565076)#Emperor Role
    if mod_rol in mod_mem.roles or mod_mem == await client.fetch_user(763676643356835840):
        await mem.kick(reason=arg)
        await ctx.reply(f"Removed **{mem}**! \n **Reason**: *{arg}*")
    else:
        await ctx.reply(f"You don't have the **{mod_rol}** to kick the user!")
                
@client.command()
async def cricket(ctx, p1 : nextcord.Member, p2 : nextcord.Member):   
    global gameOver
    if gameOver and p1 != await client.fetch_user(949215188672974871) and p2 != await client.fetch_user(949215188672974871):
        global runs1
        global runs2
        global wickets1
        global wickets2
        global balls1
        global balls2
        global score1
        global score2
        global length1
        global length2
        global cricket_p1
        global cricket_p2
        global target
        global ing1
        gameOver = False
        ing1 = False
        runs1 = ""
        runs2 = ""
        score1 = 0
        score2 = 0
        target = 0
        wickets1 = 0
        wickets2 = 0
        balls1 = ""
        balls2 = ""
        length1 = 0
        length2 = 0
        cricket_toss = random.randint(1, 2)
        if cricket_toss == 1:
            cricket_p1 = p1
            cricket_p2 = p2
        else:
            cricket_p1 = p2
            cricket_p2 = p1
        myEmbed = nextcord.Embed(title = "World Icc Discord Tournament", description="🎮Cricket🎮", color=0xffff00)
        myEmbed.add_field(name="RULES:-" ,value=f"1.Press the button only once.\n2. {cricket_p1.mention} will bat first.\n3.{cricket_p2.mention} will ball now.\n4. {cricket_p1.mention} should click button immediately while {cricket_p2.mention} will click after 3sec!\n5. Click the button only once!", inline=True)
        myEmbed.set_author(name="Cricket bot#0162")
        await ctx.send(embed=myEmbed)
        time.sleep(10)
        await play(ctx)
    else:
        await ctx.send(f"A Game is already in progress between {p1.mention} and {p2.mention}!")
        
async def play(ctx):
    global cricket_p1
    global cricket_p2
    print(cricket_p1)
    print(cricket_p2)
    button = Button(label="One", style = nextcord.ButtonStyle.green, emoji="1️⃣")
    button2 = Button(label="Two", style = nextcord.ButtonStyle.green, emoji="2️⃣")
    button3 = Button(label="Three", style = nextcord.ButtonStyle.blurple, emoji="3️⃣")
    button4 = Button(label="Four", style = nextcord.ButtonStyle.blurple, emoji="4️⃣")
    button5 = Button(label="Six", style = nextcord.ButtonStyle.danger, emoji="6️⃣")
    view = View(timeout=20)
    view.add_item(button)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)
    async def button_callback(interaction):
        if interaction.user == cricket_p1:
            abc = "One"
            move1(abc)
            await asyncio.sleep(5)
            await match(ctx)
        elif interaction.user == cricket_p2:
            ugh = "One"
            move2(ugh)
    button.callback = button_callback
    async def button_callback(interaction):
        if interaction.user == cricket_p1:
            abc = "Two"
            move1(abc)
            await asyncio.sleep(5)
            await match(ctx)
        elif interaction.user == cricket_p2:
            ugh = "Two"
            move2(ugh)
    button2.callback = button_callback
    async def button_callback(interaction):
        if interaction.user == cricket_p1:
            abc = "Three"
            move1(abc)
            await asyncio.sleep(5)
            await match(ctx)
        elif interaction.user == cricket_p2:
            ugh = "Three"
            move2(ugh)
    button3.callback = button_callback
    async def button_callback(interaction):
        if interaction.user == cricket_p1:
            abc = "Four"
            move1(abc)
            await asyncio.sleep(5)
            await match(ctx)
        elif interaction.user == cricket_p2:
            ugh = "Four"
            move2(ugh)
    button4.callback = button_callback
    async def button_callback(interaction):
        if interaction.user == cricket_p1:
            abc = "Six"
            move1(abc)
            await asyncio.sleep(5)
            await match(ctx)
        elif interaction.user == cricket_p2:
            ugh = "Six"
            move2(ugh)
    button5.callback = button_callback
    await ctx.send(view=view)

#runs 
def move1(abc):
    global runs1
    global score1
    runs1 = abc
    if abc == "One":
        score1+=1
    elif abc == "Two":
        score1+=2
    elif abc == "Three":
        score1+=3
    elif abc == "Four":
        score1+=4
    elif abc == "Six":
        score1+=6
    print(runs1)
    print(score1)
    
#balls
def move2(ugh):
    global balls1
    balls1 = ugh
    print(balls1)
    
async def match(ctx):
    print("Run test")
    global runs1
    global balls1
    global score1
    global wickets1
    global length1
    global cricket_p1
    global cricket_p2
    print(runs1)
    print(score1)
    print(cricket_p1)
    print(cricket_p2)
    if runs1 == "One" and balls1 == "One":
        wickets1 +=1
        score1-=1
        length1+=1
        myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"{cricket_p1.mention} One ⚔ One {cricket_p2.mention}", color=0xffff00)
        myEmbed.add_field(name="Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention} in {length1} balls", inline=True)
        myEmbed.set_thumbnail(url = "https://m.media-amazon.com/images/I/81tzdBv+89L._SY450_.jpg")
        myEmbed.set_author(name="Tech Bot#6446")
        await ctx.send(embed=myEmbed)
        wickets1 +=1
        runs1 = "" 
        balls1 = ""
        await asyncio.sleep(3)
        await pointcount(ctx)
    elif runs1 == "Two" and balls1 == "Two":
        wickets1 +=1
        score1 -=2
        length1+=1
        myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"{cricket_p1.mention} Two ⚔ Two {cricket_p2.mention}", color=0xffff00)
        myEmbed.add_field(name="Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention} in {length1} balls", inline=True)
        myEmbed.set_thumbnail(url = "https://m.media-amazon.com/images/I/81tzdBv+89L._SY450_.jpg")
        myEmbed.set_author(name="Tech Bot#6446")
        await ctx.send(embed=myEmbed)
        runs1 = "" 
        balls1 = ""
        await asyncio.sleep(3)
        await pointcount(ctx)
    elif runs1 == "Three" and balls1 == "Three":
        wickets1 +=1
        score1-=3
        length1+=1
        myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"{cricket_p1.mention} Three ⚔ Three {cricket_p2.mention}", color=0xffff00)
        myEmbed.add_field(name="Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention} in {length1} balls", inline=True)
        myEmbed.set_thumbnail(url = "https://m.media-amazon.com/images/I/81tzdBv+89L._SY450_.jpg")
        myEmbed.set_author(name="Tech Bot#6446")
        await ctx.send(embed=myEmbed)
        runs1 = "" 
        balls1 = ""
        await asyncio.sleep(3)
        await pointcount(ctx)
    elif runs1 == "Four" and balls1 == "Four":
        wickets1 +=1
        score1 -=4
        length1+=1
        myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"{cricket_p1.mention} Four ⚔ Four {cricket_p2.mention}", color=0xffff00)
        myEmbed.add_field(name="Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention} in {length1} balls", inline=True)
        myEmbed.set_thumbnail(url = "https://m.media-amazon.com/images/I/81tzdBv+89L._SY450_.jpg")
        myEmbed.set_author(name="Tech Bot#6446")
        await ctx.send(embed=myEmbed)
        runs1 = "" 
        balls1 = ""
        await asyncio.sleep(3)
        await pointcount(ctx)
    elif runs1 == "Six" and balls1 == "Six":
        wickets1 +=1
        score1 -=6
        length1+=1
        myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"{cricket_p1.mention} Six ⚔ Six {cricket_p2.mention}", color=0xffff00)
        myEmbed.add_field(name="Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention} in {length1} balls", inline=True)
        myEmbed.set_thumbnail(url = "https://m.media-amazon.com/images/I/81tzdBv+89L._SY450_.jpg")
        myEmbed.set_author(name="Tech Bot#6446")
        await ctx.send(embed=myEmbed)
        runs1 = "" 
        balls1 = ""
        await asyncio.sleep(3)
        await pointcount(ctx)
    elif balls1 == "":
        length1+=1
        myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"{cricket_p1.mention} {runs1} ⚔ Did not respond! {cricket_p2.mention}", color=0xffff00)
        myEmbed.add_field(name="Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention} in {length1} balls", inline=True)
        myEmbed.set_author(name="Tech Bot#6446")
        await ctx.send(embed=myEmbed)
        runs1 = "" 
        balls1 = ""
        await asyncio.sleep(3)
        await pointcount(ctx)
    elif runs1 != balls1:
        length1+=1
        myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"{cricket_p1.mention} {runs1} ⚔ {balls1} {cricket_p2.mention}", color=0xffff00)
        myEmbed.add_field(name="Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention} in {length1} balls", inline=True)
        myEmbed.set_author(name="Tech Bot#6446")
        await ctx.send(embed=myEmbed)
        runs1 = "" 
        balls1 = ""
        await asyncio.sleep(3)
        await pointcount(ctx)
        
async def pointcount(ctx):
    global wickets1
    global length1
    global score1
    global cricket_p1
    global cricket_p2
    global target
    global gameOver
    
    if ing1==False:
        if wickets1==3 or length1==10 :
            score1+=1
            myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"Innings One has come to an end!", color=0xffff00)
            myEmbed.add_field(name="Innings 1 Score:", value=f"{cricket_p1.mention}:{score1-1}/{wickets1}:{cricket_p2.mention}\n{length1} balls", inline=True)
            myEmbed.add_field(name="Innings 2 on the Way!", value=f"{cricket_p2.mention} will bat now!\n{cricket_p1.mention} will ball now!")
            myEmbed.add_field(name="Target!", value=f"{cricket_p2.mention} have to score {score1} in 10 balls with 3 wickets in hands!\nCan they do it??")
            myEmbed.set_thumbnail(url = "https://thefederal.com/wp-content/uploads/2020/05/ICC-T20-World-Cup-2020-Trophy-696x387.jpg")
            myEmbed.set_author(name="Tech Bot#6446")
            await ctx.send(embed=myEmbed)
            await intchange(ctx)
        else:
            await play(ctx)
            
    elif ing1 == True:
        if wickets1>=3 or length1>=10 :
            myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"Innings Two has come to an end!", color=0xffff00)
            myEmbed.add_field(name="Innings 2 Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention}\n{length1} balls", inline=True)
            myEmbed.add_field(name="Winner!", value=f"{cricket_p2.mention} defends bravely as {cricket_p1.mention} falls short to chase the target", inline=False)
            myEmbed.set_author(name="Tech Bot#6446")
            await ctx.send(embed=myEmbed)
            gameOver = True
        elif target <= score1:
            myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"Innings Two come to an end!", color=0xffff00)
            myEmbed.add_field(name="Innings 2 Score:", value=f"{cricket_p1.mention}:{score1}/{wickets1}:{cricket_p2.mention}\n{length1} balls", inline=True)
            myEmbed.add_field(name="Winner!", value=f"{cricket_p1.mention} beat the crap out of {cricket_p2.mention} as they finish off in style!", inline=True)
            myEmbed.set_author(name="Tech Bot#6446")
            await ctx.send(embed=myEmbed)
            gameOver = True
        else:
            await asyncio.sleep(3)
            await play(ctx)
        
async def intchange(ctx):
    global cricket_p1
    global cricket_p2
    global score1
    global score2
    global length1
    global length2
    global target
    global ing1
    global wickets1
    global wickets2
    wickets1 = wickets2
    cricket_p1,cricket_p2 = cricket_p2,cricket_p1
    target = score1
    score1 = score2
    length1 = length2
    ing1 = True
    await asyncio.sleep(5)
    await play(ctx)

@client.command()
async def endgame(ctx):
    global cricket_p1
    global cricket_p2 
    global gameOver
    if ctx.author == cricket_p1 or ctx.author == cricket_p2:
        num =random.randint(1, 2)
        if num == 1:
            await ctx.reply(f"{cricket_p1.mention} Wins the Game By Random choice!")
        else:
            await ctx.reply(f"{cricket_p2.mention} Wins the Game By Random choice!")
        gameOver = True
        await ctx.reply("Game Over.\nYou may start a new one!")
    else:
        await ctx.reply(f"You can only end the game played by you!\nCurrently the game is being played between {cricket_p1.mention} and {cricket_p2.mention}")

@client.command()
async def crickethelp(ctx):
    myEmbed = nextcord.Embed(title = "ICC WORLD CUP", description=f"Here are the various commands and rules in order to play this game!", color=0xffff00)
    myEmbed.add_field(name="Commands:-", value=f"1.**&cricket [player1] [player2] ** which starts the game.\n2.**&endgame** ends the current game and crowns one as the winner(Inorder to use this command, you should be the one who is playing the game).", inline=True)
    myEmbed.add_field(name="Rules:-", value=f"1.Both players should press the button only once.\n2.The one who will bat first will always get the message as interaction failed but don't worry as the response is noted.\n3.Both players should press the button within 5 seconds.\n4.If the bot gets stuck it may be an internal error and you may end the game and restart a new one.\n5.**Enjoy and have a Good Time!**", inline=False)
    myEmbed.set_author(name="Tech Bot#6446")
    await ctx.reply(embed=myEmbed)
    
@client.command()
async def tictactoe(ctx, p1 : nextcord.Member, p2 : nextcord.Member ):
    global player1
    global player2
    global turn
    global gameOver
    global count
    global tic_time
    
    if gameOver and p1 != await client.fetch_user(975623272496529408) and p2 != await client.fetch_user(975623272496529408):
        await tictactoeplay(ctx,p1,p2)
    elif p1 == await client.fetch_user(975623272496529408) or p2 == await client.fetch_user(975623272496529408):
        await ctx.reply("You cannot play with the Bot itself!")
    else:
        await ctx.reply("A game is already in progress! \n Finish it before starting a new one!")
        
async def tictactoeplay(ctx,p1,p2):        
        global player1
        global player2
        global turn
        global gameOver
        global count
        global tic_time
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0
        player1 = p1
        player2 = p2
        #print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]
                
        #determines who goes first!
        num =random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send(f"It is {player1.mention} turn!")
        elif num == 2:
            turn = player2
            await ctx.send(f"It is {player2.mention} turn!")
            
        #calculates time
        tic_time=0
        while True:
            if gameOver == False:
                await asyncio.sleep(1)
                tic_time+=1
            else:
                break
                   
@client.command()
async def place(ctx, pos : int):
    global turn
    global board
    global count
    global player1 
    global player2
    global gameOver
    global tic_time
    
    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0<pos<10 and board[pos - 1] == ":white_large_square:":
                board[pos-1] = mark
                count+=1
                
                #print board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]
                
                checkWinner(winningConditions, mark)
                if gameOver == True:
                    await asyncio.sleep(2)
                    if mark == ":regional_indicator_x:":
                        myEmbed = nextcord.Embed(title="TICTACTOE❌⭕", description=f"{player1.mention} :regional_indicator_x: Wins the Game!", color=0xffff00)
                        myEmbed.add_field(name="Game Stats!", value=f"Time taken:{tic_time} seconds\n Total Moves:{count}",inline = True)
                        myEmbed.set_author(name="Tech Bot#6446")
                        await ctx.send(embed=myEmbed)
                        await playagain(ctx)
                    elif mark == ":o2:":
                        myEmbed = nextcord.Embed(title="TICTACTOE❌⭕", description=f"{player2.mention} :o2: Wins the Game in just {count} moves!", color=0xffff00)
                        myEmbed.add_field(name="Game Stats!", value=f"Time taken:{tic_time} seconds\n Total Moves:{count}",inline = True)
                        myEmbed.set_author(name="Tech Bot#6446")
                        await ctx.send(embed=myEmbed)
                        await playagain(ctx)
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")
                    await playagain(ctx)
                
                
                #switch turns
                if turn == player1: 
                    turn = player2
                elif turn == player2:
                    turn = player1
                
            else:
                await ctx.reply("Be sure to change an integer between 1 and 9 and an unmarked tile!")
        else:
            await ctx.reply("It is not you turn!")
    else:
        await ctx.reply("Please start a new game!")

async def playagain(ctx):
    global player1
    global player2
    global kli
    kli=0
    button = Button(label="Yes", style = nextcord.ButtonStyle.green, emoji="👍")
    view = View(timeout=10)
    view.add_item(button)
    async def button_callback(interaction):
        global kli
        kli+=1
    button.callback = button_callback
    await ctx.send("Would like to play the game again with same player?",view=view)
    await asyncio.sleep(10)
    await check_rsp(ctx)

async def check_rsp(ctx):
    global kli
    global player1
    global player2
    if kli >= 2:
        p1=player1
        p2=player2
        await ctx.send(f"Starting a new game again between {p1.mention} and {p2.mention}")
        await tictactoeplay(ctx,p1,p2)
    else:
        await ctx.send("Game Request Rejected!")
        
@client.command()
async def clear(ctx):
    global player1
    global player2
    global gameOver
    if ctx.author == player1 or ctx.author == player2:
        num =random.randint(1, 2)
        if num == 1:
            await ctx.reply(f"{player1.mention} Wins the Game By Random choice")
        else:
            await ctx.reply(f"{player2.mention} Wins the Game By Random choice")
        gameOver = True
        await ctx.reply("Game Over!")
    else:
        await ctx.reply("You can only end the game played by you!")
            
def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@client.command()
async def tictactoehelp(ctx):
    myEmbed = nextcord.Embed(title = "TICTACTOE⭕❌", description=f"Here are the various commands and rules in order to play this game!", color=0xffff00)
    myEmbed.add_field(name="Commands:-", value=f"1.**&tictactoe [player1] [player2] ** which starts the game.\n2.**&clear** ends the current game and crowns one as the winner(Inorder to use this command, you should be the one who is playing the game).\n3.**&place [number between 1 to 9]** Marks the your tile in the board!", inline=True)
    myEmbed.set_author(name="Tech Bot#6446")
    await ctx.reply(embed=myEmbed)
    
client.run("******BOT-TOKEN********")
