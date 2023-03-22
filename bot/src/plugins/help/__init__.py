from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent,MessageEvent,PrivateMessageEvent
from nonebot.params import CommandArg
from nonebot import require

help=on_command('help', priority=1)

@help.handle()
async def send_receive(bot: Bot, event: MessageEvent):
    res='''cf/precf :返回接下来三场/之前三场codeforces赛事
atc/preatc :返回接下来三场/之前三场atcoder赛事
nc/prenc :返回接下来三场/之前三场牛客赛事
today :查看今日赛事
next ：返回接下来一场赛事
update :更新
help ：帮助
'''
    await help.finish(res)