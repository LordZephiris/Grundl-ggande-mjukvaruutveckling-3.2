from datacollection import DataCollection
import json

class CollectionManager:
    """ Manages a set of data collections.
    This class implements the methods described in the PA1489 assignment description §6.2. """

    def __init__(self):
        """ Initialises a CollectionManager object"""

        self.__collections = []

    def add_collection(self, name, description, creation_date, modification_date, updated):
        """ Create and add a DataCollection to the set of managed collections. 
        Return True if the new collection was added, otherwise False. """
        
        # Create a DataCollection object, and set the name, description, etc. to the ones in the parameters.
        dc = DataCollection()
        dc.name = name
        dc.description = description
        dc.creation_date = creation_date
        dc.modification_date = modification_date
        dc.still_updated = updated

        # Append the new DataCollection object to self.__collections.
        # If successful, the length of this array should change.
        old_len = len(self.__collections)
        self.__collections.append(dc)
        add_ok = len(self.__collections) != old_len

        return add_ok
        

    def overview(self):
        """  Overview of the managed DataCollections
        Return an array of strings, one per DataCollection object. """

        out = []
        for dc in self.__collections:
            out.append(dc.brief_str())

        return out


    def detailed_overview(self):
        """  Detailed overview of the managed DataCollections
        Return an array of arrays of strings, one per DataCollection object. """        

        # Comment: full_str() returns an array of strings, which we put as one element in the array out.
        # We could have smashed all the strings from full_str() together into one single multi-line string,
        # but that would reduce our ability to do good things with it in the next step.
        #
        # In app.py, we solve this by introducing the method "print_info(lines)", which
        # prints out an array of strings, and then make sure to use it in e.g. test_list() where we know
        # we are going to get this array of arrays of strings.

        out = []
        for dc in self.__collections:
            out.append(dc.full_str())

        return out


    def info(self, collection_name):
        """ Detailed overview of a single DataCollection.
        collection_name is the name of the desired data collection.
        Return an array of strings that represent the single data_collection"""

        # Comment: We will probably need to find single collections in many places,
        # so let's introduce and use the method "get" to find a collection based on the name.
        # In this case, we then return the full_str() from the found collection.

        dc = self.get(collection_name)
        if dc is None:
            return []

        return dc.full_str()


    def get(self, collection_name):
        """ Find and return the first data collection that matches collection_name. """

        dcs = [x for x in self.__collections if x.name==collection_name]
        if len(dcs) > 0:
            return dcs[0]

        return None


    def search(self, name):
        """ Find all data collections that matches name. 
        Return an array of brief descriptions for each matching collection. """

        matching_collections = [x for x in self.__collections if name in x.name]
        out = []
        for dc in matching_collections:
            out.append(dc.brief_str())

        return out


    def edit(self, collection_name, modification_date=None, updated=None):
        """ Modify the first data collection that maches collection_name.
        Return the modified data collection.
        
        """
        dc = self.get(collection_name)
        if dc and None != modification_date: dc.modification_date = modification_date
        if dc and None != updated: dc.still_updated = updated        
        return dc

    def delete(self, collection_name):
        """ Delete the first data collection that matches collection_name.
        Return True if a collection was found and deleted, otherwise False. """

        old_len = len(self.__collections)
        self.__collections = [x for x in self.__collections if x.name != collection_name]
        new_len = len(self.__collections)

        return new_len == old_len-1


    def overview_json(self):
        """Return an overview of all collections as JSON."""
        return json.dumps(self.overview())


    def detailed_overview_json(self):
        """Return a detailed overview of all collections as JSON."""
        return json.dumps(self.detailed_overview())


    def info_json(self, collection_name):
        """Return information about one collection as JSON."""
        dc = self.get(collection_name)

        if dc is None:
            return json.dumps(None)

        return dc.full_json()


    def search_json(self, name):
        """Return search results as JSON."""
        return json.dumps(self.search(name))

