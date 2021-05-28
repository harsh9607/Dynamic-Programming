'''
# Grid Traveller 
A player can move  Right and Down to reach to the Destination for an MxN matrix

     ---------------------------
     |  O    |          |       |  
     ---------------------------
     |       |         |        |
     ----------------------------
     |       |         |   D    |
      ---------------------------
     O - Origin
     D - Destination
    3x3 :  6 ways - (RRDD , RDRD,RDDR,DDRR,DRDR,DRRD)
'''
import time
my_dict = { }

# DYNAMIC PROGRAMMING Grid Traveller 
def grid_traveller( m,n , my_dict ):
    if  ( (m,n) in my_dict) :
        return my_dict[(m,n)];
    if (m==1 and n==1):
        return 1;
    if ( m ==0 or n==0):
        return 0 ;
    my_dict[(m,n)]   =  grid_traveller(m,n-1,my_dict) + grid_traveller(m-1,n,my_dict);
    return my_dict[(m,n)];


# Grid_Traveller - Old 
def old_grid_traveller( m,n  ):
    if (m==1 and n==1):
        return 1;
    if ( m ==0 or n==0):
        return 0 ;
    return old_grid_traveller(m,n-1) + old_grid_traveller(m-1,n);
    


def main():

    print("DYNAMIC PROGRAMMING GRID TRAVELLER ");
    start_time = time.time()
    print(grid_traveller(15,15, my_dict));
    print("--- %s seconds ---" % (time.time() - start_time))

    print("OLD NON MEOIZATION FIBO");
    start_time = time.time()
    print(old_grid_traveller(15,15))
    print("--- %s seconds ---" % (time.time() - start_time))

    


if __name__ == "__main__":
    main()

