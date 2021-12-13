

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
            "monday": {"12:06": "Social Science",
                       "12:07": "IInd language",
                       "4:30": "Short Break",
                       "4:40": "English",
                       "5:25": "IT",
                       "6:10": "Chemistry/Biology",
                       "6:55": "Lunch Break",
                       "7:25": "Math"},
            "tuesday": {"2:55": "Math",
                        "3:40": "Biology/Chemistry",
                        "4:30": "Short Break",
                        "4:40": "Physics",
                        "5:25": "Social Science",
                        "6:10": "English",
                        "6:55": "Lunch Break",
                        "7:25": "IInd Language"},
            "wednesday": {"2:55": "Chemistry",
                          "3:40": "Social Science",
                          "4:30": "Short Break",
                          "4:40": "Math",
                          "5:25": "IT",
                          "6:10": "English",
                          "6:55": "Lunch Break",
                          "7:25": "IInd Language"},
            "thursday": {"2:55": "English",
                         "3:40": "IInd Language",
                         "4:30": "Short Break",
                         "4:40": "Social Science",
                         "5:25": "Math",
                         "6:10": "Physics",
                         "6:55": "Lunch Break",
                         "7:25": "Math"},
            "friday":   {"2:55": "IInd Language",
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

    # @commands.Cog.listener()
    @tasks.loop(seconds=60.0)
    async def checktimetable(self):
        curr_date = date.today()
        current_day = str(calendar.day_name[curr_date.weekday()]).lower()

        if current_day in self.timetable.keys():
            day = current_day

        time = datetime.today()
        current_time_parsed = f"{time.hour}:{time.minute}"

        # if current_time_parsed in self.timetable.values():
        try:
            subject = self.timetable[day][current_time_parsed]
            self.subject = subject

        except:
            pass
        if self.subject:
            channel = self.client.get_channel(self.channel_id)
            if channel:
                await channel.send(f"It's **{self.subject}** period! Please join right now! (P.S it might be substitution so don't blast me.)")
                self.subject = None


def setup(client):
    client.add_cog(Timetable(client))
