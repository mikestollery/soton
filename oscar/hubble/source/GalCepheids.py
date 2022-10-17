
import math

class GalCepheids:
    def __init__(self, filename):
        self._filename = filename
        self._galaxyName = ''
        self._columnNames = []
        self._cepheids = []

        rowCount = 0
        with open(self._filename, 'r') as lines:
            for line in lines:
                rowCount += 1
                row = line.strip()
                s = line[0]  # in case we need to identify a commented data line
                data = row.lstrip('#').split()
                colCount = len(data)

                if rowCount == 1:
                    self._galaxyName = data[0] + data[1]
                elif rowCount == 2:
                    self._columnNames = data
                else:
                    cepheid = {
                        self._columnNames[0]: data[0],
                        self._columnNames[1]: float(data[1]),
                        self._columnNames[2]: float(data[2]),
                        self._columnNames[3]: float(data[3]),
                        'M_V': 0.0, # to be calculated
                        'dpc_V': 0.0
                    }
                    self._cepheids.append(cepheid)

    def galaxyName(self):
        return self._galaxyName

    def process(self):
        pass    # to do

    def calcM_V(self, alpha_V, beta_V):
        
        for cepheid in self._cepheids:
            cepheid['M_V'] = alpha_V * cepheid['logP'] + beta_V  # placeholder
            # need to calculate this from 2.2.3 Distances for a Set of Nearby Galaxies (page 5)
            # mv - Mv = 5 log(dpc) - 5 + Av
            
    def calc_dpc_V (self, A_V_MW):
        for cepheid in self._cepheids:
            cepheid['dpc_V'] = math.exp((cepheid['m_V'] + 5 - cepheid['M_V'] - A_V_MW)/5)
        
    def show(self):
        print ("Galaxy Name: " + self._galaxyName)
        for cepheid in self._cepheids:
            print ('Name=' + str(cepheid['Name']) \
                  + ' logP=' + str(cepheid['logP']) \
                  + ' m_V=' + str(cepheid['m_V']) \
                  + ' m_I=' + str(cepheid['m_I']) \
                  + ' M_V=' + str(cepheid['M_V']))

    def display(self):
        print ("Galaxy Name: " + self._galaxyName)
        print ('Name       logP   m_V    m_I      M_V      dpc_V')
        for cepheid in self._cepheids:
            print('{0:8s} {1:6.3f} {2:6.2f} {3:6.2f} {4:6.2f} {5:6.2f}'.format(cepheid['Name'],
                                                              cepheid['logP'],
                                                              cepheid['m_V'],
                                                              cepheid['m_I'],
                                                              cepheid['M_V'],
                                                              cepheid['dpc_V']))

    def galaxy_dist(self):
        average = 0
        n = 0
        for cepheid in self._cepheids:
            average += cepheid['dpc_V']
            n += 1
        average = average/n
        print (average, n)
        return average





