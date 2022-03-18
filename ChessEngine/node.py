class Node:
    def __init__(self,board,move,parent):
        self.board = board
        self.move = move
        self.parent_node = parent
        self.child_nodes = []
        self.utility = [0,0]
        self.func = None
        
    def evaluate(self,idx):
        if len(self.child_nodes) == 0:
            material = material_counter(self.board)
            white = material[0]
            black = material[1]
            if idx == 0:
                self.utility = black - white
            else:
                self.utility = white - black
        else:
            child_util = [node.utility for node in self.child_nodes]
            self.utility = self.func(child_util)
            
    def extend(self):
        continuations,legal_moves = pos_cont(self.board)
        for i in range(len(continuations)):
            self.child_nodes.append(Node(continuations[i],legal_moves[i],self))