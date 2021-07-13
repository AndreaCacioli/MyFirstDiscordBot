from mal import AnimeSearch
from mal import MangaSearch

def getScore(e):
    if e.score == None:
        return 0
    return float(e.score)

async def sendSuggestion(query, message):
        if query.startswith('!anime'):
            try:
                category = query.split(' ')[1]
            except:
                await message.channel.send('Be sure to use the right syntax: !anime [category]')
                return   
            answer = 'My anime suggestions for the category ' + str(category) + ' would be:\n'
            search = AnimeSearch(category)
            search.results.sort(reverse = True, key = getScore)
            for i in range(5):
                answer = answer + '\t\t*  ' + str(search.results[i].title) + '\t\t Score: ' + str(search.results[i].score) + '\n'
            await message.channel.send(answer)

        if query.startswith('!manga'):
            try:
                category = query.split(' ')[1]
            except:
                await message.channel.send('Be sure to use the right syntax: !manga [category]')
                return   
            answer = 'My manga suggestions for the category ' + str(category) + ' would be:\n'
            search = MangaSearch(category)
            search.results.sort(reverse = True, key = getScore)
            for i in range(5):
                answer = answer + '\t\t*  ' + str(search.results[i].title) + '\t\t Score: ' + str(search.results[i].score) + '\n'
            await message.channel.send(answer)