## My recursion
import time

my_dict = { }

# DYNAMIC PROGRAMMING FIBONACCI
def fibonacci( n , my_dict ):
    if  (n in my_dict) :
        return my_dict[n];
    if (n<=2):
        return 1;
    my_dict[n]   =  fibonacci(n-2,my_dict) + fibonacci(n-1,my_dict);
    return my_dict[n]


# Static Fibonacci - Old 
def fibo(n):
    if (n<=2 ):
        return 1;
    return ( fibo(n-1) + fibo(n-2) ) ;


def main():
    print("DYNAMIC PROGRAMMING , fibo of 3 , 5 ,10 & 36 ");
    start_time = time.time()
    print(fibonacci(3, my_dict));
    print(fibonacci(5,my_dict));
    print(fibonacci(10,my_dict));
    print(fibonacci(50,my_dict));
    print("--- %s seconds ---" % (time.time() - start_time))
    print("OLD NON MEOIZATION FIBO");
    start_time = time.time()
    print(fibo(3));
    print(fibo(5));
    print(fibo(10));
    print(fibo(50));
    print("--- %s seconds ---" % (time.time() - start_time))

    



if __name__ == "__main__":
    main()

