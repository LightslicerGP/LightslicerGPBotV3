import discord
from discord.ext import commands
import json

# done 12/19/25


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="test")
    async def test(self, ctx, message_id: int):
        # Try to fetch the message by ID from the current channel
        try:
            message = await ctx.channel.fetch_message(message_id)
        except discord.NotFound:
            return await ctx.reply("Message not found in this channel.")
        except discord.Forbidden:
            return await ctx.reply("I do not have permission to read this message.")
        except discord.HTTPException:
            return await ctx.reply(
                "Failed to fetch the message due to a network error."
            )

        if not message.embeds:
            return await ctx.reply("That message has no embeds.")

        embed = message.embeds[0]
        raw = embed.to_dict()
        raw_json = json.dumps(raw, indent=2, ensure_ascii=False)
        await ctx.reply(
            f"Raw embed JSON from message `{message_id}`:\n```json\n{raw_json}\n```"
        )


async def setup(bot):
    await bot.add_cog(Test(bot))
