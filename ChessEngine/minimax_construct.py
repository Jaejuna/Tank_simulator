class MinMaxTree():
    def __init__(self):
        pass

    def create_root_node(self,board):
        root_node = Node(board,None,None)
        self.root_node = root_node
        
    def construct(self,depth = 2):   
        nodes = []
        prev_gen = [self.root_node]
        
        for i in range(depth):
            new_gen = []
            for parent_node in prev_gen:
                parent_node.extend()
                new_gen.extend(parent_node.child_nodes)
            prev_gen = new_gen
            nodes.append(prev_gen)
            
        self.nodes = nodes
        # self.function_list = np.array([[] + [max,min] for _ in range(depth//2)]).flatten()
        
        function_list = []
        if depth % 2 == 0:
            funcs = [max,min]
        else:
            funcs = [min,max]
        for i in range(depth):
            func = funcs[i%2]
            function_list.append(func)
        self.function_list = function_list
        
        return self.root_node
    
    def predict(self,board,side,depth = 3):
        func = np.argmax
        self.create_root_node(board)
        #print('Root Node Created')
        self.construct(depth = depth)
        #print('Tree Constructed')
        self.evaluate(side)
        #print('Evaluation Complete')
        utilities = [node.utility for node in self.nodes[0]]
        effe = func(utilities)
        move = self.nodes[0][func(utilities)].move
        if 'x' in board.san(move):
            effe = 1
        return move,effe