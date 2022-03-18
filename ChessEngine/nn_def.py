class NeuralNetwork():
    def __init__(self):
        self.optimizer = 'Adam'
        self.loss = 'categorical_crossentropy'
        
    def define(self):
        input_layer= Input(shape=(8,8,12))
        x = Conv2D(filters=64,kernel_size = 2,strides = (2,2))(input_layer)
        x = Conv2D(filters=128,kernel_size=2,strides = (2,2))(x)
        x = Conv2D(filters=256,kernel_size=2,strides = (2,2))(x)
        x = Flatten()(x)

        x = Dense(4096,activation = 'softmax')(x)
        output = Reshape((1,64,64))(x)

        model = Model(inputs=input_layer,outputs=output)
        model.compile(optimizer = self.optimzier,loss = self.loss)
        self.model = model