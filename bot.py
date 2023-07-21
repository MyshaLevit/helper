import nextcord
from nextcord.ext import commands
import datetime
from db import update_message_count, check_message_count
import os

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

async def give_warning(user):
    role = None
    for r in user.roles:
        if r.name in ['•| ⊱🌹⊰ |•Co-Owner', '•| ⊱🔱⊰ |•Support', '•| ⊱🍥⊰ |•Administrator', '•| ⊱🌷⊰ |•Curator', '•| ⊱🌿⊰ |•Main admin', '•| ⊱🍁⊰ |•Senior moder', '•| ⊱💧⊰ |•Moderator', '•| ⊱💗⊰ |•Control']:
            role = r.name
            break
    await user.send(f"@Balonchikkiss#2176, репорт на пользователя {user.name} !\nЮзернейм: {user.name}\nID: {user.id}\nРоль на сервере: {role}\nПричина: не выполнил норму сообщений.")

# Команда для проверки количества сообщений пользователя
@bot.command(name="Профиль")
async def messages(ctx):
    message_count = check_message_count(ctx.author.id)
    role = None
    for r in ctx.author.roles:
        if r.name in ['•| ⊱🌹⊰ |•Co-Owner', '•| ⊱🔱⊰ |•Support', '•| ⊱🍥⊰ |•Administrator', '•| ⊱🌷⊰ |•Curator', '•| ⊱🌿⊰ |•Main admin', '•| ⊱🍁⊰ |•Senior moder', '•| ⊱💧⊰ |•Moderator', '•| ⊱💗⊰ |•Control']:
            role = r.name
            break
    if role is None:
        await ctx.send("Вы не имеете никакой роли на сервере.")
    else:
        if role == '•| ⊱🌹⊰ |•Co-Owner':
            message_goal = 15
        elif role == '•| ⊱🔱⊰ |•Support':
            message_goal = 15
        elif role == '•| ⊱🍥⊰ |•Administrator':
            message_goal = 25
        elif role == '•| ⊱🌷⊰ |•Curator':
            message_goal = 35
        elif role == '•| ⊱🌿⊰ |•Main admin':
            message_goal = 45
        elif role == '•| ⊱🍁⊰ |•Senior moder':
            message_goal = 65
        elif role == '•| ⊱💧⊰ |•Moderator':
            message_goal = 75
        elif role == '•| ⊱💗⊰ |•Control':
            message_goal = 80
        messages_left = message_goal - message_count
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        time_left = datetime.datetime.strptime(tomorrow, '%Y-%m-%d') - datetime.datetime.now()
        time_left_str = str(time_left).split('.')[0]
        await ctx.send(f"Вы отправили {message_count}/{messages_left} сообщений за сегодня.\nВам нужно отправить еще {messages_left} сообщений.\nВаша роль на сервере: {role}.\n Время до обнуления: {time_left_str}.")

@bot.command()
async def чек(ctx, member: nextcord.Member):
    roles = member.roles
    message_goal = 0
    for role in roles:
        if role.name == '•| ⊱🌹⊰ |•Co-Owner':
            message_goal = 15
        elif role.name == '•| ⊱🔱⊰ |•Support':
            message_goal = 15
        elif role.name == '•| ⊱🍥⊰ |•Administrator':
            message_goal = 25
        elif role.name == '•| ⊱🌷⊰ |•Curator':
            message_goal = 35
        elif role.name == '•| ⊱🌿⊰ |•Main admin':
            message_goal = 45
        elif role.name == '•| ⊱🍁⊰ |•Senior moder':
            message_goal = 65
        elif role.name == '•| ⊱💧⊰ |•Moderator':
            message_goal = 75
        elif role.name == '•| ⊱💗⊰ |•Control':
            message_goal = 80
    if message_goal > 0:
        message = f"{member.mention} написал {message_goal} сообщений."
        await ctx.send(message)
    else:
        await ctx.send(f"{member.mention} не имеет нужных ролей.")

""" @bot.command()
async def чек(ctx):
    co_owner_count = 0
    support_count = 0
    administrator_count = 0
    curator_count = 0
    main_admin_count = 0
    senior_moder_count = 0
    moderator_count = 0
    control_count = 0
    for member in ctx.guild.members:
        for role in member.roles:
            if role.name == '•| ⊱🌹⊰ |•Co-Owner':
                co_owner_count += check_message_count(member.id)
            elif role.name == '•| ⊱🔱⊰ |•Support':
                support_count += check_message_count(member.id)
            elif role.name == '•| ⊱🍥⊰ |•Administrator':
                administrator_count += check_message_count(member.id)
            elif role.name == '•| ⊱🌷⊰ |•Curator':
                curator_count += check_message_count(member.id)
            elif role.name == '•| ⊱🌿⊰ |•Main admin':
                main_admin_count += check_message_count(member.id)
            elif role.name == '•| ⊱🍁⊰ |•Senior moder':
                senior_moder_count += check_message_count(member.id)
            elif role.name == '•| ⊱💧⊰ |•Moderator':
                moderator_count += check_message_count(member.id)
            elif role.name == '•| ⊱💗⊰ |•Control':
                control_count += check_message_count(member.id)
    await ctx.send(f"•| ⊱🌹⊰ |•Co-Owner: {co_owner_count}\n•| ⊱🔱⊰ |•Support: {support_count}\n•| ⊱🍥⊰ |•Administrator: {administrator_count}\n•| ⊱🌷⊰ |•Curator: {curator_count}\n•| ⊱🌿⊰ |•Main admin: {main_admin_count}\n•| ⊱🍁⊰ |•Senior moder: {senior_moder_count}\n•| ⊱💧⊰ |•Moderator: {moderator_count}\•| ⊱💗⊰ |•Control: {control_count}") """



# Событие при отправке сообщения
@bot.event
async def on_message(message):
    if not message.author.bot:
        update_message_count(message.author.id, str(message.author))
        message_count = check_message_count(message.author.id)
        role = None
        for r in message.author.roles:
            if r.name in ['•| ⊱🌹⊰ |•Co-Owner', '•| ⊱🔱⊰ |•Support', '•| ⊱🍥⊰ |•Administrator', '•| ⊱🌷⊰ |•Curator', '•| ⊱🌿⊰ |•Main admin', '•| ⊱🍁⊰ |•Senior moder', '•| ⊱💧⊰ |•Moderator', '•| ⊱💗⊰ |•Control']:
                role = r.name
                break
        if role is not None:
            if role == '•| ⊱🌹⊰ |•Co-Owner':
                message_goal = 15
            elif role == '•| ⊱🔱⊰ |•Support':
                message_goal = 15
            elif role == '•| ⊱🍥⊰ |•Administrator':
                message_goal = 25
            elif role == '•| ⊱🌷⊰ |•Curator':
                message_goal = 35
            elif role == '•| ⊱🌿⊰ |•Main admin':
                message_goal = 45
            elif role == '•| ⊱🍁⊰ |•Senior moder':
                message_goal = 65
            elif role == '•| ⊱💧⊰ |•Moderator':
                message_goal = 75
            elif role == '•| ⊱💗⊰ |•Control':
                message_goal = 80
            messages_left = message_goal - message_count
            if messages_left <= 0 and 'Уведомление отправлено' not in [str(x.content) for x in await message.channel.history(limit=10).flatten()]:
                await message.channel.send(f"{message.author.mention}, поздравляю! Вы выполнили свою норму сообщений за сегодня. Ваша роль на сервере: {role}. Уведомление отправлено")
    await bot.process_commands(message)
# Запуск бота

token = os.getenv('TOKEN')
bot.run(token)