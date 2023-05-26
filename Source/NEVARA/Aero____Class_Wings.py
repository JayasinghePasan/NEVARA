class wing:
    def __init__(self,wingName, trueChord, spanLength):
        self.wingName = wingName
        self.trueChord = trueChord
        self.spanLength = spanLength

        self.aspectRatio = self.spanLength / self.trueChord

        if wingName == "NACA0015":
            self.ClFunctionArray = [-30.353, -81.127, +4.2290, -17.6890, -0.1288, +6.5701, +0.0005]
            self.CdFunctionArray = [+71.467, +0.5047, -3.0477,  -0.0553, +0.3035, +0.0011, +0.0083]

        if wingName == "NACA0012":
            self.ClFunctionArray = [+2.9908, -236.17, -0.3472, -5.6825, +0.0239, +6.4798, -0.0004]
            self.CdFunctionArray = [+207.76, -0.0016, -16.892, -0.0016, +0.6903, +6e-05 , +0.0065]

        if wingName == "NACA0018":  ### WROOOONGGG
            self.ClFunctionArray = [+2.9908, -236.17, -0.3472, -5.6825, +0.0239, +6.4798, -0.0004]
            self.CdFunctionArray = [+207.76, -0.0016, -16.892, -0.0016, +0.6903, +6e-05 , +0.0065]