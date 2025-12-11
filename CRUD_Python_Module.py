from pymongo import MongoClient

class AnimalShelter(object):
    """CRUD operations for the AAC database."""

    def __init__(self, username='aacuser', password='snhu1234',
                 host='localhost', port=27017, db='aac', col='animals'):
        # Connect without authentication (Codio uses no-auth MongoDB)
        self.client = MongoClient(f"mongodb://{host}:{port}")
        self.database = self.client[db]
        self.collection = self.database[col]

    # CREATE
    def create(self, data):
        """Insert a document. Return True if successful."""
        if data:
            try:
                result = self.collection.insert_one(data)
                return bool(result.inserted_id)
            except Exception as e:
                print("Create error:", e)
                return False
        return False

    # READ
    def read(self, query=None):
        """Return list of documents matching query."""
        try:
            if query is None:
                query = {}
            return list(self.collection.find(query))
        except Exception as e:
            print("Read error:", e)
            return []

    # UPDATE
    def update(self, query, new_values):
        """Update docs matching query. Return number modified."""
        if query and new_values:
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except Exception as e:
                print("Update error:", e)
                return 0
        return 0

    # DELETE
    def delete(self, query):
        """Delete docs matching query. Return number removed."""
        if query:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Delete error:", e)
                return 0
        return 0
