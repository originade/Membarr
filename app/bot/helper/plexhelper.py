from plexapi.myplex import MyPlexAccount
import re


def plexadd(plex, plexname, Plex_LIBS):
    try:
        if len(Plex_LIBS) == 0:
            Plex_LIBS = plex.library.sections()
        plex.myPlexAccount().inviteFriend(user=plexname, server=plex, sections=Plex_LIBS, allowSync=False,
                                          allowCameraUpload=False, allowChannels=False, filterMovies=None,
                                          filterTelevision=None, filterMusic=None)
        print(plexname + ' has been added to plex')
        return True
    except Exception as e:
        print(e)
        return False


def plexremove(plex, plexname):
    try:
        plex.myPlexAccount().removeFriend(user=plexname)
        print(plexname + ' has been removed from plex')
        return True
    except Exception as e:
        print(e)
        return False


def verifyemail(addressToVerify):
    regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
    match = re.match(regex, addressToVerify.lower())
    return match != None
