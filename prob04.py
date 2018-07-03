def main():
    # Get input
    altitudes = [int(num) for num in input().split()]

    # Declare varaible to store number of peaks
    no_of_peaks = 0
    
    # Iterate through altitudes
    for i, altitude in enumerate(altitudes[:-1]):

        # Check for diffrence in altitude
        difference = altitude - altitudes[i+1]

        # If difference is positive, current altitude is mountain peak
        if difference > 0:
            
            # Print peak value
            print(altitude, end=" ")

            # Increment peak number counter
            no_of_peaks += 1

    print()

    # If altitude is last altitude, check if is higher than previous altitude
    if altitudes[-1] > altitudes[-2]:

        # Then consider altitude as peak
        print(altitudes[-1])
        
        # Increment peak number counter
        no_of_peaks += 1

    # Print total number of peaks(ie. the number of flags to carry)
    print(no_of_peaks)
    

if __name__ == "__main__":
    main()