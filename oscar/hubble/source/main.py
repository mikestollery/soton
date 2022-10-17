
from MWCepheids import MWCepheids
from GalaxyData import GalaxyData
from GalCepheids import GalCepheids
from Galaxy import Galaxy

def main():

    # Read Milky Way Cepheids data from file
    mwCepheids = MWCepheids('MW_Cepheids.dat')
    mwCepheids.display()  # view data as a table
    #mwCepheids.show()    # view unformatted data
    mwCepheids.process()

    # Read Galaxy Data from file
    galaxyData = GalaxyData('galaxy_data.dat')
    galaxyData.process()
    #galaxyData.display()
    #galaxyData.show()

    galaxyDict = {} # A collection of Galaxy objects

    # Read Galaxy Cepheids data from 8 files
    for n in range(8):
        filename = 'hst_gal' + str(n + 1) + '_cepheids.dat'
        galCepheids = GalCepheids(filename)
        galaxyName = galCepheids.galaxyName()
        vRec = galaxyData.vRec(galaxyName)
        A_V_MW = galaxyData.A_V_MW(galaxyName)

        # Put galaxy data and cepheids in Galaxy object for each galaxy
        galaxyDict[galaxyName] = Galaxy(galaxyName, vRec, A_V_MW, galCepheids, mwCepheids)

    # process each galaxy
    totalH0 = 0.0
    for galaxyName in galaxyDict.keys():
        galaxy = galaxyDict[galaxyName]
        galaxy.process()
        totalH0 += galaxy._H0
        galaxy.display()
        #galaxy.show()

    meanH0 = totalH0 / 8
    print('meanH0=' + str(meanH0))
    tau = 1 / meanH0
    print('tau=' + str(tau))



print ('')
print ('########### START #############')

if(__name__ == "__main__"):
    main()

print ('###########  END  #############')






