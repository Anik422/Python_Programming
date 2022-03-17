class TagCloud:
    def __init__(self):
        self.tags = {}
    def add(self, tag):
        self.tags[tag] = self.tags.get(tag, 0) + 1

cloud = TagCloud()
cloud.add("Python") 
cloud.add("python") 
cloud.add("python") 
print(cloud.tags)