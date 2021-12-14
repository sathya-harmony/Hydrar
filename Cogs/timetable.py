

#from _typeshed import Self
from discord.ext import commands, tasks
import time
from math import *
from modules.common import *
from datetime import date, datetime
import calendar


class Timetable(commands.Cog):
    def __init__(self,  client):

        self.client = client
        self.checktimetable.start()

    timetable =\
        {
            "monday": {"2:55": "Social Science",
                       "3:40": "2nd language",
                       "4:30": "Short Break",
                       "4:40": "English",
                       "5:25": "IT",
                       "6:10": "Chemistry/Biology",
                       "6:55": "Lunch Break",
                       "7:25": "Math"},
            "tuesday": {"3:00": "Math",
                        "3:40": "Biology/Chemistry",
                        "4:30": "Short Break",
                        "4:40": "Physics",
                        "5:25": "Social Science",
                        "6:10": "English",
                        "6:55": "Lunch Break",
                        "7:25": "2nd Language"},
            "wednesday": {"2:55": "Chemistry",
                          "3:40": "Social Science",
                          "4:30": "Short Break",
                          "4:40": "Math",
                          "5:25": "IT",
                          "6:10": "English",
                          "6:55": "Lunch Break",
                          "7:25": "2nd Language"},
            "thursday": {"2:55": "English",
                         "3:40": "2nd Language",
                         "4:30": "Short Break",
                         "4:40": "Social Science",
                         "5:25": "Math",
                         "6:10": "Physics",
                         "6:55": "Lunch Break",
                         "7:25": "Math"},
            "friday":   {"2:55": "2nd Language",
                         "3:40": "IT",
                         "4:30": "Short Break",
                         "4:40": "Art",
                         "5:25": "Math",
                         "6:10": "Biology/Chemistry",
                         "6:55": "Lunch Break",
                         "7:25": "Social Science"}

        }
    guild_id = 915620989293977620
    channel_id = 915620989293977622
    subject = []
    subject2 = []

    @tasks.loop(seconds=60.0)
    async def checktimetable(self):
        curr_date = date.today()
        current_day = str(calendar.day_name[curr_date.weekday()]).lower()

        if current_day in self.timetable.keys():
            day = current_day

        time = datetime.today()
        current_time_parsed = f"{time.hour}:{time.minute}"

        try:
            subject = self.timetable[day][current_time_parsed]
            self.subject = subject
            self.subject2 = subject

        except:
            pass
        if self.subject:
            channel = self.client.get_channel(self.channel_id)

            if self.subject == "Short Break" or self.subject == "Lunch Break":
                await channel.send("Its break time! Go and eat nicely! (Or watch youtube lol)")
                self.subject = None
            else:
                await channel.send(f"@everyone It's **{self.subject}** period! Please join right now! (P.S it might be substitution so don't blast me.)")
                self.subject = None

    @commands.command()
    async def period(self, ctx):
        if self.subject2:
            if self.subject2 == ("Short Break" or "Lunch Break"):
                await ctx.reply(f"It's break time hippy.")

            else:

                await ctx.reply(f"Current period is : **{self.subject2}**")
        else:
            await ctx.reply("No period is currently going on!")


def setup(client):
    client.add_cog(Timetable(client))
