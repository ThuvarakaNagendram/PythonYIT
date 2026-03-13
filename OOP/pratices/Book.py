class Book:
    
    def __init__(self,title,author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages
        
    def display(self):
        print(self.title)
        print(self.author)
        print(self.num_pages)
        
book1=Book("A","Author1",597)
book1.display()