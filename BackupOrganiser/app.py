from collectionmanager import CollectionManager
from backupmanager import BackupManager
from restinterface import RESTInterface


def print_info(lines):
    """Prints each line in a list"""
    for line in lines:
        print(line)

def test_overview(cm):
    """Runs test for CollectionManagers overview function"""
    print("---------- Overview")
    for e in cm.overview():
        print(e)

def test_list(cm):
    """Runs test for CollectionManagers detailed_overview function"""
    print("---------- List")
    for e in cm.detailed_overview():
        print_info(e)
        print("---")
    
def test_info(cm):
    """Runs test for CollectionManagers info function"""
    print("---------- Info")
    print_info(cm.info("collection 1"))

def test_search(cm):
    """Runs test for CollectionManagers search function"""
    print("---------- Search for 'collection'")
    for e in cm.search("collection"):
        print(e)

    print("---------- Search for '1'")
    for e in cm.search("1"):
        print(e)

def test_unbackup(cm, bm):
    """Runs test for BackupManagers unbackup function"""
    print("---------- Unbackup")
    print("-- before")
    print_info(cm.info("collection 2"))

    print("-- removing something that does not exist")
    bm.unbackup(cm.get("collection 2"), "disk", "May 2025");
    print_info(cm.info("collection 2"))

    print("-- removing something that exists")
    bm.unbackup(cm.get("collection 2"), "disk", "April 2025");
    print_info(cm.info("collection 2"))

def test_edit(cm):
    """Runs test for CollectionManagers edit function"""
    print("---------- Edit")
    print("-- full edit")
    cm.edit("collection 1", "yesterday", False)
    print_info(cm.info("collection 1"))
    print("-- partial edit")
    cm.edit("collection 1", "today")
    print_info(cm.info("collection 1"))

def test_delete(cm):
    """Runs test for CollectionManagers delete function"""
    print("---------- Delete")
    cm.delete("collection 3")
    for e in cm.overview():
        print(e)

def test_json(cm, bm):
    """Runs tests for CollectionManagers JSON functions"""
    print("---------- JSON tests")
    print("---------- JSON Overview")
    print(cm.overview_json())

    print("---------- JSON Detailed Overview")
    print(cm.detailed_overview_json())

    print("---------- JSON Info")
    print (cm.info_json("collection 1"))

    print("---------- JSON Search")
    print (cm.search_json("collection 1"))
    

def test_collmanager(cm, bm):
    """Adds data for testing"""
    cm.add_collection("collection 1", "first collection", "2024", "2025", True)
    cm.add_collection("collection 2", "second collection", "2024", "2025", True)
    cm.add_collection("collection 3", "third collection", "2024", "2025", True)
    
    bm.add_backup(cm.get("collection 1"), "disk", "April 2025", "on my desk")
    bm.add_backup(cm.get("collection 1"), "disk", "May 2025", "on my desk")
    bm.add_backup(cm.get("collection 2"), "disk", "March 2025", "on my desk")
    bm.add_backup(cm.get("collection 2"), "disk", "April 2025", "on my desk")

    """
    test_overview(cm)
    test_list(cm)
    test_info(cm)
    test_search(cm)
    test_unbackup(cm, bm)
    test_edit(cm)
    test_json(cm, bm)
    test_delete(cm)
    """



def main():
    cm = CollectionManager()
    bm = BackupManager()

    #for testing
    #test_collmanager(cm, bm)

    #for running in docker
    rest = RESTInterface()
    rest.start(cm, bm)

if __name__ == "__main__":
    main()
