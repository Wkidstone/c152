import matplotlib.pyplot as plt

data =  [[0,0,0,0,0,0,0,0],
         [0,0,0,0,1,0,0,0],
         [0,0,0,1,1,0,0,0],
         [0,0,0,0,1,0,0,0],
         [0,0,0,0,1,0,0,0],
         [0,0,0,0,1,0,0,0],
         [0,0,1,1,1,1,1,0]
                         ]
plt.imshow(data, cmap= "gray")
plt.show()