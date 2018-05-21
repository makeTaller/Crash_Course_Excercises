def make_Album(a_name,a_title,tracks='0'):
    """ Dictionary for artist and ablum"""
    if int(tracks) >0:
        collection = {'artist':a_name, 'title':a_title,'tracks':tracks}
    else:
        collection = {'artist':a_name, 'title':a_title}
    return collection

art_name = input("Enter the Artist: ")
art_title = input("Enter the title: ")
art_tracks = input("Enter the amount of tracks: ")


artist = make_Album(art_name,art_title,art_tracks)
print(artist)
