# noinspection PyUnresolvedReferences
import discord
import random
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.chat_formatting import box, pagify, escape_mass_mentions
from random import choice, randint
import xkcd

__author__ = "shibe "


class Shibe:
    """ShibeBot's Commands"""

    def __init__(self, bot):
        self.bot = bot
        self.base = 'data/doge/'

    # --Start Much E-sports Image embeds , Images go in /data/images/
    @commands.command(pass_context=True)
    async def yoshi(self, context):
        """YOSHI"""
        await self.bot.send_file(context.message.channel, '{}images/yoshi.png'.format(self.base))

    @commands.command(pass_context=True)
    async def bun(self, context):
        """bun"""
        await self.bot.send_file(context.message.channel, '{}images/bun.png'.format(self.base))

    @commands.command(pass_context=True)
    async def bossbattle(self, context):
        """Boss Battles be like"""
        await self.bot.send_file(context.message.channel, '{}images/bossbattle.gif'.format(self.base))

    @commands.command(pass_context=True)
    async def shibe(self, context):
        """SHIBE"""
        await self.bot.send_file(context.message.channel, '{}images/shibe.png'.format(self.base))

    @commands.command(pass_context=True)
    async def order66(self, context):
        """order66"""
        await self.bot.send_file(context.message.channel, '{}images/order66.gif'.format(self.base))

    @commands.command(pass_context=True)
    async def ringer(self, context):
        """ringer"""
        await self.bot.send_file(context.message.channel, '{}images/ringer.gif'.format(self.base))

    @commands.command(pass_context=True)
    async def claiborne(self, context):
        """claiborne"""
        await self.bot.send_file(context.message.channel, '{}images/claiborne.jpg'.format(self.base))

    @commands.command(pass_context=True)
    async def jeff(self, context):
        """jeff"""
        await self.bot.send_file(context.message.channel, '{}images/jeff.png'.format(self.base))

    @commands.command(pass_context=True)
    async def underpowered(self, context):
        """underpowered"""
        await self.bot.send_file(context.message.channel, '{}images/underpowered.gif'.format(self.base))

    @commands.command(pass_context=True)
    async def doge(self, context):
        """doge"""
        await self.bot.send_file(context.message.channel, '{}images/doge.png'.format(self.base))

    @commands.command(pass_context=True)
    async def muffin(self, context):
        """muffin"""
        await self.bot.send_file(context.message.channel, '{}images/muffin.png'.format(self.base))

    @commands.command(pass_context=True)
    async def rex(self, context):
        """rex"""
        await self.bot.send_file(context.message.channel, '{}images/rex.jpg'.format(self.base))

    @commands.command(pass_context=True)
    async def potato(self, context):
        """potato"""
        await self.bot.send_file(context.message.channel, '{}images/potato.png'.format(self.base))

    @commands.command(pass_context=True)
    async def moo(self, context):
        """moo"""
        await self.bot.send_file(context.message.channel, '{}images/cody.png'.format(self.base))

    @commands.command(pass_context=True)
    async def pie(self, ctx):
        """pie"""
        await self.bot.send_file(ctx.message.channel, '{}images/pie.png'.format(self.base))

    @commands.command(pass_context=True)
    async def hadoken(self, ctx):
        """hadoken"""
        await self.bot.delete_message(ctx.message)
        await self.bot.send_file(ctx.message.channel, '{}images/hadoken.gif'.format(self.base))

    @commands.command(pass_context=True)
    async def summongreg(self, ctx):
        """summon greg"""
        await self.bot.send_file(ctx.message.channel, '{}images/summongreg.gif'.format(self.base))

    @commands.command(pass_context=True)
    async def scoofy(self, context):
        """scoofy"""
        await self.bot.send_file(context.message.channel, '{}images/scoofy.jpg'.format(self.base))

    @commands.command(pass_context=True)
    async def fine(self, context):
        """fine"""
        await self.bot.send_file(context.message.channel, '{}images/fine.png'.format(self.base))

    @commands.command(pass_context=True)
    async def thunder(self, context):
        """thunder"""
        await self.bot.send_file(context.message.channel, '{}images/thunder.gif'.format(self.base))

    @commands.command(pass_context=True)
    async def jack(self, context):
        """jack"""
        await self.bot.send_file(context.message.channel, '{}images/jack.png'.format(self.base))

    @commands.command(pass_context=True)
    async def pie2(self, context):
        """pie2"""
        await self.bot.send_file(context.message.channel, '{}images/pie2.png'.format(self.base))

    @commands.command(pass_context=True)
    async def what9000(self, context):
        """power level!?"""
        await self.bot.send_file(context.message.channel, '{}images/9000.gif'.format(self.base))

    @commands.command(pass_context=True)
    async def homer(self, context):
        """abandon thread"""
        await self.bot.send_file(context.message.channel, '{}images/homer.gif'.format(self.base))

    # --END Image embeds

    @commands.command(pass_context=True, no_pm=True, aliases=["suhdude"])
    async def suh(self, ctx):
        """suh dude"""
        await self.bot.delete_message(ctx.message)
        await self.bot.say(":v: SUH DUDE :v: ")

    @commands.command(pass_context=True, no_pm=True)
    async def greg(self, ctx):
        """ShibeBot , ATTACK!"""
        await self.bot.delete_message(ctx.message)
        await self.bot.say("ShibeBot growls and attacks Greg's face")

    @commands.command()
    async def ark(self):
        """Get's link for Mandrew ARK"""
        em = discord.Embed(title='Click To Connect to Mandrew ARK',
                           description='steam://connect/71.93.28.250:27015 \n Whisper a Doge Master for the password \n\n NOTE: If it\'s your first time, You\'ll have to reconnect multiple times until all the mods are loaded. You can track workshop content download progress in your steam client in between reconnects',
                           colour=0xDEADBF)
        em.set_author(name='ShibeBot', icon_url='http://i.imgur.com/mYdLixs.png')
        await self.bot.say(embed=em)

    @commands.command()
    async def piefact(self):
        """100 Percent PieFacts"""
        lines = open('{}/piefacts/piefacts.txt'.format(self.base)).read().splitlines()
        piefact = random.choice(lines)
        await self.bot.say(piefact)

    @commands.command()
    async def pecker(self):
        """How-to be safe"""
        lines = open('{}/pecker/pecker.txt'.format(self.base)).read().splitlines()
        pecker = random.choice(lines)
        await self.bot.say(pecker)

def setup(bot):
    n = Shibe(bot)
    bot.add_cog(n)
