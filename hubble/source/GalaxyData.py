
class GalaxyData:
    def __init__(self, filename):
        self._filename = filename
        self._columnNames = []
        self._galaxies = []

        self._vRec = {} # recession velocities
        self._A_V_MW = {} # V-band extinction in MW towards galaxy

        rowCount = 0
        with open(self._filename, 'r') as lines:
            for line in lines:
                rowCount += 1
                row = line.strip()
                s = line[0]  # in case we need to identify a commented data line
                data = row.lstrip('#').split()
                colCount = len(data)

                if rowCount == 1:
                    self._columnNames = data
                elif rowCount == 2:
                    pass # ignore second line
                else:
                    galaxyName = data[0]
                    galaxy = {
                        'Name': data[0],
                        self._columnNames[1]: float(data[1]),
                        self._columnNames[2]: float(data[2])
                    }
                    self._galaxies.append(galaxy)

                    self._vRec[galaxyName] = float(data[1])
                    self._A_V_MW[galaxyName] = float(data[2])

    def vRec(self, galaxyName):
        return self._vRec[galaxyName]

    def A_V_MW(self, galaxyName):
        return self._A_V_MW[galaxyName]

    def process(self):
        pass    # to do

    def show(self):
        print ('Galaxy Data:')
        for galaxy in self._galaxies:
            print ('Name=' + str(galaxy['Name']) \
                  + ' Recession=' + str(galaxy['Recession']) \
                  + ' A_{V,MW}=' + str(galaxy['A_{V,MW}']))

    def display(self):
        print ('Galaxy Data:')
        print ('Name   Recession  A_{V,MW}')
        for galaxy in self._galaxies:
            print('{0:8s} {1:7.1f} {2:7.4f} '.format(galaxy['Name'],
                                                      galaxy['Recession'],
                                                      galaxy['A_{V,MW}'],
                                                      ))

