class Ucus():
    havayolu = "THY"

    def __init__(self, kod,kalkis,varis,sure,kapasite,yolcu):
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.sure=sure
        self.kapasite=kapasite
        self.yolcu=yolcu

    def anonsn_yap(self ):

        return "{} sefer sayılı  {} - {} ucusumuz {} dk surecek".format(
            self.kod,
            self.kalkis,
            self.varis,
            self.sure)

ucus2 = Ucus('TK78','23.00','01.55',175,200,150)
cikti=ucus2.anonsn_yap()
print(cikti)