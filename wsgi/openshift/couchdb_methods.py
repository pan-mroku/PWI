from couchdb import Server

#wydajna iteracja, na viewsach - warunek, musi byc view w couchdb juz dodany
def get_Doc(docname, view='_all_docs'):
    SERVER = Server('http://194.29.175.241:5984/')
    if docname in SERVER:
        doc= SERVER[docname].view(view)
        return doc
    return None
