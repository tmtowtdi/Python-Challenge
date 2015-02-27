
import re, requests

class Pyc():
    def __init__( self ):
        self.base_url           = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
        self.current_nothing    = "12345"
        #self.current_nothing    = "66831"  # the payoff argument
        self.set_url()

        self.nothing_pat        = re.compile("and the next nothing is (\d+)")
        self.divide_two_pat     = re.compile("divide by two and", re.I)

    def set_url( self ):
        self.current_url = self.base_url + self.current_nothing

    def get_url( self ):
        resp = requests.get( self.current_url )
        if resp.status_code != 200:
            raise KeyError( "{} returned a status code of {}.".format(url, resp.status_code) )

        ct = resp.headers['content-type']
        if ct != "text/html":
            raise KeyError( "{} had a content-type of {}.".format(url, ct) )
        return resp

    def find_nothing( self, resp:requests.models.Response ):
        print( resp.text )

        m = self.nothing_pat.search( resp.text )
        if m:
            self.current_nothing = m.group(1)
            return

        m = self.divide_two_pat.search( resp.text )
        if m:
            ### self.current_nothing starts as a string.
            ### int from str so division is possible
            ### int from float so we get 2 rather than 2.0
            ### str from int so we can append it to the URL (*sigh*)
            self.current_nothing = str(int(int(self.current_nothing) / 2))
            return

        raise KeyError( "no nothing match was found on", self.current_url )

