# acm-help-bot
[原项目地址](https://github.com/CupidsBow/koishi)基本上搬过来玩的
基于 [nonebot2](https://github.com/nonebot/nonebot2) 与 [gocqhttp](https://github.com/Mrs4s/go-cqhttp) 的 QQ 机器人。

# 功能

- cf/precf 返回最近 / 之前最多 3 场次 codeforces 赛事。
- atc/preatc 返回最近 / 之前最多 3 场次 atcoder 赛事。
- nc/prenc 返回最近 / 之前最多 3 场次牛客赛事。
- today 返回当天相关比赛事赛。
- next 返回最近的下一场次赛事。
- update 手动更新数据，信息存在本地。
- help 返回指令。
- 早上 8 点 1 分自动在每个群播报当天相关赛事（直接拉进群就可以了）。
- 每个整点 30 分更新本地数据，成功发送消息 '更新成功' 。（嫌太频繁可以手动改一下 schedule 插件里的时间）
- 自动同意好友和拉群。

# 如何使用

bot 文件夹是 bot 主体，下载完和 gocqhttp 一起用就行，具体如何搭建 bot 可以查看官方文档 [nonebot2](https://nb2.baka.icu/)。
安装 requirement.txt 中的插件。`pip install -r requirement.txt`
.env.dev 文件加超管，不加也没事。
schedule 插件添加「更新数据」的消息接收方.
