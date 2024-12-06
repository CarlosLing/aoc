
class AOCInput: 
    def __init__(self, path):
        self.path = path
        with open(path, 'r') as f:
            self.raw_data = f.read()
        
    def get_lines(self):
        return self.raw_data.split('\n')
    
    def get_paragraphs(self):
        return self.raw_data.split('\n\n')

    
        
        