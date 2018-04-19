

def processUSGS_rating(rating_file):
    """
    Returns lists for stage, shift, and discharge (q) of a USGS
    rating curve file.
    """
    
    

    ##Empty lists for each variable
    stage = []
    shift = []
    q = []
    
    ## Reading the file
    with open(rating_file) as f:
        lines = f.readlines()
        
        for line in lines:
            # Passing header lines
            if not line.startswith(("#", "INDEP", "16N")):
                # Appending data to empty lists
                line_list = line.split()
                stage.append(line_list[0])
                shift.append(line_list[1])
                q.append(line_list[2])

    return stage, shift, q



def processHECfile(hec_file):
    """
    Returns lists for stage and discharge (hec_q) of a
    HECRAS model output .txt file.
    """

    
    ##Empty list objects for HECRAS variables
    hec_stage = []
    hec_q = []
    
    ##Reading the file
    with open(hec_file) as h:
        heclines = h.readlines()
        
        ## define beginning of data- assumes data lines begin @ line 13
        for hecline in heclines[14:]:
            hec_list= hecline.split()
            
            ##Checking for empty lines
            if hec_list != []:
                
                ##Checking for complete lines of data
                if len(hec_list) == 15:
                    
                    ## Appending data to empty lists
                    hec_stage.append(hec_list[3])
                    hec_q.append(hec_list[5])
                

                else:    
                    pass


    return hec_stage, hec_q
   
#if __name__ == '__main__':
#   processUSGS_rating()
#   processHECfile()
