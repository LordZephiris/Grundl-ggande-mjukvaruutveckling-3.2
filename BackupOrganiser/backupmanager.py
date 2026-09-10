
class BackupManager:
    """ This class modifies the BACKUPS field of a DataCollection object to add and remove elements. """

    def __init__(self):
        """ Nothing to do here """
        pass

    def add_backup(self, collection_object, backup_name, backup_date, backup_location):
        """ Creates a Backup object and appends it to the COLLECTION_OBJECT.

        COLLECTION OBJECT is expected to be of the type DataCollection.

        Returns the updated COLLECTION_OBJECT. """
        
        backup_obj = {"name": backup_name,
                      "date": backup_date,
                      "location": backup_location}

        collection_object.backups.append(backup_obj)
        return collection_object

    def unbackup(self, collection_object, backup_name, backup_date):
        """ Find all backup items with the given name and date and removes them from COLLECTION_OBJECT 

        Returns the updated COLLECTION_OBJECT. """

        collection_object.backups = [x for x in collection_object.backups if backup_name != x["name"] or backup_date != x["date"]]
        return collection_object
