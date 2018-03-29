import pandas as pd
import markovify
import re
import gensim

# data = ""

def get_data():
    df = pd.read_csv('songdata.csv')
    pattern = re.compile('\n *\n')
    data = {}
    for index, row in df.iterrows():
        artist = row['artist']
        text = '\n'.join([t.strip().lower() for t in pattern.split(row['text'])])
        if artist not in data:
            data[artist] = text + '\n'
        else:
            data[artist] = data[artist] + text
    return data

class ArtistModel:
    def __init__(self, artist, data, state_size=2):
        self.model = markovify.NewlineText(data[artist], state_size=state_size)

    def lyric(self, length=0):
        length = int(length)
        if length > 10000:
            return "Too long length"
        if length == 0:
            return self.model.make_sentence()
        if length > 0:
            return self.model.make_short_sentence(length)

    def finish_lyric(self, start):
        try:
            return self.model.make_sentence_with_start(start.strip().lower(), strict=False)
        except:
            return "Beginning not in corpus"

    def mashup(self, models):
        self.model = markovify.combine([self.model] + [model.model for model in models])


def artists(data):
    artists = list(data.keys())
    artists.sort()
    return artists


def get_mashup(artists, data, length=0):
    models = []
    for artist in artists:
        model = ArtistModel(artist, data)
        models.append(model)
    models[0].mashup(models[1:])
    return models[0].lyric(length)


def get_lyric(artist, data, length=0):
    model = ArtistModel(artist, data)
    return model.lyric(length)

#
# def main():
#     get_data()
#
# if __name__ == '__main__':
#     main()

# data = get_data()
# yeezy = ArtistModel('Kanye West', data)
# linkin = ArtistModel('Linkin Park', data)
# # print linkin.lyric()
# print yeezy.mashup([linkin.model])
# print yeezy.lyric()
# model.finish_lyric('pain')
# model.lyric()
