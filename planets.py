def weight_on_planets():
    weight = int(input("What do you weigh on earth? "))
    str1 = "\nOn Mars you would weigh {0:.2f} pounds.".format(weight * 0.38)
    str2 = "\nOn Jupiter you would weigh {0:.2f} pounds.".format(weight * 2.34)
    print(str1 + str2)   

   
if __name__ == '__main__':
   weight_on_planets()
