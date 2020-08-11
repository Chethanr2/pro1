# This program will give the box printing
'''

**************
*            *
*            *
*            *
*            *
*            *
**************

'''
def BoxPrinting (symbole, width, hieght):

    if len(symbole) != 1:
        raise Exception('"Symbol" needs to be string of 1 not more than that')

    if (width) < 2 or (hieght) < 2:
        raise  Exception('Height and width should be greater than 2')

    print (symbole * width)

    for i in range(hieght - 2):
        print (symbole + (' ' * (width - 2) ) + symbole )

    print (symbole * width)


#BoxPrinting('*', 15, 7)
#BoxPrinting('$', 15, 9)
BoxPrinting('^', 19, 5)