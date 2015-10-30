# Hugo Polanco 77818141 and Yang Jiao 82222745. ICS 31 Lab sec 6.  Lab asst 8.
##
## ICStunes:  A Music Manager
##
## Original version ("InfxTunes") in Scheme by Alex Thornton,
##      modified 2007 and 2008 by David G. Kay
## Python version by David G. Kay, 2012

from collections import namedtuple
#######################################
# Album, Song
#######################################

Album = namedtuple('Album', 'id artist title year songs')
# id is a unique ID number; artist and title are strings; year is a number,
#   the year the song was released; songs is a list of Songs

Song = namedtuple('Song', 'track title length play_count')
# track is the track number; title is a string; length is the number of
#   seconds long the song is; play_count is the number of times the user
#   has listened to the song

MUSIC = [
    Album(1, "Peter Gabriel", "Up", 2002,
        [Song(1, "Darkness", 411, 5),
         Song(2, "Growing Up", 453, 5),
         Song(3, "Sky Blue", 397, 2),
         Song(4, "No Way Out", 473, 2),
         Song(5, "I Grieve", 444, 2),
         Song(6, "The Barry Williams Show", 735, 1),
         Song(7, "My Head Sounds Like That", 389, 1),
         Song(8, "More Than This", 362, 1),
         Song(9, "Signal to Noise", 456, 2),
         Song(10, "The Drop", 179, 1)]),
    Album(2, "Simple Minds", "Once Upon a Time", 1985,
        [Song(1, "Once Upon a Time", 345, 9),
         Song(2, "All the Things She Said", 256, 10),
         Song(3, "Ghost Dancing", 285, 7),
         Song(4, "Alive and Kicking", 326, 26),
         Song(5, "Oh Jungleland", 314, 13),
         Song(6, "I Wish You Were Here", 282, 12),
         Song(7, "Sanctify Yourself", 297, 7),
         Song(8, "Come a Long Way", 307, 5)]),
    Album(3, "The Postal Service", "Give Up", 2003,
        [Song(1, "The District Sleeps Alone", 284, 13),
         Song(2, "Such Great Heights", 266, 13),
         Song(3, "Sleeping In", 261, 12),
         Song(4, "Nothing Better", 226, 18),
         Song(5, "Recycled Air", 269, 13),
         Song(6, "Clark Gable", 294, 12),
         Song(7, "We Will Become Silhouettes", 300, 11),
         Song(8, "This Place is a Prison", 234, 9),
         Song(9, "Brand New Colony", 252, 9),
         Song(10, "Natural Anthem", 307, 7)]),
    Album(4, "Midnight Oil", "Blue Sky Mining", 1989,
        [Song(1, "Blue Sky Mine", 258, 12),
         Song(2, "Stars of Warburton", 294, 11),
         Song(3, "Bedlam Bridge", 266, 11),
         Song(4, "Forgotten Years", 266, 8),
         Song(5, "Mountains of Burma", 296, 9),
         Song(6, "King of the Mountain", 231, 8),
         Song(7, "River Runs Red", 322, 9),
         Song(8, "Shakers and Movers", 268, 9),
         Song(9, "One Country", 353, 7),
         Song(10, "Antarctica", 258, 6)]),
    Album(5, "The Rolling Stones", "Let It Bleed", 1969,
        [Song(1, "Gimme Shelter", 272, 3),
         Song(2, "Love In Vain", 259, 2),
         Song(3, "Country Honk", 187, 0),
         Song(4, "Live With Me", 213, 2),
         Song(5, "Let It Bleed", 327, 2),
         Song(6, "Midnight Rambler", 412, 1),
         Song(7, "You Got the Silver", 170, 0),
         Song(8, "Monkey Man", 251, 13),
         Song(9, "You Can't Always Get What You Want", 448, 10)])
]
#######################################
# Sorting the collection
#######################################

# Sort the collection into chronological order
# The 'key=' argument of sort() takes a function---that function
#   takes an album and produces the value that will be used for
#   comparisons in the sort.
# So first we define that function

def Album_year(A: Album) -> int:
    ''' Return the album's year
    '''
    return A.year

# Sort the collection by Album title
def Album_title(A: Album) -> str:
    ''' Return the album's title
    '''
    return A.title

MUSIC.sort(key=Album_title)

# Sort the collection by length (playing time) of album
def Album_length(a: Album) -> int:
    ''' Return the total length of all the songs in the album
    '''
    total_length = 0
    for s in a.songs:
        total_length += int(s.length)
    return total_length

MUSIC.sort(key=Album_length)


# Sort the collection by Album id (as above)
def Album_id(A: Album) -> str:
    ''' Return the album's number
    '''
    return A.id

MUSIC.sort(key=Album_id)

## We can also write a conventional function to sort a collection, so
## we could say collection_sort(MUSIC, Album_length) instead of using
## the method notation MUSIC.sort(key=Album_length).  We do this by
## PASSING A FUNCTION AS A PARAMETER (like the interchangeable
## attachment on a robot arm).

def collection_sort(C: 'list of Album', keyfunction: 'Function on Albums') -> None:
    ''' Sort collection according to specified key function
        Note that this function, like the sort() method, sorts the collection
        IN PLACE (by reference), so it changes the argument it was called with.
        That's why it doesn't RETURN anything.
    '''
    C.sort(key=keyfunction)
    return

collection_sort(MUSIC, Album_title)
assert(MUSIC[0].title == "Blue Sky Mining") # Kind of a half-hearted test
assert(MUSIC[-1].title == "Up")

collection_sort(MUSIC, Album_id) # Just to put it back in the original order


#######################################
# Top 10 most frequently played songs
#######################################

# Collect all the songs out of all the albums.
# To find the MOST frequent, just use the find-largest (king-of-the-hill) algorithm
# To find the top N is hard to code that way.
# Better: Take the list of songs, sort by play_count, take first 10 -- songlist[:10]

def Song_play_count(s: Song) -> int:
    ''' Return the number of times this song has been played
    '''
    return s.play_count

def all_songs(MC: 'list of Album') -> 'list of Song':
    ''' Return a list of all the Songs in a music collection (list of Album)
    '''
    result = [ ]
    for a in MC:
        result.extend(a.songs)
    return result

Songlist = all_songs(MUSIC)
assert(Songlist[0] == Song(1, "Darkness", 411, 5))
assert(Songlist[1] == Song(2, "Growing Up", 453, 5))
assert(Songlist[-1] == Song(9, "You Can't Always Get What You Want", 448, 10))

def top_n_played_songs(MC: 'list of Album', n: int) -> 'list of Song':
    ''' Return a list of the n most frequently played songs in MC
    '''
    Songlist = all_songs(MC)
    Songlist.sort(key=Song_play_count, reverse=True)
    return Songlist[:n]

assert(top_n_played_songs(MUSIC, 5) ==
       [Song(4, "Alive and Kicking", 326, 26),
        Song(4, "Nothing Better", 226, 18),
        Song(5, "Oh Jungleland", 314, 13),
        Song(1, "The District Sleeps Alone", 284, 13),
        Song(2, "Such Great Heights", 266, 13)])


###################################
# Song-displays
###################################
# But these songs don't have their album information!  We removed it when we created
# the list of all songs.  If we want to display selected songs on our iPod screen,
# we'd want to have the album information along with the song information.

# We could flatten out our data structure, storing a copy of the album
# information with each song:
#       1   Up  Peter Gabriel  2002  1  Darkness   411   5
#       1   Up  Peter Gabriel  2002  2  Growing Up   453  8
#       1   Up  Peter Gabriel  2002  3  Sky Blue    397  2
#            ...
# This would work, but there's a lot of duplicate data---it would be wasteful of storage
# and error-prone to store our music data this way permanently.

# Instead, let's just get the album info that goes with a song WHEN WE NEED IT,
# during the computation.  To do this, we define a structure that contains the
# info we need to display a song (on our iPod screen, e.g.)---song details plus
# the info we need from that song's album:

Songdisplay = namedtuple('Songdisplay', 'artist a_title year track s_title length play_count')

# We'll create these structures as we need them during the computation,
# discarding them as we're done; this doesn't affect the main, permanent
# list of albums (like the one we defined as MUSIC above).

def all_Songdisplays(MC: 'list of Album') -> 'list of Songdisplay':
    ''' Return a list of all the songs in the collection MC, in Songdisplay form
    '''
    result = [ ]
    for a in MC:
        result.extend(Album_to_Songdisplays(a))
    return result

def Album_to_Songdisplays(a: Album) -> 'list of Songdisplay':
    ''' Return a list of Songdisplays, one for each song in the album
    '''
    result = [ ]
    for s in a.songs:
        result.append(Songdisplay(a.artist, a.title, a.year,
            s.track, s.title, s.length, s.play_count))
    return result
#print ((all_Songdisplays(MUSIC))[1])
#print ((Album_to_Songdisplays(MUSIC[1]))[1].a_title)
#Once Upon a Time
def play_count_from_songdisplay(sd: Songdisplay) -> int:
    ''' Return the play_count from a Songdisplay
    '''
    return sd.play_count

def top_n_played(MC: 'list of Album', n: int) -> 'list of Songdisplay':
    ''' Return the top n most frequently played songs in MC
    '''
    list_of_Songdisplays = all_Songdisplays(MC)
    list_of_Songdisplays.sort(key=play_count_from_songdisplay, reverse=True)
    return list_of_Songdisplays[:n]

#c
print ('c.1')
def Song_str(s: Song) -> str:
    '''that takes a song and returns a string containing that
    song's information in an easily readable format suitable for printing.
    '''
    return '\t{:2}  {:30}  {:3}  {:2}\n'.format(s.track, s.title, s.length, s.play_count)

def Album_str(a: Album) -> str:
    '''that takes an album and returns a string containing that
    album's information (including the Song_str information for each song on the album) in an easily readable format suitable for printing.
    '''
    albumstr = ''
    songstr = ''
    for song in a.songs:
        songstr += Song_str(song)
    albumstr = '{:2}  {:20}  {:20}  {:4}\n'.format(a.id, a.artist, a.title, a.year)
    return albumstr + songstr

def Songdisplay_str(sd: 'list of Songdisplay') ->str:
    '''that takes a Songdisplay and returns a string containing
    that information in an easily readable form suitable for printing. 
    '''
    songliststr = ''
    for a in sd:

        songliststr += ('{:20}  {:20}  {:4}  {:2}  {:25}  {:3}  {:1}\n'.format(a.artist, a.a_title, a.year, a.track, a.s_title, a.length, a.play_count))
    return songliststr

#Songdisplay string      
print ('Let us test the top 3 play songs!\n' + Songdisplay_str(top_n_played(MUSIC, 3)))



print ('\nc.2')
# Sort the collection by the number of tracks of album
def Album_track(a: Album) -> int:
    ''' Return the total number of tracks of all the songs in the album
    '''
    
    return len(a.songs)

MUSIC.sort(key=Album_track)
# print the resulting collection using Album_str
for a in MUSIC:
    print ('Let us print the result by the total number of tracks!')
    print (Album_str(a))
    
# sort the collection MUSIC by some other key like album title
MUSIC.sort(key=Album_title)

# number-of-tracks sorting task by calling collection_sort and then print
collection_sort(MUSIC, Album_track)
#print ('Let us print the number-of-tracks sorting task by calling collection_sort!') 
#print (MUSIC)



print ('\nc.3')
def unplayed_songs(MC: 'list of albums') -> 'list of Songdisplays':
    '''takes a music collection (a list of albums) and returns a list of Songdisplays that
    one for each song that has never been played
    '''
    result = []
    for a in MC:
        for s in a.songs:
            if s.play_count == 0:
                result.append(Songdisplay(a.artist, a.title, a.year, s.track, s.title, s.length, s.play_count))
##            print('unplayed_songs', s)
    return result
# Print the resulting list using Songdisplay_str
print ('Let us print the unplayed songs using Songdiisplay_str!')
print (Songdisplay_str(unplayed_songs(MUSIC)))



print ('\nc.4')
def length_from_songdisplay(sd:Songdisplay) ->int:
    '''takes a Songdisplay and returns the length of the song
    '''
    return sd.length

        
print ('\nc.5')

# Since the total time the user has spent listening to an album is computed from the play counts and the song lengths, we should calculate the total song length of one album times the play counts. In this way, we compute the the total time.
    
def Album_total_time(a:Album)->int:
    '''takes an alnum and returns the total time per album
    '''
    total_time_listening = 0
    for s in a.songs:
        total_time_listening += int(s.length) * int(s.play_count)
    return total_time_listening
    
def favorite_album(MC: 'list of album') -> 'favorite album':
    '''takes a list of albums and returns the album that is the "favorite."
    '''
    collection_sort(MC, Album_total_time)
    return Album_str(MC[-1])

print ('Let us print the favorite album based on the total time!\n' +favorite_album(MUSIC))


    
print ("\nc.6 \nassert (top_n(MUSIC, 1, play_count_from_songdisplay, True) == [Songdisplay(artist='Simple Minds', a_title='Once Upon a Time', year=1985, track=4, s_title='Alive and Kicking', length=326, play_count=26)] ) ")

def top_n (MC:'list of album', num: int, keyfunction:'Function on Albums', boo:bool) -> 'list of album':
    ''' that takes a list of albums and a number, a function and a Boolean, returns a list of album
    '''
    result = ''
    list_of_Songdisplay = all_Songdisplays(MC)
    list_of_Songdisplay.sort(key = keyfunction, reverse = boo)
    
    result = list_of_Songdisplay[:num]
        
    return result
    
assert (top_n(MUSIC, 1, play_count_from_songdisplay, True) == [Songdisplay(artist='Simple Minds', a_title='Once Upon a Time', year=1985, track=4, s_title='Alive and Kicking', length=326, play_count=26)] )


print ('\nc.7')
def favorite_album2(MC:'list of albums', fmf: 'avorite measurement function')->'list of album':
    '''a list of albums and a "favorite measurement function" comparing those results to determine the favorite
    '''
    collection_sort(MC, fmf)
    return Album_str(MC[-1])

#print (favorite_album2(MUSIC, Album_total_time))

# Write at least one example of a favorite measurement function other than total listening time
def Album_time_per_song(a: Album) -> int:
    ''' Return the album's number
    '''
    result = int (Album_total_time(a) / len(a))
    return result



print ('Let us print the favorite album based on the longest time played per song!\n' + favorite_album2(MUSIC, Album_time_per_song))


print ('\nc.8')
def collection_search(MC: 'list of album', para :str) -> 'list of Songdisplays':
    '''taking a collection and a string as parameters and returning a list of Songdisplays of songs whose title, artist, or album title include that string
    '''
    Songplaylist = all_Songdisplays(MC)
##    print(Songplaylist)
    result = []
    para = para.lower()
##    print(para)
    for a in Songplaylist:
##        print(a.artist.lower(), para, a.artist.lower() == para)
        if para in a.a_title.lower() or para in a.artist.lower() or para in a.s_title.lower():
            
            result.append(a)
        
    return result
print ('Let us find The Postal Service by Postal')
print (Songdisplay_str(collection_search(MUSIC, 'Postal')))




# -------------------------------------------------------
# Add a menu-style user interface
'''
favorite_album2
collection_sort
Album_year
Album_title
Album_length
Album_id
Album_track
Album_total_time
Album_time_per_song


top_n (MC:'list of album',num: int, keyfunction:'Function on Albums', boo:bool)

top_n_played_songs


all_Songdisplays
top_n_played
unplayed_songs
'''
# ------------------------------------------------------------

def collection_sort2(MC:'list of album', key:'keyfuncion') -> str:
    ''' print the sorted list and print the result
    '''
    collection_sort(MC, key)
    
    for a in MC:  
        print (Album_str(a))
    
Menu = """Chooce one
a: sort the collection by the album functions
b: select the favorite album by the album functions
c: select the certain number of songdisplay by the key function
d: show the unplayed songs
s: general search for album title, album artist, song title
q: quit
"""
##MUSIC = []
def Album_tab(a: Album) ->str:
    ''' return a's fields, tab delimited
    '''
    return str(a.id) + '\t' + a.artist + '\t' +  a.title + '\t' +  str(a.year) + '\t\t\t' +  Song_tab(a.songs) + '\n'

def Song_tab(songs: 'list of Songs') -> str:
    #''' return s' s fields, tab delimited
    #'''
    result = ''
    for s in songs:
        result += str(s.track) + '\t' + s.title + '\t' + str(s.length) + '\t' + str(s.play_count) + '\t\t'

    return result

keyfunctionlist = ['year', 'title', 'length', 'id', 'track', 'total time played', 'total time per song']

def command_handle() -> str:
    print ('Welcome to our analyzing song system!')
    MUSIC = []


    filechoice = input('Do you want to start with the existing file?\n>>').lower().strip()
    if filechoice == 'yes':
        infile = open('ICStunes.txt','r')
        for line in infile:
            newSongList = []
            #print (line)
            lineList = line.strip().split('\t\t\t')
            #print (lineList[1])
            #for songs in lineList[1]:
            a_songList = lineList[1].strip().split('\t\t')
            #print (' ====', a_songList)
            for a_song in a_songList:
                
                #print (' **', a_song)
                songdetailList = a_song.strip().split('\t')
                    #print (songdetailList)
                newSongList.append(Song(int(songdetailList[0]),songdetailList[1],int(songdetailList[2]),int(songdetailList[3])))
                    #print (newSongList)
            #print (lineList)
            albumList = lineList[0].strip().split('\t')
            a_Album = Album(int(albumList[0]), albumList[1], albumList[2], int(albumList[3]), newSongList)
            #print (a_Album)
            MUSIC.append(a_Album)


        #print (MUSIC)
        infile.close()

        
    else:
        print ('So you want to create a collection')
    
        
    outfile = open('ICStunes2.txt', 'w')
    #print (MUSIC)
    for al in MUSIC:
        #print (Album_str(al))
        outfile.write(Album_str(al))
    
    outfile.close()


    
    while True:
        print (Menu)
        choice1 = input ('what is your choice?\n>>').strip()
        if choice1.lower() == 'a':
            key1 = input ('what is the key function?\nChoice available: title, length, id, track, total time played, total time per song.\n>>')
            keyindex = keyfunctionlist.index(key1.lower())
            if keyindex == 0:
                (collection_sort2(MUSIC, Album_year))
                
            elif keyindex == 1:
                (collection_sort2(MUSIC, Album_title))
                
            elif keyindex == 2:
                (collection_sort2(MUSIC, Album_length))
                
            elif keyindex == 3:
                (collection_sort2(MUSIC, Album_id))
                
            elif keyindex == 4:
                (collection_sort2(MUSIC, Album_track))
                
            elif keyindex == 5:
                (collection_sort2(MUSIC, Album_total_time))
                
            elif keyindex == 6:
                (collection_sort2(MUSIC, Album_time_per_song))
                
            
        elif choice1.lower() == 'b':
            key2 = input ('what is the key function?\nChoice available: title, length, id, track, total time played, total time per song.\n>>')
            keyindex = keyfunctionlist.index(key2.lower())
            if keyindex == 0:
                print (favorite_album2(MUSIC, Album_year))
                
            elif keyindex == 1:
                print (favorite_album2(MUSIC, Album_title))
                
            elif keyindex == 2:
                print (favorite_album2(MUSIC, Album_length))
                
            elif keyindex == 3:
                print (favorite_album2(MUSIC, Album_id))
                
            elif keyindex == 4:
                print (favorite_album2(MUSIC, Album_track))
                
            elif keyindex == 5:
                print (favorite_album2(MUSIC, Album_total_time))
                
            elif keyindex == 6:
                print (favorite_album2(MUSIC, Album_time_per_song))
                
        elif choice1.lower() == 'c':
            key3 = input ('what is the key function?\nChoice available: length, play count.\n>>')
            num = eval (input ('How many albums do you want to see?\n>>'))
            reverse = bool(input ('Do you want to reverse the selection? Please input True if you don\'t want to reverse; False if you want to reverse.\n>>').capitalize())

            if key3.lower() == 'length':
                print (Songdisplay_str(top_n(MUSIC, num, length_from_songdisplay, reverse)))
            elif key3.lower() == 'play count':
                print (Songdisplay_str(top_n(MUSIC, num, play_count_from_songdisplay, reverse)))
            else:
                print ('the choice', key3, 'is not valid. Please try again!')
                

        elif choice1.lower() == 'd':
            #print(MUSIC)
            print (Songdisplay_str(unplayed_songs(MUSIC)))

        elif choice1.lower() == 's':
            para = input('Please input the keyword of in album artist, album title, or song title that you want to search.\n>>')
##            print (para)
##            print (type(para))
            result = (Songdisplay_str(collection_search(MUSIC, para)))
            if result == '':
                print ('Nothing was found.')
            else:
                print(result)
        elif choice1.lower() == 'q':
            print ('Thank you. Bye')
            break
            
        else:
            print('Sorry the choice is invalid, please select choice again\n>>')

        
command_handle()       
    
    
    