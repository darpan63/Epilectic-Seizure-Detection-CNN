import os
import matplotlib.pyplot as plt

'''
for filename in os.listdir("F"):
    with open('F/'+filename) as f:
        lines = f.readlines()
        x = [line.split()[0] for line in lines]
        plt.plot(x)
        plt.savefig('F1/' + filename + '.png')
        plt.close()
'''

for filename in os.listdir("N"):
    with open('N/'+filename) as f:
        lines = f.readlines()
        x = [line.split()[0] for line in lines]
        plt.plot(x)
        plt.savefig('N1/' + filename + '.png')
        plt.close()

for filename in os.listdir("O"):
    with open('O/'+filename) as f:
        lines = f.readlines()
        x = [line.split()[0] for line in lines]
        plt.plot(x)
        plt.savefig('O1/' + filename + '.png')
        plt.close()

for filename in os.listdir("S"):
    with open('S/'+filename) as f:
        lines = f.readlines()
        x = [line.split()[0] for line in lines]
        plt.plot(x)
        plt.savefig('S1/' + filename + '.png')
        plt.close()

for filename in os.listdir("Z"):
    with open('Z/'+filename) as f:
        lines = f.readlines()
        x = [line.split()[0] for line in lines]
        plt.plot(x)
        plt.savefig('Z1/' + filename + '.png')
        plt.close()