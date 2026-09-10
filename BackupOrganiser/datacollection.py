import json

class DataCollection:
    """ A DataCollection object represents a single backup-worthy collection of data."""

    def __init__(self):
        self.name = ""
        self.description = ""
        self.creation_date = ""
        self.modification_date = ""
        self.still_updated = True
        self.backups = []

    def backup_str(self, entry):
        """ Creates and returns a single string from one backup ENTRY """

        return entry["date"] + " " + entry["name"] + " " + entry["location"]

    def brief_str(self):
        """ Generates and returns a single string (last obj) that briefly describes this DataCollection object. """

        if 0 != len(self.backups):            
            return self.name + " " + self.backup_str(self.backups[-1])
        else:
            return self.name + " -- No backup -- "

    def full_str(self):
        """ Generates and returns an array of strings that fully describes this DataCollection object. """

        out=[self.name, self.description,
             "Created: " + self.creation_date,
             "Modified: " + self.modification_date,
             "Updated:" + str(self.still_updated),
             "Backups:"]

        for b in self.backups:
            out.append("- " + self.backup_str(b))

        return out
        
    def full_json(self):
        """ Returns the attributes of this DataCollection object as a json object """

        return json.dumps(vars(self))
