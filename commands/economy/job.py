import discord
from discord.ext import commands
import json
import random

# done 12/15/25

OWNER_ID = 586225258269245538
DB_FILE = "database.json"
VAR_FILE = "variables.json"


async def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)


async def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=2)


async def load_jobs():
    with open(VAR_FILE, "r") as f:
        data = json.load(f)
        return data.get("jobs", {})


class Job(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # #job
    @commands.group(invoke_without_command=True)
    async def job(self, ctx, *, member: discord.Member = None):
        async with ctx.typing():
            if member is None:
                member = ctx.author

            db = await load_db()
            jobs_db = db.get("Job", {})
            user_jobs = jobs_db.get(str(member.id), [])
            if user_jobs:
                job_descriptions = []
                for job_entry in user_jobs:
                    job_name = job_entry.get("job", "Unknown Job")
                    raise_amt = job_entry.get("raise", 0)
                    if raise_amt:
                        job_descriptions.append(f"{job_name} (+{raise_amt} raise)")
                    else:
                        job_descriptions.append(f"{job_name}")
                description = "\n".join(job_descriptions)
            else:
                description = "Unemployed"

            embed = discord.Embed(
                title=f"Jobs for {member.display_name}",
                description=description,
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)

    # #job apply
    @job.command()
    async def apply(self, ctx):
        async with ctx.typing():
            db = await load_db()
            jobs = await load_jobs()
            user_id = str(ctx.author.id)

            success_jobs = []
            for job_name, pay in jobs.items():
                chance = (0.01 ** (1 / 90)) ** (pay - 10)
                if random.random() < chance:
                    success_jobs.append(job_name)

            if success_jobs:
                selected_job = random.choice(success_jobs)
                jobs_db = db.setdefault("Job", {})
                current_jobs = jobs_db.get(user_id, [])
                if not isinstance(current_jobs, list):
                    current_jobs = []
                current_jobs.append({"job": selected_job, "raise": 0})
                jobs_db[user_id] = current_jobs
                await save_db(db)

                embed = discord.Embed(
                    title="Job Application Successful!",
                    description=f"You got the job: **{selected_job}**",
                    color=discord.Color(0x80FF80),
                )
            else:
                embed = discord.Embed(
                    title="Job Application Failed",
                    description="Better luck next time!",
                    color=discord.Color(0x80FF80),
                )

            await ctx.reply(embed=embed)

    # #job list
    @job.command()
    async def list(self, ctx):
        async with ctx.typing():
            jobs = await load_jobs()
            description = ""
            for i, (job_name, pay) in enumerate(jobs.items(), start=1):
                description += f"{i}. {job_name} - ${pay}/hr\n"

            embed = discord.Embed(
                title="Available Jobs",
                description=description,
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)

    # #jobs
    @commands.command(name="jobs")
    async def jobs(self, ctx):
        await self.list(ctx)

    # #job give
    @job.command()
    async def give(self, ctx, *, job: str = None):
        if ctx.author.id != OWNER_ID:
            embed = discord.Embed(
                title="Permission Denied",
                description="You do not have permission to use this command.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)
            return

        async with ctx.typing():
            args = job.split() if job else []
            jobs_data = await load_jobs()
            job_list = list(jobs_data.keys())
            selected_job = None
            member = None

            if ctx.message.mentions:
                member = ctx.message.mentions[0]
                args = [
                    arg
                    for arg in args
                    if arg
                    not in [member.mention, f"<@{member.id}>", f"<@!{member.id}>"]
                ]
            else:
                member = ctx.author

            job_in = " ".join(args).strip() if args else None

            if not job_in:
                embed = discord.Embed(
                    title="Missing job argument",
                    description="You must provide the job index or job name.",
                    color=discord.Color(0x80FF80),
                )
                await ctx.reply(embed=embed)
                return

            try:
                job_index = int(job_in)
                if not 1 <= job_index <= len(job_list):
                    raise ValueError
                selected_job = job_list[job_index - 1]
            except ValueError:
                lower_map = {jn.lower(): jn for jn in job_list}
                job_name_matched = lower_map.get(job_in.lower())
                if job_name_matched:
                    selected_job = job_name_matched
                else:
                    embed = discord.Embed(
                        title="Invalid Job",
                        description=f"Could not find job: '{job_in}'. Use `#job list` to see valid jobs.",
                        color=discord.Color(0x80FF80),
                    )
                    await ctx.reply(embed=embed)
                    return

            db = await load_db()
            jobs_db = db.setdefault("Job", {})
            user_id = str(member.id)
            current_jobs = jobs_db.get(user_id, [])
            if not isinstance(current_jobs, list):
                current_jobs = []
            current_jobs.append({"job": selected_job, "raise": 0})
            jobs_db[user_id] = current_jobs
            await save_db(db)

            embed = discord.Embed(
                title="Job Assigned",
                description=f"{member.mention} was given the job: **{selected_job}**",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)

    # #job remove
    @job.command()
    async def remove(self, ctx, *, job: str = None):
        if ctx.author.id != OWNER_ID:
            embed = discord.Embed(
                title="Permission Denied",
                description="You do not have permission to use this command.",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)
            return

        async with ctx.typing():
            args = job.split() if job else []
            jobs_data = await load_jobs()
            job_list = list(jobs_data.keys())
            member = None

            if ctx.message.mentions:
                member = ctx.message.mentions[0]
                args = [
                    arg
                    for arg in args
                    if arg
                    not in [member.mention, f"<@{member.id}>", f"<@!{member.id}>"]
                ]
            else:
                member = ctx.author

            job_in = " ".join(args).strip() if args else None

            if not job_in:
                embed = discord.Embed(
                    title="Missing job argument",
                    description="You must provide the job index or job name to remove.",
                    color=discord.Color(0x80FF80),
                )
                await ctx.reply(embed=embed)
                return

            db = await load_db()
            jobs_db = db.setdefault("Job", {})
            user_id = str(member.id)
            current_jobs = jobs_db.get(user_id, [])
            if not isinstance(current_jobs, list):
                current_jobs = []

            if not current_jobs:
                embed = discord.Embed(
                    title="No Jobs",
                    description=f"{member.mention} has no jobs to remove.",
                    color=discord.Color(0x80FF80),
                )
                await ctx.reply(embed=embed)
                return

            removed_job = None
            try:
                job_index = int(job_in)
                if not 1 <= job_index <= len(current_jobs):
                    raise ValueError
                job_entry = current_jobs[job_index - 1]
                job_name = (
                    job_entry.get("job", "Unknown Job")
                    if isinstance(job_entry, dict)
                    else str(job_entry)
                )
                removed_job = current_jobs.pop(job_index - 1)
            except ValueError:
                lower_job_in = job_in.lower()
                for idx, job_entry in enumerate(current_jobs):
                    job_name = ""
                    if isinstance(job_entry, dict):
                        job_name = job_entry.get("job", "")
                    else:
                        job_name = str(job_entry)
                    if job_name.lower() == lower_job_in:
                        removed_job = current_jobs.pop(idx)
                        break

                if removed_job is None:
                    embed = discord.Embed(
                        title="Invalid Job",
                        description=f"Could not find job to remove: '{job_in}'. Use `#job` to see current jobs.",
                        color=discord.Color(0x80FF80),
                    )
                    await ctx.reply(embed=embed)
                    return

            jobs_db[user_id] = current_jobs
            await save_db(db)

            if isinstance(removed_job, dict):
                rm_job_name = removed_job.get("job", "Unknown Job")
            else:
                rm_job_name = str(removed_job)

            embed = discord.Embed(
                title="Job Removed",
                description=f"{member.mention} had the job removed: **{rm_job_name}**",
                color=discord.Color(0x80FF80),
            )
            await ctx.reply(embed=embed)

    # #job raise
    @job.group(name="raise", invoke_without_command=True)
    async def _raise(self, ctx):
        embed = discord.Embed(
            title="Job Raise Commands",
            description=(
                "`#job raise set [@user] <job/index> <amount>`\n"
                "`#job raise reset [@user] <job/index>`"
            ),
            color=discord.Color(0x80FF80),
        )
        await ctx.reply(embed=embed)

    # #job raise set
    @_raise.command(name="set")
    async def raise_set(self, ctx, *, args: str = None):
        if ctx.author.id != OWNER_ID:
            await ctx.reply(
                embed=discord.Embed(
                    title="Permission Denied",
                    description="You do not have permission to use this command.",
                    color=discord.Color(0x80FF80),
                )
            )
            return

        if not args:
            await ctx.reply("Missing arguments.")
            return

        parts = args.split()

        if ctx.message.mentions:
            member = ctx.message.mentions[0]
            parts = [
                p
                for p in parts
                if p not in (member.mention, f"<@{member.id}>", f"<@!{member.id}>")
            ]
        else:
            member = ctx.author

        if len(parts) < 2:
            await ctx.reply(
                "You must specify a job (name or index) and a raise amount."
            )
            return

        job_in = " ".join(parts[:-1])
        try:
            raise_amount = float(parts[-1])
        except ValueError:
            await ctx.reply("Raise amount must be a number.")
            return

        db = await load_db()
        jobs_db = db.get("Job", {})
        user_jobs = jobs_db.get(str(member.id), [])

        if not user_jobs:
            await ctx.reply(f"{member.mention} has no jobs.")
            return

        target_job = None

        try:
            idx = int(job_in) - 1
            if 0 <= idx < len(user_jobs):
                target_job = user_jobs[idx]
        except ValueError:
            pass

        if not target_job:
            for job_entry in user_jobs:
                if job_entry.get("job", "").lower() == job_in.lower():
                    target_job = job_entry
                    break

        if not target_job:
            await ctx.reply("Job not found.")
            return

        target_job["raise"] = raise_amount
        jobs_db[str(member.id)] = user_jobs
        await save_db(db)

        await ctx.reply(
            embed=discord.Embed(
                title="Raise Set",
                description=f"{member.mention}'s **{target_job['job']}** raise set to **{raise_amount}**",
                color=discord.Color(0x80FF80),
            )
        )

    # #job raise reset
    @_raise.command(name="reset")
    async def raise_reset(self, ctx, *, args: str = None):
        if ctx.author.id != OWNER_ID:
            await ctx.reply(
                embed=discord.Embed(
                    title="Permission Denied",
                    description="You do not have permission to use this command.",
                    color=discord.Color(0x80FF80),
                )
            )
            return

        if not args:
            await ctx.reply("Missing arguments.")
            return

        parts = args.split()

        if ctx.message.mentions:
            member = ctx.message.mentions[0]
            parts = [
                p
                for p in parts
                if p not in (member.mention, f"<@{member.id}>", f"<@!{member.id}>")
            ]
        else:
            member = ctx.author

        job_in = " ".join(parts)

        db = await load_db()
        jobs_db = db.get("Job", {})
        user_jobs = jobs_db.get(str(member.id), [])

        if not user_jobs:
            await ctx.reply(f"{member.mention} has no jobs.")
            return

        target_job = None

        try:
            idx = int(job_in) - 1
            if 0 <= idx < len(user_jobs):
                target_job = user_jobs[idx]
        except ValueError:
            pass

        if not target_job:
            for job_entry in user_jobs:
                if job_entry.get("job", "").lower() == job_in.lower():
                    target_job = job_entry
                    break

        if not target_job:
            await ctx.reply("Job not found.")
            return

        target_job["raise"] = 0
        jobs_db[str(member.id)] = user_jobs
        await save_db(db)

        await ctx.reply(
            embed=discord.Embed(
                title="Raise Reset",
                description=f"{member.mention}'s **{target_job['job']}** raise has been reset.",
                color=discord.Color(0x80FF80),
            )
        )


async def setup(bot):
    await bot.add_cog(Job(bot))
