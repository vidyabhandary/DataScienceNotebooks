class Collectionitem:
    collection_item_count = 0
    
    def __init__(self, colldict):
        self.colldict = colldict
        Collectionitem.collection_item_count += 1
        
    # method to get the birth year of the first creator for each collection item
    def birthyearcreator1(self):
        if ('birth_year' in self.colldict['creators'][0]):
            byear = self.colldict['creators'][0]['birth_year']
        else:
            byear = 'Unknown'
        return byear
    
    # method to get the birth years for all creators
    def birthyearsall(self):
        byearlist = [item.get('birth_year') for item in self.colldict['creators']]
        return byearlist
    
    # method to count the number of creators
    def ncreators(self):
        return len(self.colldict['creators'])
    
    # method to count the number of media citations
    def ncitations(self):
        return len(self.colldict['citations'])    
    