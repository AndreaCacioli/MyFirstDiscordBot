import discord
from functions import sendSuggestion
import os
from keep_alive import keep_alive



class MyClient(discord.Client):

    channelNumber = 1
    channels_to_be_cancelled = []

    async def on_ready(self):
        print('Logged on as {0}!\n'.format(self.user))
        return

    async def on_message(self, message):
        if message.author == client.user:
            return
        query = message.content
        query = query.lower() 
        if query.startswith('!anime') or query.startswith('!manga'):
            await sendSuggestion(query, message)
        


    async def on_voice_state_update(self, member, before, after):
        print(str(member) + " from guild " + str(member.guild) + ' just moved!')
        #Cancello vecchie stanze
        if(before.channel != None and len(before.channel.members) == 0 and before.channel in self.channels_to_be_cancelled and before != after):
            self.channels_to_be_cancelled.remove(before.channel)
            await before.channel.delete()

        #Stanza Temporanea
        if member.voice != None:
            if member.voice.channel.name == 'Crea Stanza Temporanea':
                #controllo tutti i nomi
                names = []
                for channel in member.guild.channels:
                    names = names + [channel.name]
                print(names)
                roomName = 'Room' + str(self.channelNumber)
                if roomName not in names:
                    #Creo il canale
                    channel = await member.guild.create_voice_channel(roomName, type = discord.ChannelType.private)
                    print("New channel created:" + str(channel))
                    #Sposto nel nuovo canale
                    print('Moving to new room')
                    await member.move_to(channel)
                    self.channels_to_be_cancelled = self.channels_to_be_cancelled + [channel]
                    #Permessi
                    await channel.set_permissions(member, connect = True, speak = True, move_members = True, manage_roles = True, manage_channels = True, view_channel = True, mute_members = True, deafen_members = True)
                else:
                    await member.move_to(None) #Basically kick the user
                self.channelNumber = self.channelNumber + 1

                



client = MyClient()
keep_alive()
client.run(os.environ['TOKEN'])