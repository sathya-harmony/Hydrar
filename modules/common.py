from pymongo import MongoClient

import re

from typing import (Callable, Coroutine, List, NewType, Optional, Type,
                    TypeVar, Union)

import discord


from discord.embeds import EmbedProxy

from discord.ext import commands
from discord.ext.commands.errors import CommandError


cluster = MongoClient(
    "mongodb+srv://Hydra:CihVirus123@economy.2xn9e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")


OWNER_PERMS = [611210739830620165]
TESTERS = []

LOG_CHANNEL_ID = 896428684158844928
PRIVATE_CMDS = []


async def has_owner_perms(ctx, msg=None):  # Owner Permissions
    if ctx.author.id in OWNER_PERMS:
        if msg is not None:
            await ctx.send(msg)
        return True
    await ctx.send("Only <@907602358756847646> owner(s) can use this command.")
    return False


def check_owner_perms(ctx):  # Check Owner Permissions
    return ctx.author.id in OWNER_PERMS


async def has_tester_perms(ctx, msg=None):
    if ctx.author.id in OWNER_PERMS or ctx.author.id in TESTERS:
        if msg is not None:
            await ctx.send(msg)
        return True
    await ctx.send("Only <@907602358756847646> owner(s) or tester(s) can use this command.")
    return False


def check_tester_perms(ctx):
    return ctx.author.id in OWNER_PERMS or ctx.author.id in TESTERS


"""================================================================================================"""


class NotAGuildError(CommandError):
    pass


def owner_or_perm(**perms):

    original = commands.has_guild_permissions(**perms).predicate

    async def extended_check(ctx):
        if ctx.guild is None:
            return False
        is_bot_owner = check_owner_perms(ctx)

        return (ctx.guild.owner_id == ctx.author.id or is_bot_owner) or await original(ctx)
    return commands.check(extended_check)


def guild_only():

    async def extended_check(ctx):
        if ctx.guild is None:
            raise NotAGuildError

        return True

    return commands.check(extended_check)


"""================================================================================================"""
"""================================================================================================"""

str_URL = NewType('str_URL', str)
CustomE = TypeVar('CustomE', bound='CustomEmbed')

'''def pour_fields(index:int, field_sizes:list, max_size:int):
    if sum(field_sizes[index]) > max_size:
        field_sizes.insert(index+1, [])
        while sum(field_sizes[index])>max_size:
            field_sizes[index+1].insert(0,
                field_sizes[index].pop())
    return field_sizes'''


class CustomEmbed(discord.Embed):
    @property
    def fields_len(self) -> int:
        total = 0
        for field in getattr(self, '_fields', []):
            total += len(field['name']) + len(field['value'])

        return total

    @property
    def space(self) -> int:
        return 6000 - len(self)

    @classmethod
    def from_embed(cls, embed: discord.Embed):
        return cls.from_dict(embed.to_dict())

    @classmethod
    def embed_dict_len(cls, embed: dict):
        total = len(embed.get('title', '')) \
            + \
            len(embed.get('description', ''))

        for field in embed.get('fields', []):
            total += len(field['name']) + len(field['value'])

        total += len(embed
                     .get('footer', {})
                     .get('text', ''))

        total += len(embed
                     .get('author', {})
                     .get('name', ''))

        return total

    """
    # EMBED DOESN'T SEND THO :((
    def handle_fields_overflow(self, middle_embed=None, last_embed=None) -> list[CustomE]:
        '''
        !!! LATE REALISATION !!! THIS EMBED LIST DOES NOT GET SENT ANYWAYS, IF TOTAL SUM OF ALL THE EMBEDS' SIZE IS MORE THAN 6000. SO NO MATTER HOW TO ORGANIZE THE 6000+ SIZED EMBED, YOU CANNOT SEND IT!!! :(((
        Takes in the middle and last embed formats.
        Returns a list of embed(s) where all the embeds' size is below 6000.
        This was designed to spread out the fields (in same order), to reduce individual embed sizes, so the handling of other embed components may not work here, and may be bugged.
        '''
        # If the current embed has not crossed the limit, then just return it's copy in a list.
        if len(self) <= 6000:
            return [self.copy()]
        fields = self._fields
        # If no middle_embed is given, make a new embed with the same color as the primary embed's.
        if middle_embed is None:
            middle_embed = self.__class__(color=self.color)
        # If no last_embed is given, make a new embed with the same color and footer as the primary embed's.
        if last_embed is None:
            last_embed = self.__class__(color=self.color)
            last_embed.set_footer(**self._footer)
        # Make primary embed dictionary, size and empty_space variables, then remove it's footer.
        primary_embed = self.to_dict()
        if 'fields' in primary_embed:
            primary_embed.pop('fields')
        primary_embed_size = self.__class__.embed_dict_len(primary_embed)
        primary_embed_space = 6000 - primary_embed_size
        if 'footer' in primary_embed:
            primary_embed.pop('footer')
        # Make middle embed size, empty_space, and dictionary variables.
        middle_embed_size = len(middle_embed)
        middle_embed_space = 6000 - middle_embed_size
        middle_embed = middle_embed.to_dict()
        # Make last embed size, empty_space, and dictionary variables.
        last_embed_size = len(last_embed)
        last_embed_space = 6000 - last_embed_size
        last_embed = last_embed.to_dict()
        # Make an embeds list to store the final embeds in.
        embeds = []
        # Declare a 2d field_sizes list.
        field_sizes = [[]]
        # Fill the field sizes, in the above 2d list. Pattern of how it at the end: [[124,32,1112]]
        for field in fields:
            field_sizes[0].append(len(field['name']) + len(field['value']))
        # Now put the fields list in another fields list.
        fields = [fields]
        # While there is: only one item in field sizes and its sum is greater than the primary embed empty space,
        #                OR
        #                there is more than one item in field sizes, and the last item has its sizes summed up to more than that of the empty space in last embed empty space, ...
        while (len(field_sizes) == 1 and sum(field_sizes[0]) > primary_embed_space)\
                or (len(field_sizes) > 1 and sum(field_sizes[-1]) > last_embed_space):
            # Select which embed's empty space to check in this iteration.
            space = primary_embed_space \
                if len(field_sizes) == 1 \
                else last_embed_space
            # Add a new list to field sizes, make new pointers to the last two items in the field sizes list, ie, the current_group, and the next_group (the empty list which we just appended).
            field_sizes.append([])
            current_group = field_sizes[-2]
            next_group = field_sizes[-1]
            # While the total sum of the current group remains more than the empty space selected, just move the last item of the current group to the first index (index 0) of the next group.
            while sum(current_group) > space:
                next_group.insert(0, current_group.pop())
            # If the space selected was the last embed's empty space, ...
            if space == last_embed_space:
                # If the sum of the current group's sizes added to the first size in the next group, is not more than the empty space of the middle embed format, ...
                if sum(current_group) + next_group[0] <= middle_embed_space:
                    # and while there is something in the next group, and the sum is still not more than the empty space of the middfle embed format, then set the next group's first item as current group's last item.
                    while len(next_group) > 0 \
                            and sum(current_group) + next_group[0] <= middle_embed_space:
                        current_group.append(next_group.pop(0))
                # If, by chance, even after all this, the next group is empty, and the total sum of the sizes in the current group is more than the empty space in the last embed, then set the current group's last item as the next group's first item.
                if len(next_group) == 0 \
                        and sum(current_group) > last_embed_space:
                    next_group.insert(0, current_group.pop())
            # Push all the extra fields in the current last FIELD LIST, to a another list which now becomes the last field list.
            fields.append(fields[-1]
                          [len(current_group):])
            # Truncate the previous fields list.
            fields[-2] = fields[-2][:len(current_group)]
            # Select which embed format to use.
            embed = primary_embed \
                if len(fields) == 2 \
                else middle_embed
            # Make a new embed with the appropriate fields list, and add it to the embeds list.
            embeds.append(
                custom_embed(
                    embed=self.__class__.from_dict(embed),
                    fields=fields[len(embeds)]))
        # Lastly (but not the least), add the last embed with the last fields list to the embeds list.
        embeds.append(
            custom_embed(
                embed=self.__class__.from_dict(last_embed),
                fields=fields[len(embeds)]))
        # FINALLY! Return the embeds list :) 😅
        return embeds
    """


def set_multiple_dict_defaults(_dict, **kwargs):
    for key, value in kwargs.items():
        _dict.setdefault(key, value)


def custom_embed(*,
                 embed=None,
                 color=0x00ffff,
                 description="", desc="",
                 title="",
                 _type="rich",
                 url="",
                 timestamp=discord.Embed.Empty,
                 time=discord.Embed.Empty,
                 fields=None,
                 footer=None,
                 img: str_URL = None,
                 thumbnail: str_URL = None,
                 author=None,
                 EmbedClass: Type[discord.Embed] = discord.Embed):

    # Fixing the pointer problem
    if fields is None:
        fields = []

    if isinstance(footer, EmbedProxy):
        footer = footer.__dict__

    if isinstance(embed, dict):
        # Making the embed_dict
        set_multiple_dict_defaults(embed,
                                   color=color,
                                   description=description or desc,
                                   title=title,
                                   type=_type,
                                   url=url,
                                   timestamp=timestamp or time)

        if 'fields' not in embed:
            embed['fields'] = list()

        for i in range(len(fields)):
            if "inline" not in fields[i]:
                fields[i]["inline"] = False

            embed['fields'].append({'name': fields[i]["name"],
                                    'value': fields[i]["value"],
                                    'inline': fields[i]["inline"]})

        if not footer is None:
            if isinstance(footer, dict):
                if "text" not in footer:
                    footer["text"] = EmbedClass.Empty
                if "icon_url" not in footer:
                    footer["icon_url"] = EmbedClass.Empty
            else:
                footer = {'text': str(footer),
                          'icon_url': EmbedClass.Empty}

            embed['footer'] = footer

        if img is not None:
            embed['image'] = {'url': img}

        if thumbnail is not None:
            embed['thumbnail'] = {'url': thumbnail}

        if author is not None:
            if isinstance(author, dict) \
                    and "name" in author \
                        and not (author["name"] == ""
                                 or author["name"].isspace()):
                embed['author'] = author
            else:
                embed['author'] = {'name': str(author)}

    else:
        # Making the embed
        if embed is None:
            embed = EmbedClass(color=color,
                               description=description or desc,
                               title=title,
                               type=_type,
                               url=url,
                               timestamp=timestamp or time)

        for i in range(len(fields)):
            if "inline" not in fields[i]:
                fields[i]["inline"] = False

            embed.add_field(name=fields[i]["name"],
                            value=fields[i]["value"],
                            inline=fields[i]["inline"])

        if not footer is None:
            if isinstance(footer, dict):
                if "text" not in footer:
                    footer["text"] = EmbedClass.Empty
                if "icon_url" not in footer:
                    footer["icon_url"] = EmbedClass.Empty
            else:
                footer = {'text': str(footer),
                          'icon_url': EmbedClass.Empty}

            embed.set_footer(text=footer["text"], icon_url=footer["icon_url"])

        if img is not None:
            embed.set_image(url=img)

        if thumbnail is not None:
            embed.set_thumbnail(url=thumbnail)

        if author is not None:
            if isinstance(author, dict) \
                and "name" in author \
                and not (author["name"] == ""
                         or author["name"].isspace()):
                embed.set_author(**author)
            else:
                embed.set_author(name=str(author))

    return embed


'''
def get_fields_size(embed):
    fields = list()
    if isinstance(embed, discord.Embed):
        for field in embed.fields:
            fields.append(field.name)
            fields.append(field.value)
    elif isinstance(embed, dict):
        if 'fields' in embed:
            for field in embed["fields"]:
                fields.append(field["name"])
                fields.append(field["value"])
    fields_length = 0
    for item in fields:
        fields_length += len(str(item))\
            if item is not discord.Embed.Empty\
            else 0
    return fields_length
def handle_fields_size(embed):
    if isinstance(embed, dict):
        embed = discord.Embed.from_dict(embed)
    embeds = [embed]
    if len(embeds[0]) > 5700:
        embeds.insert(1, custom_embed(color=embeds[0].color,
                                      footer={'text': embeds[0].footer.text,
                                              'icon_url': embeds[0].footer.icon_url}))
        embeds[0].remove_footer()
        while len(embeds[0]) > 5700:
            embeds[1].insert_field_at(
                0,
                name=embeds[0].fields[-1].name,
                value=embeds[0].fields[-1].value,
                inline=embeds[0].fields[-1].inline,)
            embeds[0].remove_field(-1)
            if len(embeds[1]) > 5700:
                embeds.insert(1, custom_embed(embed={},
                                              color=embeds[0].color,
                                              fields=[embeds[1].fields[0]]))
                embeds[1].remove_field(0)
    print([len(embed)for embed in embeds])
    return embeds
'''

"""================================================================================================"""
"""================================================================================================"""


# Set the time unit values in seconds.
TIME_UNIT_VALUES = {}
TIME_UNIT_VALUES['s'] = 1
TIME_UNIT_VALUES['m'] = 60*TIME_UNIT_VALUES['s']
TIME_UNIT_VALUES['h'] = 60*TIME_UNIT_VALUES['m']
TIME_UNIT_VALUES['d'] = 24*TIME_UNIT_VALUES['h']
TIME_UNIT_VALUES['w'] = 7*TIME_UNIT_VALUES['d']

# Make a string containing the required time units.
TIME_UNITS = 'smhdw'

# Make a dict for time_units in actual words
TIME_UNIT_NAMES = {'s': 'second',
                   'm': 'minute',
                   'h': 'hour',
                   'd': 'day',
                   'w': 'week'}

# Set the time unit caps.
TIME_UNIT_CAPS = {}
# Iterate from first to last but one time_unit.
for i, unit in enumerate(TIME_UNITS[:-1]):
    # To get the cap, divide the seconds of the next unit value with the current unit value.
    TIME_UNIT_CAPS[unit] = int(
        TIME_UNIT_VALUES[TIME_UNITS[i+1]] / TIME_UNIT_VALUES[unit])

# Pre-Define the time patterns.
TIME_PATTERNS = {}
# Iterate though the time_units.
for unit in TIME_UNITS:
    # A group of digits, followed by first letter of the unit.
    # A group of digits: `(\d+)`, and zero or more white spaces: `\s*`.
    TIME_PATTERNS[unit] = re.compile(r'(\d+)\s*' + unit)


def time_parser(time_str):
    # print(parser.parse(time_str))
    # print(pd.to_datetime(time_str))
    # print(parse(time_str))

    # Make a dictionary with time units as the keys and 0 as the value.
    parsed_time = dict.fromkeys(TIME_UNITS, 0)

    # Initiate the time in seconds variable.
    time_in_secs = 0

    # If the str is in a format with separated colons like: '12:00:00', then...
    if ':' in time_str:
        # Make a list, separating the time_str on colons, then reverse it.
        # We need to reverse in order to go from the smallest unit to the largest.
        split_time_str = reversed(time_str.split(':'))

        # Set the index to 0.
        i = 0
        # Iterate through the values in the separated list.
        for value in split_time_str:
            # If the value stripped of spaces, newlines, tabs, etc, is a numeric string, then...
            if value.strip().isnumeric():
                # Get the time unit at the current index, and set its parsed_time to the value (after converting the value to int).
                parsed_time[TIME_UNITS[i]] = int(value)
                # Increase the index by one.
                i += 1

                if len(TIME_UNITS) <= i:
                    break

    # If the str is not in a format with separated colons like: 12:00:00, then...
    else:
        # Iterate through the items (time unit, and pattern) in time_patterns.
        for unit, pattern in TIME_PATTERNS.items():
            # Search for the pattern in the time string, and store it in a `result` variable.
            result = re.search(pattern, time_str)

            # If the result is not None, ie, if a match is found,
            if result is not None:
                # Set the parsed_time at the current unit to the first group in the match after converting it to the int.
                # If you don't recall, the first group for this is the `(\d+)`.
                parsed_time[unit] = int(result.group(1))

    # Iterate from first to last but one time_unit, taking the index, and the time unit in every iteration.
    for i, unit in enumerate(TIME_UNITS[:-1]):
        # If the parsed_time at the current unit is more than or equal to the cap of this unit, then...
        if parsed_time[unit] >= TIME_UNIT_CAPS[unit]:

            # Add the quotient (floor division to be precise)
            #    of the parsed_time at the current unit,
            #    divided by the cap of the unit,
            #    to the parsed time of the next unit,
            parsed_time[TIME_UNITS[i+1]] += \
                parsed_time[unit] // TIME_UNIT_CAPS[unit]

            # and set the parsed_time at the current unit to the remainder (mod to be precise).
            parsed_time[unit] %= TIME_UNIT_CAPS[unit]

        # Take the parsed_time at the current unit and multiply with the value of the unit (in seconds) to get the value of the parsed_time at the unit in seconds, and then add it to the total `time_in_secs` variable.
        time_in_secs += parsed_time[unit] * TIME_UNIT_VALUES[unit]

    # As we iterated only till the second-last unit, we'll handle adding the seconds of the last unit outside the loop.
    time_in_secs += parsed_time[TIME_UNITS[-1]] * \
        TIME_UNIT_VALUES[TIME_UNITS[-1]]

    # Return the parsed_time and the time_in_secs respectively, as a tuple.
    return parsed_time, time_in_secs


def time_to_string(time_in_secs):
    parsed_time = dict.fromkeys(TIME_UNITS, 0)
    in_words, in_ratio = [], []

    for unit in reversed(TIME_UNITS):
        if time_in_secs >= TIME_UNIT_VALUES[unit]:

            parsed_time[unit] = time_in_secs // TIME_UNIT_VALUES[unit]

            time_in_secs %= TIME_UNIT_VALUES[unit]

        if parsed_time[unit] != 0:
            in_words.append(
                f"{parsed_time[unit]} {TIME_UNIT_NAMES[unit].title()}{'' if parsed_time[unit] == 1 else 's'}")
            in_ratio.append(f"{parsed_time[unit]:2}".replace(' ', '0'))

        elif not in_ratio == []:
            in_ratio.append(f"{parsed_time[unit]:2}".replace(' ', '0'))

    return in_words, in_ratio


"""================================================================================================"""
