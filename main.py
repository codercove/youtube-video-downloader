from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys
from pytube import YouTube, Playlist


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Youtube Downloader')
        self.setWindowIcon(QtGui.QIcon('favicon.ico'))
        self.setGeometry(100, 100, 300, 400)
        self.formGroupBox = QGroupBox('YT Downloader')
        self.selectOP = QComboBox()
        self.selectOPQuality = QComboBox()
        self.selectOP.addItems(['Video', 'Playlist'])
        self.selectOPQuality.addItems(['Low', 'High'])
        self.videoURL = QLineEdit()
        self.createForm()
        self.previewImage = QLineEdit()
        self.buttonBox1 = QDialogButtonBox(QDialogButtonBox.Ok)
        self.buttonBox2 = QDialogButtonBox(QDialogButtonBox.Cancel)
        self.buttonBox1.accepted.connect(self.start)
        self.buttonBox2.rejected.connect(self.reject)
        self.Alert = QLineEdit()
        self.previewImage.setText('All rights  reserved by ncoderlk')
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.buttonBox1)
        mainLayout.addWidget(self.buttonBox2)
        mainLayout.addWidget(self.Alert)
        mainLayout.addWidget(self.previewImage)
        self.setLayout(mainLayout)
        self.Alert.setText('No Error Found')

    def start(self):
        URL = self.videoURL.text()
        option = self.selectOP.currentText()
        quality = self.selectOPQuality.currentText()
        if (URL == ""):
            self.Alert.setText('URL Box Cannot Be Empty')
        else:
            if (option == "Video"):
                self.downloadVideo(URL, quality)
            elif (option == "Playlist"):
                self.downloadPlaylist(URL, quality)

    def downloadVideo(self, link, quality):
        if link != "":
            video = YouTube(link)
            if quality == 'High':
                video = video.streams.get_highest_resolution()
            elif quality == 'Low':
                video = video.streams.get_lowest_resolution()

            try:
                video.download('./downloaded-videos/')
                self.Alert.setText("Downloading...")
                self.previewImage.setText(video.get_file_path())
                self.previewImage.setText(video.exists_at_path())
            except:
                self.Alert.setText('Error While Downloading Video...')
            self.Alert.setText("Video Downloaded Succesfully...")

    def downloadPlaylist(self, links, quality):
        p = Playlist(links)
        try:
            for video in p.videos:
                if quality == 'High':
                    video = video.streams.get_highest_resolution()
                elif quality == 'Low':
                    video = video.streams.get_lowest_resolution()
                video.streams.first().download('./downloaded-playlists')
                self.previewImage.setText(video.get_file_path())
                self.previewImage.setText(video.exists_at_path())
        except:
            self.Alert.setText('Error While Downloading Playlist...')

    def createForm(self):
        layout = QFormLayout()
        layout.addRow(QLabel("URL"), self.videoURL)
        layout.addRow(QLabel("Select"), self.selectOP)
        layout.addRow(QLabel("Quality"), self.selectOPQuality)
        self.formGroupBox.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
