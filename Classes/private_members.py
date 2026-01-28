# Private Members

"""On our class TagCloud when we try to access our dictionary directly like this 'print(cloud.tags["PYTHON"])' 
 we get an error messege let fix that by making our tags private by double underscore __tags
 
 The problem with class TagCloud is that it give us access to a dictinary that is used keep track of the
  count of text , so we need to hide the attribute so we don't access it  """

class TagCloud:

    def __init__(self):
        self.__tags = {} # dictionary to store tags and their weights

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1 # we are checking if we have a tag in our dictionary
                                                    # if we don't have we set it's value to 1, otherwise we increment it's value by 1
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0) #  we do this to be able to get the value of tag   

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count # we do this to be able to set the value of tag

    def __len__(self): 
        return len(self.__tags) # we do this to be able to get the length of our container

    def __iter__(self):
        return iter(self.__tags) # we do this to be able to iterate over our container
                        # iter -> iterator object is an object that walks a container and get one item at a time in for loop


cloud = TagCloud()
cloud["Python"] = 10
print(len(cloud))  # 1
cloud.add("Python")
cloud.add("python")
cloud.add("python")
# print(cloud.tags)  # {'python': 3}



# print(cloud.tags["PYTHON"]) # will raise error messege "KeyError"

print(cloud.__dict__) 
print(cloud._TagCloud__tags)

## Making something private is to avoid the accidently access to it.