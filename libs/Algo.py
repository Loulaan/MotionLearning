import os, shutil
import subprocess
from ConvFun import *
import librosa
import numpy as np


def str2int(strT):
    if strT == '0':
        strT = '0:0'
    index = strT.find(':')
    sec = float(strT[index+1:]) + 60 * float(strT[:index])
    return sec


def MLConv(self, GUI):
    """ Конвертер """
    if GUI.savePath[-1] != '/':  # Проверка пути без к фалу
        GUI.savePath += '\\'
    if os.path.exists('temp'):
        shutil.rmtree('temp')
    os.makedirs('temp')  # создание временной папки temp
    subprocess.call("ffmpeg\\bin\\ffmpeg -y -i {0} -ar 44100 -ac 2 -ab 192K -vn {1}".format(
        GUI.currentFileName + GUI.preFile, 'temp\\TempAudio.wav'), creationflags=0x08000000,
        shell=True)  # Извлечение звуковой дорожки
    
    GUI.settings.setEnabled(False)

    if GUI.settings.ui.aRBf_1.isChecked():
        GUI.ath.start()

    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # устанавливаем видео кодек
    cap = cv2.VideoCapture(GUI.currentFileName + GUI.preFile)  # Захват видео файла
    valueForPBMax = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # получаем кол-во кадров (нужно для progressBar'a)
    width = int(cap.get(3))
    heigth = int(cap.get(4))  # получаем ширину и высоту кадра
    size = width, heigth
    fps = float(cap.get(5))  # получаем fps видео

    modeF = setFlagF(GUI)  # Извлечение мода обработки фреймов из radioButtons
    modeS = setFlagS(GUI)

    vid = cv2.VideoWriter('temp\\temp_' + GUI.doneFile, fourcc, fps, size, 1)  # задаем параметры записи кадра
    self.StatusBarSignal.emit('Converting...')
    currentPBValue = 0

    start = GUI.settings.ui.lineEdit.text()
    end = GUI.settings.ui.lineEdit_2.text()

    startI = str2int(start)
    endI = str2int(end)
    st = startI*fps
    en = endI*fps

    mid = (st + en) / 2
    brd = (en - st) / 2
    i = 0

    while cap.grab(): # Проверяем есть ли в видео еще не обработанные кадры
        _, frame = cap.retrieve() # достаем кадр

        if abs(i - mid) <= brd:
            doneFrame = ConvPilot(frame, modeF, modeS)  # конвертируем кадр
            vid.write(doneFrame)  # Запись обработанного кадра
        else:
            vid.write(frame)

        currentPBValue += 1
        currentPBValueInPersent = currentPBValue * 100 / valueForPBMax
        self.ProgressBarSignal.emit(currentPBValueInPersent)
        i += 1
    cap.release()  # Закрываем чтение
    vid.release()  # закрываем запись
    self.StatusBarSignal.emit('Final touches')

    if GUI.settings.ui.aRBf_1.isChecked():
        while GUI.ath.isRun:
            pass

    subprocess.call("ffmpeg\\bin\\ffmpeg -y -i {0} -i {1} -vcodec copy -shortest {2}".format
                    ('temp\\TempAudio.wav', 'temp\\temp_' + GUI.doneFile, GUI.savePath + GUI.doneFile),
                    creationflags=0x08000000, shell=True)  # Наложение звуковой дорожки на основное видео
    shutil.rmtree('temp')  # Удаление папки temp
    self.StatusBarSignal.emit('Complited!')
    GUI.settings.setEnabled(True)


def AudioConv(self, GUI):
    self.isRun = True
    y, sr = librosa.load("temp\\TempAudio.wav", sr=None, mono=False)
    y1, y2 = y[0], y[1]
    shift = GUI.settings.ui.spinBox.value()
    fShift = float(shift) / 100
    y_shifted1 = librosa.effects.pitch_shift(y1, sr, n_steps=fShift) # shifted by -0.1 half steps
    y_shifted2 = librosa.effects.pitch_shift(y2, sr, n_steps=fShift) # shifted by -0.1 half steps
    new = np.array([y_shifted1, y_shifted2])
    librosa.output.write_wav('temp\\TempAudio.wav', new, sr)
    self.isRun = False