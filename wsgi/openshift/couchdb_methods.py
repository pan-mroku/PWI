from couchdb import Server

#wydajna iteracja, na viewsach - warunek, musi byc view w couchdb juz dodany
def get_Doc(docname, view='_all_docs'):
    #https://www.openshift.com/forums/openshift/permission-denied-on-port-8081
    #SERVER = Server('http://194.29.175.241:5984/')
    SERVER = Server('http://szyszko.is-a-chef.net:80/')
    if docname in SERVER:
        doc= SERVER[docname].view(view)
        return doc
    return None

def get_chatData(onlyActive=False):
    chat= get_Doc("chat","utils/list_active")
    docs=[]
    if onlyActive:
        for key in chat:
            if 'value' in key:
                docs.append(key['value'])
    else:
        for key in chat:
            if 'value' in key:
                    if key['value']['active']:
                        docs.append(key['value'])
    return docs
