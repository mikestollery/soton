'''
This holds all the information we need for a particular galaxy.
Recession Velocity (vRec) and Visual Extinction within Milky Way (A_V_MW)
have been obtained from the galaxy data file.
The galaxy's cepheids have been obtained from the hst_gal_cepheids file
'''


class Galaxy:
    def __init__(self, name, vRec, A_V_MW, cepheids, mwCepheids):
        self._name = name
        self._vRec = vRec
        self._A_V_MW = A_V_MW 
        self._dpc_V = 0.0 # get this from GalCepheids average dpc
        self._H0 = 0.0
        self._cepheids = cepheids
        self._mwCepheids = mwCepheids

    def process(self):
        self._cepheids.calcM_V(self._mwCepheids.alpha_V(), 
                               self._mwCepheids.beta_V())
        self._cepheids.calc_dpc_V(self._A_V_MW)
        self._dpc_V = self._cepheids.galaxy_dist()
        self._H0 = self._vRec/self._dpc_V
        
        pass    # to do

    def show(self):
        print ('Galaxy name=' + str(self._name) + ' vRec=' + str(self._vRec) + ' A_V_MW=' + str(self._A_V_MW))
        self._cepheids.show()

    def display(self):
        print ('Galaxy name=' + str(self._name) + ' vRec=' + str(self._vRec) + ' A_V_MW=' + str(self._A_V_MW) + ' Galaxy dist=' + str(self._dpc_V), ' H0=' + str(self._H0))
        self._cepheids.display()

