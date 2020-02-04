class Lattice:

    def __init__(self, data):
        self.data = data  # lattice (assumed to be sorted by x, then by y, then by z)
        self.n, self.startLoc, self.endLoc = self.Grid(data)  # lattice properties (vectors)
        self.AssignConnections()  # populate lists of connecting lattice nodes

    def Grid(self, data):
        # lattice discretization
        self.x0 = sort(list(set(data['x'])))
        self.y0 = sort(list(set(data['y'])))
        self.z0 = sort(list(set(data['z'])))
        n = Vector(len(self.x0), len(self.y0), len(self.z0))
        startLoc = Vector(min(self.x0), min(self.y0), min(self.z0))
        endLoc = Vector(max(self.x0), max(self.y0), max(self.z0))
        return n, startLoc, endLoc

    def AssignConnections(self):
        # add index numbers for (up-sequence) connecting lattice nodes
        self.data['selfIndex'] = self.data.index.values
        self.data['xIndexUp'] = (self.data.index.values + 1) * (self.data['x'] != self.endLoc.x) - 1 * (
                    self.data['x'] == self.endLoc.x)  # for all x-axis connections
        self.data['yIndexUp'] = (self.data.index.values + self.n.x) * (self.data['y'] != self.endLoc.y) - 1 * (
                    self.data['y'] == self.endLoc.y)  # for all y-axis connections
        self.data['zIndexUp'] = (self.data.index.values + self.n.x * self.n.y) * (
                    self.data['z'] != self.endLoc.z) - 1 * (self.data['z'] == self.endLoc.z)  # for
