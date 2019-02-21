#
def example1():
    for i in range( 3 ):
        x = int( input( "enter a number: " ) )
        y = int( input( "enter another number: " ) )
        print( x, '/', y, '=', x/y )


def example2(L):
    print( "\n\nExample 2" )
    sum = 0
    sumOfPairs = []
    for i in range( len(L) ):
        sumOfPairs.append(L[i]+L[i+1])

    print( "sumOfPairs = ", sumOfPairs )


def printUpperFile( fileName ):
   file = open( fileName, "r" )
   for line in file:
       print( line.upper() )
   file.close()

def main():
    try:
        example1()
        L = [ 10, 3, 5, 6, 9, 3 ]
        example2( L )
        example2( [ 10, 3, 5, 6, 4, 3 ] )
        example2( [ 10, 3, 5, 6 ] )

        printUpperFile( "doesNotExistYet.txt" )
        printUpperFile( "misspelled.txt" )
    except IndexError:
        print("You have an index error.")
main()
