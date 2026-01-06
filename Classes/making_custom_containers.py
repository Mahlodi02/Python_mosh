# Making Custom Containers

"""Ealier we learnt about common data structures in python,
leart about lists, tuples, sets and dictionaries.
But sometimes we want to create our own custom data structures"""

class TagCloud:

    def __init__(self):
        self.tags = {} # dictionary to store tags and their weights

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1 # we are checking if we have a tag in our dictionary
                                                    # if we don't have we set it's value to 1, otherwise we increment it's value by 1
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0) #  we do this to be able to get the value of tag   

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count # we do this to be able to set the value of tag

    def __len__(self): 
        return len(self.tags) # we do this to be able to get the length of our container

    def __iter__(self):
        return iter(self.tags) # we do this to be able to iterate over our container
                        # iter -> iterator object is an object that walks a container and get one item at a time in for loop


cloud = TagCloud()
cloud["Python"] = 10
print(len(cloud))  # 1
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)  # {'python': 3}