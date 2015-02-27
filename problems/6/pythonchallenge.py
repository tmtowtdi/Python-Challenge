
import re, zipfile

class Pyc():
    def __init__( self ):
        self.zipfile = "channel.zip"
        self.zip = zipfile.ZipFile( self.zipfile, 'r')
        self.namedict = {}
        for fn in self.zip.namelist():
            self.namedict[ fn ] = 1
        self.current_nothing = '90052'
        self.set_filename()

        self.comments = []

        self.nothing_pat = re.compile("Next nothing is (\d+)")

    def set_filename( self ):
        self.filename = self.current_nothing + ".txt"

    def read_current_file(self):
        print( "Reading {}.".format(self.filename) )
        contents = self.zip.read( self.filename ).decode("utf-8")

        m = self.nothing_pat.search(contents)
        if m:
            self.current_nothing = m.group(1)
            info = self.zip.getinfo( self.filename )
            self.comments.append( info.comment.decode("utf-8") )
            self.set_filename()
            return

        print( ''.join(self.comments) )
        raise KeyError("That contains string '{}'.".format(contents))

