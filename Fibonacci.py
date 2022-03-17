def fibonacci( x ):
    a = 0
    b = 1
    for i in range( 0, x+1 ):
        print(a)
        c = a + b
        a=b
        b=c


num = int( input( "Enter any number :" ) )
fibonacci( num )
