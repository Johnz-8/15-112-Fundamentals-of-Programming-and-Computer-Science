from cmu_cpcs_utils import testFunction

class Song:
    def __init__(self, title, time):
        self.title=title
        self.time=time
        self.minutes=int(self.time.split(':')[0])
        self.seconds=int(self.time.split(':')[1])

    def getSeconds(self):
        return self.minutes*60+self.seconds        

class Album:
    def __init__(self, title, musician, genre, songs):
        self.title=title
        self.musician=musician
        self.genre=genre
        self.songs=songs
    
    def getTotalSeconds(self):
        total=0
        for song in self.songs:
            total+=song.getSeconds()
        return total
    
    def getPlayTime(self):
        totalSeconds=self.getTotalSeconds()
        minutes=str(totalSeconds//60)
        seconds=str(totalSeconds%60)
        if len(seconds)==1:
            seconds='0'+seconds
        return minutes+':'+seconds

@testFunction
def testSongAndAlbumClasses():
    song1 = Song('Peaceful', '18:16') # 18 minutes and 16 seconds
    assert(song1.title == 'Peaceful')
    assert(song1.getSeconds() == 1096) # 18*60 + 16 = 1096

    song2 = Song('In a Silent Way', '19:52') # 19 minutes and 52 seconds
    assert(song2.title == 'In a Silent Way')
    assert(song2.getSeconds() == 1192) # 19*60 + 52 = 1192

    album1 = Album('In a Silent Way', 'Miles Davis', 'Jazz', [song1, song2])
    assert(album1.title == 'In a Silent Way')
    assert(album1.musician == 'Miles Davis')
    assert(album1.genre == 'Jazz')
    assert(album1.songs == [song1, song2])
    assert(album1.getTotalSeconds() == 2288) # 1096 + 1192 = 2288
    assert(album1.getPlayTime() == '38:08')  # 32 minutes and 8 seconds

    song3 = Song('Happening', '3:44') # 3 minutes and 44 seconds
    assert(song3.title == 'Happening')
    assert(song3.getSeconds() == 224) # 3*60 + 44 = 224

    album2 = Album('Happening', 'AKMU', 'Folk', [song3])
    assert(album2.title == 'Happening')
    assert(album2.musician == 'AKMU')
    assert(album2.genre == 'Folk')
    assert(album2.songs == [song3])
    # since there's only one song, duration of album == duration of song
    assert(album2.getTotalSeconds() == 224) 
    assert(album2.getPlayTime() == '3:44') # 3 minutes and 44 seconds

    song4 = Song('Lado B', '2:39')
    song5 = Song('Telegrama', '4:15')
    song6 = Song('Pieles', '2:20')
    song7 = Song('La Oscuridad', '3:36')
    song8 = Song('Miedo, Amor y Vida', '2:44')
    album3 = Album('Mieldo, Amor y Vida', 'Ati Lane', 'Folk', [song4, song5, song6, song7, song8])
    assert(album3.title == 'Mieldo, Amor y Vida')
    assert(album3.musician == 'Ati Lane')
    assert(album3.genre == 'Folk')
    assert(album3.songs == [song4, song5, song6, song7, song8])
    assert(album3.getTotalSeconds() == 934)
    assert(album3.getPlayTime() == '15:34') # 15 minutes and 34 seconds

def main():
    testSongAndAlbumClasses()

main()
