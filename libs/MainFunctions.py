import time
from PyQt5 import QtWidgets
from Algo import *

# Functions


def About(self):
    if not self.dA.isVisible():
        self.dA.show()
    else:
        self.dA.activateWindow()


def open_file(self):
    """ Open Video File """
    self.ui.statusbar.showMessage('Opening file...')

    def formatFile(NameOfFile):
        """ Функция достает название файла из пути к нему """
        res = ''
        for s in reversed(NameOfFile):
            if s == "/":
                break
            else:
                res = s + res
        return res

    filters = "Video (*.264 *.3g2 *.3gp *.3gp2 *.3gpp *.3gpp2 *.3mm *.3p2 *.60d *.787 *.89 *.aaf *.aec *.aep *.aepx *.aet *.aetx *.ajp *.ale *.am *.amc *.amv *.amx *.anim *.aqt *.arcut *.arf *.asf *.asx *.avb *.avc *.avd *.avi *.avp *.avs *.avs *.avv *.axm *.bdm *.bdmv *.bdt2 *.bdt3 *.bik *.bin *.bix *.bmk *.bnp *.box *.bs4 *.bsf *.bvr *.byu *.camproj *.camrec *.camv *.ced *.cel *.cine *.cip *.clpi *.cmmp *.cmmtpl *.cmproj *.cmrec *.cpi *.cst *.cvc *.cx3 *.d2v *.d3v *.dat *.dav *.dce *.dck *.dcr *.dcr *.ddat *.dif *.dir *.divx *.dlx *.dmb *.dmsd *.dmsd3d *.dmsm *.dmsm3d *.dmss *.dmx *.dnc *.dpa *.dpg *.dream *.dsy *.dv *.dv-avi *.dv4 *.dvdmedia *.dvr *.dvr-ms *.dvx *.dxr *.dzm *.dzp *.dzt *.edl *.evo *.eye *.ezt *.f4p *.f4v *.fbr *.fbr *.fbz *.fcp *.fcproject *.ffd *.flc *.flh *.fli *.flv *.flx *.gfp *.gl *.gom *.grasp *.gts *.gvi *.gvp *.h264 *.hdmov *.hkm *.ifo *.imovieproj *.imovieproject *.ircp *.irf *.ism *.ismc *.ismv *.iva *.ivf *.ivr *.ivs *.izz *.izzy *.jss *.jts *.jtv *.k3g *.kmv *.ktn *.lrec *.lsf *.lsx *.m15 *.m1pg *.m1v *.m21 *.m21 *.m2a *.m2p *.m2t *.m2ts *.m2v *.m4e *.m4u *.m4v *.m75 *.mani *.meta *.mgv *.mj2 *.mjp *.mjpg *.mk3d *.mkv *.mmv *.mnv *.mob *.mod *.modd *.moff *.moi *.moov *.mov *.movie *.mp21 *.mp21 *.mp2v *.mp4 *.mp4v *.mpe *.mpeg *.mpeg1 *.mpeg4 *.mpf *.mpg *.mpg2 *.mpgindex *.mpl *.mpl *.mpls *.mpsub *.mpv *.mpv2 *.mqv *.msdvd *.mse *.msh *.mswmm *.mts *.mtv *.mvb *.mvc *.mvd *.mve *.mvex *.mvp *.mvp *.mvy *.mxf *.mxv *.mys *.ncor *.nsv *.nut *.nuv *.nvc *.ogm *.ogv *.ogx *.osp *.otrkey *.pac *.par *.pds *.pgi *.photoshow *.piv *.pjs *.playlist *.plproj *.pmf *.pmv *.pns *.ppj *.prel *.pro *.prproj *.prtl *.psb *.psh *.pssd *.pva *.pvr *.pxv *.qt *.qtch *.qtindex *.qtl *.qtm *.qtz *.r3d *.rcd *.rcproject *.rdb *.rec *.rm *.rmd *.rmd *.rmp *.rms *.rmv *.rmvb *.roq *.rp *.rsx *.rts *.rts *.rum *.rv *.rvid *.rvl *.sbk *.sbt *.scc *.scm *.scm *.scn *.screenflow *.sec *.sedprj *.seq *.sfd *.sfvidcap *.siv *.smi *.smi *.smil *.smk *.sml *.smv *.spl *.sqz *.srt *.ssf *.ssm *.stl *.str *.stx *.svi *.swf *.swi *.swt *.tda3mt *.tdx *.thp *.tivo *.tix *.tod *.tp *.tp0 *.tpd *.tpr *.trp *.ts *.tsp *.ttxt *.tvs *.usf *.usm *.vc1 *.vcpf *.vcr *.vcv *.vdo *.vdr *.vdx *.veg *.vem *.vep *.vf *.vft *.vfw *.vfz *.vgz *.vid *.video *.viewlet *.viv *.vivo *.vlab *.vob *.vp3 *.vp6 *.vp7 *.vpj *.vro *.vs4 *.vse *.vsp *.w32 *.wcp *.webm *.wlmp *.wm *.wmd *.wmmp *.wmv *.wmx *.wot *.wp3 *.wpl *.wtv *.wve *.wvx *.xej *.xel *.xesc *.xfl *.xlmv *.xmv *.xvid *.y4m *.yog *.yuv *.zeg *.zm1 *.zm2 *.zm3 *.zmv)"
    selected_filter = filters
    filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'), filters, selected_filter)  # Получаем путь к файлу
    if filename[0]:  # Убеждаемся что путь не пустой ( баг с активацией функции open_file и закрытием диалогового окна прежде чем выберем файл )
        formCurrentFileName = formatFile(filename[0])
        if self.savePath == '':
            self.savePath = filename[0][:-len(formCurrentFileName)]
            self.currentFileName = filename[0][:-len(formCurrentFileName)-1] + '/'
        self.preFile = formCurrentFileName
        self.doneFile = 'conv_' + formCurrentFileName
        self.ui.label_2.setText(formCurrentFileName.strip())
        self.ui.pushButton.setEnabled(True)
        self.ui.statusbar.showMessage('')
        cap = cv2.VideoCapture(self.currentFileName + self.preFile)
        MaxFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # получаем кол-во кадров (нужно для progressBar'a)
        fps = float(cap.get(5)) # получаем fps видео
        t = MaxFrames / fps + (MaxFrames % fps > 0)
        self.settings.ui.lineEdit.setText("0")
        mEnd = str(round(t / 60))
        sEnd = str(round(t % 60))
        if len(sEnd) == 1:
            sEnd = "0" + sEnd
        self.settings.ui.lineEdit_2.setText(mEnd + ":" + sEnd)
        cap.release()
        

def ConfirmChoice(self):
    self.savePath = self.dSP.ui.lineEdit.displayText()
    self.dSP.close()


def ChangePath(self):
    directory = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory', os.getenv('HOME'))
    if directory:
        self.dSP.ui.lineEdit.setText(directory)
        self.savePath = directory
    self.dSP.activateWindow()


def ChangeSavePath(self):
    """ Change save path """
    self.dSP.ui.lineEdit.setText(self.savePath)
    if not self.dSP.isVisible():
        self.dSP.show()
    else:
        self.dSP.activateWindow()


def convert(self):
    """ Video Converter """
    self.ui.pushButton.setEnabled(False)
    self.ui.statusbar.showMessage('Checking file')
    if self.currentFileName == '': # Проверка не пустой ли путь к файлу
        self.ui.statusbar.showMessage('No file selected!')
    else:
        self.ui.statusbar.showMessage('Start converting')
    time.sleep(0.5)
    self.th.start()
        

def FinishTh(self):
    time.sleep(0.5)
    self.ui.statusbar.showMessage('')
    self.ui.pushButton.setEnabled(True)


def SettingsStart(self):
    if not self.settings.isVisible():
        self.settings.show()
    else:
        self.settings.activateWindow()


def ConfirmSettings(self):
    self.settings.close()

def EnabledSpinBox(self):
    self.settings.ui.spinBox.setEnabled( self.settings.ui.aRBf_1.isChecked() )