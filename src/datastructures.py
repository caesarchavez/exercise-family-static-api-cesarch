"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        ## You have to implement this method
        ## Append the member to the list of _members
        if 'id' not in member:
            member['id'] = self._generate_id()
            self._members.append(member)
            return member
        else:
            self._members.append(member)
            return member

    def delete_member(self, id):
        ## You have to implement this method
        ## Loop the list and delete the member with the given id
        self._members = [i for i in self._members if i['id'] != id]
        

    def get_member(self, id):
        ## You have to implement this method
        ## Loop all the members and return the one with the given id
        for i in self._members:
            if i['id'] == id: 
                return i

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members