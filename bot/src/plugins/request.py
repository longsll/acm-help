from nonebot import on_command,on_request
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Bot, Message, GroupMessageEvent,MessageEvent,PrivateMessageEvent,FriendRequestEvent,GroupRequestEvent
from nonebot.params import CommandArg
from nonebot import require
import asyncio

self_add=on_request(priority=60)
group_add=on_request(priority=60)

@self_add.handle()
async def ad_f(bot: Bot, event: FriendRequestEvent):
    await event.approve(bot)
    id = int(event.get_user_id())
    await asyncio.sleep(1)
    await bot.call_api('send_private_msg',user_id=id,message=Message('''---bot---
cf/precf :返回接下来三场/之前三场codeforces赛事
atc/preatc :返回接下来三场/之前三场atcoder赛事
nc/prenc :返回接下来三场/之前三场牛客赛事
today :查看今日赛事
next ：返回接下来一场赛事
update :更新
help ：帮助
-支持私聊，加好友进群自动同意
-有事联系QQ:1506911471
'''
    ))

@group_add.handle()
async def ad_f(bot: Bot, event: GroupRequestEvent):
    await event.approve(bot)
    await asyncio.sleep(1)
