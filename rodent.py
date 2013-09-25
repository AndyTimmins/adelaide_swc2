# tag ID: A8025
# size (oz)
# sitings per month

# is large(large > 5 0z)
# is small (small < 3 oz)
# capture(month)


class Rodent:
    def __init__(self, tag_id, size ):
        self.tag_id = tag_id
        self.size = size
        self.sightings_per_month = {}
    
    def is_large(self):
        # return True if size is > 5oz
        return (self.size > 5)
    
    def is_small(self):
        # return True if size is < 3oz
        return (self.size < 3)
    
    def plot(self):
        # return the letter of the plot at which
        # this rodent was first captured
        return self.tag_id[0]
        
    

