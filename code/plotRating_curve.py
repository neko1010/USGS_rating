import matplotlib.pyplot as plt
import sys
import processRating_data as pRd


def control_args():
    """
    Flags necessary for plot (-p) and 
    """
    #alternate string formatting
    verbose = "Stage range = {0} - {1}".format(stage[0], stage[-1])
    #verbose = "Stage range = %s - %s" %(stage[0], stage[-1])
    plot = False
    if "-p" in sys.argv[:]:
        plot = True
    
    #if "-txt" in sys.argv[:]:
    #    verbose = False

    return verbose, plot 
    

def plotRating_curve(q, stage, hec_q, hec_stage, verbose):
    """
    Plots modeled HECRAS output against USGS rating curve.
    Requires three command line arguments:
    1. USGS  rating file location
    2. HECRAS output file location
    3. String for site name
    4. '-p' flag necessary to plot- see control_args
    """
    
    ## Plot line (USGS rating file)
    plt.plot(q,stage, label= 'USGS Rating Curve')
    
    ## Plot scatter (HECRAS model output)
    plt.scatter(hec_q, hec_stage, s= 5, label = 'HECRAS Model', color = 'black') 
    ## Setting x-axis to log scale
    plt.xscale('log')
    plt.title( sys.argv[3] + ' Rating Curve')
    plt.xlabel('Discharge (cfs)')
    plt.ylabel('Stage (ft)')
    plt.legend()
    plt.annotate(verbose, (3,33))
    
    plt.show()
   
if __name__ == '__main__':
   # processUSGS_rating()
   # processHECfile()
    
    stage, shift, q = pRd.processUSGS_rating(sys.argv[1])
    hec_stage, hec_q = pRd.processHECfile(sys.argv[2])

    verbose, plot = control_args()

    if plot == True:
        plotRating_curve(q, stage, hec_q, hec_stage, verbose)

    else:
        print(verbose)
