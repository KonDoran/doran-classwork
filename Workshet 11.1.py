import pdb
print("Please enter the height of the walls.")
roomheight = int(input())
print("Please enter the length of one wall.")
roomwidth = int(input())
print("Please enter the length of the other wall.")
roomlength = int(input())
totaldim = (2*(roomheight*roomwidth))+(roomwidth*roomlength)+(2*(roomheight*roomlength))
print("Now enter the total dimensions of the unpaintable areas.")
unpaintdim = int(input())
print("Now enter how many layers of paint you would like.")
layers = int(input())
Neededpaint = ((totaldim - unpaintdim)*layers)/11
print("You need", Neededpaint,"litres of paint.")
