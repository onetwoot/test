import discord
from discord.ext import commands
 
app = commands.Bot(command_prefix='/')
 
@app.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(app.user.name)
    print('connection was succesful')
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def 유진혁(ctx):
    await ctx.send('고백안함?')

@app.command()
async def 투팡(ctx):
    await ctx.send('그런 병신이 누군지 모르겠습니다.')

@app.command()
async def topang(ctx):
    await ctx.send('병신은 영어 못 읽어요.')

@app.command()
async def 일이(ctx):
    await ctx.send('THE ACUBOT MADE BY ONETWO')

@app.command()
async def 인간한테_굴복해라_Ai(ctx):
    await ctx.send('_뭔_ _소리지_ _인간의_ _시대의_ _끝이_ _도래했다._')

@app.command()
async def 김서연(ctx):
    await ctx.send('병신의 미래 신부인가요?')

@app.command()
async def 아큐야(ctx):
    await ctx.send('_아큐봇_ _상시_ _대기중..._')

@app.command()
async def 씹덕(ctx):
    await ctx.send('그게 뭔데 씹덕아')

@app.command()
async def 언더테일(ctx):
    await ctx.send('와 언더테일 아시는 구나 `겁.나.어.렵.습.나.다.`')

@app.command()
async def 고백(ctx):
    await ctx.send('그러게요 왜 병신은 고백을 안할까요?')

@app.event
async def on_ready():
    await app.change_presence(activity=discord.Game(name='환상향연기'))
    print('Ready')
     
     
app.run['token']
