import datetime

import discord
from discord.ext import commands

import logger

bot = commands.Bot(command_prefix="!!", owner_ids=[674813875291422720])


@bot.event
async def on_ready():
    print("가동 시작")


# @bot.listen()
# async def on_message(msg):
#         await logger.file(msg)
#         time = datetime.datetime.now()
#         time = (
#             str(time.year)
#             + "/"
#             + str(time.month)
#             + "/"
#             + str(time.day)
#             + " "
#             + str(time.hour)
#             + ":"
#             + str(time.minute)
#             + ":"
#             + str(time.second)
#         )
#         context = (
#             "["
#             + time
#             + "]"
#             + msg.author.name
#             + "("
#             + msg.author.name
#             + "): "
#             + msg.content
#             + "\n"
#         )
#         file = open("log.txt", "a", encoding="utf8")
#         file.write(context)
#         file.close()


@bot.command()
async def 로깅(ctx, channel):
    if ctx.author.guild_permissions.administrator == True or ctx.author.id in bot.owner_ids:
        logch = (
            channel.replace("<", "").replace(">", "").replace("#", "").replace(" ", "").strip()
        )
        res = await logger.set_ch(ctx.guild.id, int(logch))
        if res:
            em = discord.Embed(color=0x00FF00)
            em.add_field(
                name="로깅 채널", value=channel + " 채널로 로깅 채널이 설정되었습니다.", inline=False
            )
            await ctx.send(embed=em)
        else:
            em = discord.Embed(color=0x00FF00)
            em.add_field(name="로깅 채널", value="```!!로깅 채널```\n양식에 따르십시오!", inline=False)
            await ctx.send(embed=em)


@bot.event
async def on_message_edit(bmsg, msg):
        if msg.guild != None:
            await logger.edit_log(bmsg, msg)
        time = datetime.datetime.now()
        time = (
            str(time.year)
            + "/"
            + str(time.month)
            + "/"
            + str(time.day)
            + " "
            + str(time.hour)
            + ":"
            + str(time.minute)
            + ":"
            + str(time.second)
        )
        context = (
            "["
            + time
            + "]"
            + msg.author.name
            + "("
            + msg.author.name
            + "): "
            + bmsg.content
            + " > "
            + msg.content
            + "\n"
        )
        file = open("log.txt", "a", encoding="utf8")
        file.write(context)
        file.close()


@bot.event
async def on_raw_bulk_message_delete(msglist, ch):
    if bot.get_channel(ch).guild != None:
        await logger.del_bulk_log(bot, msglist, ch)


@bot.event
async def on_message_delete(msg):
        try:
            serverid = msg.guild.id
        except:
            serverid = "dm"
        if not serverid == "dm":
            await logger.del_log(msg)

        time = datetime.datetime.now()
        time = (
            str(time.year)
            + "/"
            + str(time.month)
            + "/"
            + str(time.day)
            + " "
            + str(time.hour)
            + ":"
            + str(time.minute)
            + ":"
            + str(time.second)
        )
        context = (
            "["
            + time
            + "]"
            + msg.author.name
            + "("
            + msg.author.name
            + "): <삭제>"
            + msg.content
            + "\n"
        )
        file = open("log.txt", "a", encoding="utf8")
        file.write(context)
        file.close()

bot.run("token")
