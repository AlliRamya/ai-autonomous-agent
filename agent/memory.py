class Memory:

    def __init__(self):

        self.history=[]

    def save(self,request,plan):

        self.history.append({

            "request":request,

            "plan":plan

        })

    def get_context(self):

        return self.history


memory=Memory()