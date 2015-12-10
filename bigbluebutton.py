import settings
import urllib
import hashlib
from uuid import uuid4
from helpers import EndPointRequest

class BBB_API():

    def __init__(self):
        self.secret = settings.BBB_SECRET
        self.api_url = settings.API_URL
        self.query = None
        self.meetingID = None

    def create(self, query_dict):

        if not query_dict:
            raise Exception('You need to set the query values')
        elif 'meetingid' in map(str.lower, query_dict):
            raise Exception("You can't set a custom meetingID")

        self.meetingID = str(uuid4())
        query_dict['meetingID'] = self.meetingID

        query = urllib.urlencode(query_dict)
        
        try:
            query = query + '&checksum=%s' % self._create_checksum(query, 'create')
        except:
            raise

        api_url = self.api_url + 'create?%s' % query

        try:
            create = EndPointRequest(api_url)
            request = create.get_xml()
        except Exception, e:
            raise e
        else:
            return request

    def join(self, query_dict):
        
        query = urllib.urlencode(query_dict)

        try:
            checksum = self._create_checksum(query, 'join')
        except Exception, e:
            raise e
        
        query = '%s&checksum=%s' % (query, checksum)

        api_url = '%sjoin?%s' % (self.api_url, query)

        return api_url

    def end(self):
        pass

    def _create_checksum(self, query, event):
        
        if event in ('create', 'join'):
            checksum = '%s%s%s' % (event, query, self.secret)
            return hashlib.sha1(checksum).hexdigest()
        else:
            raise Exception("No event defined")
