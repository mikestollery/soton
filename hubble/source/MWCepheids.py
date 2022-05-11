import math
#import numpy as np
from matplotlib import pyplot as plt


class MWCepheids:
    def __init__(self, filename):
        self._filename = filename
        self._columnNames = []
        self._cepheids = []

        # To be calculated from derived data
        self._alpha_V = 0.0
        self._alpha_I = 0.0
        self._beta_V = 0.0
        self._beta_I = 0.0

        rowCount = 0
        with open(self._filename, 'r') as lines:
            for line in lines:
                rowCount += 1
                row = line.strip()
                s = line[0]  # in case we need to identify a commented data line
                data = row.lstrip('#').split()
                colCount = len(data)
                #print (str(colCount) + ': line=' + str(line)) # DEBUG only
                if (colCount > 7):

                    if rowCount == 1:
                        self._columnNames = data
                    elif rowCount == 2:
                        pass # ignore second line
                    elif rowCount == 3:
                        pass # ignore third line
                    else:
                        # derived data:
                        logP = math.log(float(data[3])) # log(Period)
                        dpc = 1000 / float(data[1])  # distance (from earth) in parsecs
                        mu = 5 * math.log(dpc) - 5 # distance modulus (m - M)

                        # Abs V mag = Apparent V mag - mu - A_V
                        M_V = float(data[4]) - mu - float(data[6])

                        # Abs I mag = Apparent I mag - mu - A_I
                        M_I = float(data[5]) - mu - (0.556 * float(data[6]))  # A_I = 0.556 * A_V

                        cepheid = {
                                self._columnNames[0]: data[0],
                                self._columnNames[1]: float(data[1]),
                                self._columnNames[2]: float(data[2]),
                                self._columnNames[3]: float(data[3]), # Period
                                self._columnNames[4]: float(data[4]), # m_V
                                self._columnNames[5]: float(data[5]), # m_I
                                self._columnNames[6]: float(data[6]),
                                self._columnNames[7]: float(data[7]),
                                'logP': logP,
                                'dpc': dpc,
                                'mu': mu,
                                'M_V': M_V,
                                'M_I': M_I,
                                #'M_Verr': errors!!!
                        }
                        self._cepheids.append(cepheid)

    def process(self ):
        
        logP_list = [] # x-values
        M_V_list = [] # y-values
        for cepheid in self._cepheids:
            print('x: logP=' + str(cepheid['logP']))
            print('y: M_V=' + str(cepheid['M_V']))
            logP_list.append(cepheid['logP'])
            M_V_list.append(cepheid['M_V'])

        print('logP_list=' + str(logP_list))
        print('M_V_list=' + str(M_V_list))

        plt.xlabel('logP')
        plt.ylabel('M_V')
        plt.title('')
        plt.plot(logP_list, M_V_list, color='red', marker='o', markersize=5, linestyle="None")
        plt.show()

        # hardcoded values
        self._alpha_V = -1.22385
        self._alpha_I = -1.22385
        self._beta_V = -18.10425
        self._beta_I = -18.10425


    def alpha_V(self):
        return self._alpha_V

    def alpha_I(self):
        return self._alpha_I

    def beta_V(self):
        return self._beta_V

    def beta_I(self):
        return self._beta_I

    def show(self):
        print ('Milky Way Cepheids:')
        for cepheid in self._cepheids:
            print ('Object=' + str(cepheid['Object']) \
                  + ' parallax=' + str(cepheid['parallax']) \
                  + ' err(par)=' + str(cepheid['err(par)']) \
                  + ' Period=' + str(cepheid['Period']) \
                  + ' m_V=' + str(cepheid['m_V']) \
                  + ' m_I=' + str(cepheid['m_I']) \
                  + ' A_V=' + str(cepheid['A_V']) \
                  + ' err(A_V)=' + str(cepheid['err(A_V)']) \
                  + ' logP=' + str(cepheid['logP'])\
                  + ' dpc=' + str(cepheid['dpc'])\
                  + ' mu=' + str(cepheid['mu'])\
                  + ' M_V=' + str(cepheid['M_V'])\
                  + ' M_I=' + str(cepheid['M_I']))

    def display(self):
        print ('Milky Way Cepheids:')
        print ('Object	  Parallax err(par) Period  m_V      m_I  A_V err(A_V) logP    dpc     mu      M_V     M_I')
        for cepheid in self._cepheids:
            print('{0:12s} {1:5.2f} {2:4.2f} {3:10.6f} {4:6.3f} {5:6.3f} {6:4.2f} {7:4.2f}     {8:6.4f} {9:8.3f} {10:6.3f} {11:7.3f} {12:7.3f}'.format(cepheid['Object'],
                                            cepheid['parallax'],
                                            cepheid['err(par)'],
                                            cepheid['Period'],
                                            cepheid['m_V'],
                                            cepheid['m_I'],
                                            cepheid['A_V'],
                                            cepheid['err(A_V)'],
                                            cepheid['logP'],
                                            cepheid['dpc'],
                                            cepheid['mu'],
                                            cepheid['M_V'],
                                            cepheid['M_I']))
