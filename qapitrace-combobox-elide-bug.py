import os
from os.path import abspath, dirname
try:
    from PySide6.QtCore import Qt, QSize, QPoint, QCoreApplication, QFile
    from PySide6.QtWidgets import QApplication, QDialog, QComboBox, QLayout
    from PySide6.QtWidgets import QVBoxLayout, QGroupBox, QGridLayout, QSizePolicy
    from PySide6.QtWidgets import QDialogButtonBox, QCheckBox, QSpinBox, QLabel
    from PySide6.QtUiTools import QUiLoader
except ModuleNotFoundError:
    from PySide2.QtCore import Qt, QSize, QPoint, QCoreApplication, QFile
    from PySide2.QtWidgets import QApplication, QDialog, QComboBox, QLayout
    from PySide2.QtWidgets import QVBoxLayout, QGroupBox, QGridLayout, QSizePolicy
    from PySide2.QtWidgets import QDialogButtonBox, QCheckBox, QSpinBox, QLabel
    from PySide2.QtUiTools import QUiLoader
    

def simpleComboDlg():
    dlg = QDialog()
    vLayout = QVBoxLayout(dlg)
    combo = QComboBox(dlg)
    combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
    #combo.setIconSize(QSize(0,0))
    vLayout.addWidget(combo)

    combo.addItem("Run & Check")
    #combo.setMinimumContentsLength(11)
    combo.setCurrentIndex(0)
    return dlg

def retracerDlg():
    dlg = QDialog()
    dlg.setWindowModality(Qt.ApplicationModal)
    dlg.resize(238, 282)
    dlg.setModal(True)
    vLayout = QVBoxLayout(dlg)
    #vLayout.setSizeConstraint(QLayout.SetFixedSize)

    checkboxesLayout = QVBoxLayout()
    checkboxesLayout.setObjectName("checkboxesLayout")
    doubleBufferingCB = QCheckBox(dlg)
    doubleBufferingCB.setObjectName("doubleBufferingCB")

    checkboxesLayout.addWidget(doubleBufferingCB)

    coreProfileCB = QCheckBox(dlg)
    coreProfileCB.setObjectName("coreProfileCB")

    checkboxesLayout.addWidget(coreProfileCB)

    errorCheckCB = QCheckBox(dlg)
    errorCheckCB.setObjectName("errorCheckCB")
    errorCheckCB.setChecked(True)

    checkboxesLayout.addWidget(errorCheckCB)

    singlethreadCB = QCheckBox(dlg)
    singlethreadCB.setObjectName("singlethreadCB")

    checkboxesLayout.addWidget(singlethreadCB)


    vLayout.addLayout(checkboxesLayout)

    queriesGroupBox = QGroupBox(dlg)
    sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(queriesGroupBox.sizePolicy().hasHeightForWidth())
    queriesGroupBox.setSizePolicy(sizePolicy)
    gridLayout = QGridLayout(queriesGroupBox)
    gridLayout.setObjectName("gridLayout")
    queryCheckReportThreshold = QSpinBox(queriesGroupBox)
    queryCheckReportThreshold.setObjectName("queryCheckReportThreshold")
    queryCheckReportThreshold.setMaximum(100000)
    queryCheckReportThreshold.setSingleStep(10)

    gridLayout.addWidget(queryCheckReportThreshold, 2, 1, 1, 1)

    checkThresholdLabel = QLabel(queriesGroupBox)
    checkThresholdLabel.setObjectName("checkThresholdLabel")

    gridLayout.addWidget(checkThresholdLabel, 2, 0, 1, 1)

    handlingLabel = QLabel(queriesGroupBox)
    handlingLabel.setObjectName("handlingLabel")

    gridLayout.addWidget(handlingLabel, 1, 0, 1, 1)

    combo = QComboBox(queriesGroupBox)
    combo.setObjectName("queryHandlingSelector")
    combo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
    #combo.setIconSize(QSize(0,0))
    gridLayout.addWidget(combo, 1, 1, 1, 1)

    vLayout.addWidget(queriesGroupBox)

    dlg.setWindowTitle(QCoreApplication.translate("RetracerDialog", "Retracer Configuration", None))
    doubleBufferingCB.setText(QCoreApplication.translate("RetracerDialog", "Use double buffering", None))
    coreProfileCB.setText(QCoreApplication.translate("RetracerDialog", "Use core profile", None))
    errorCheckCB.setText(QCoreApplication.translate("RetracerDialog", "Error checking", None))
    singlethreadCB.setText(QCoreApplication.translate("RetracerDialog", "Singlethread", None))
    queriesGroupBox.setTitle(QCoreApplication.translate("RetracerDialog", "Queries", None))
    checkThresholdLabel.setText(QCoreApplication.translate("RetracerDialog", "Check threshold:", None))
    handlingLabel.setText(QCoreApplication.translate("RetracerDialog", "Handling:", None))
    combo.setCurrentText("")


    combo.addItem("Skip")
    combo.addItem("Run")
    combo.addItem("Run & Check")
    #combo.setMinimumContentsLength(11)
    combo.setCurrentIndex(0)
    return dlg

def retracerDlgFromUiFile():
    loader = QUiLoader()
    file = QFile(f"{abspath(dirname(__file__))}/retracerdialog.ui")
    file.open(QFile.ReadOnly)
    dlg = loader.load(file)
    file.close()

    #print(dir(Qt.WindowModality))
    dlg.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
    #dlg.setWindowModality(Qt.NonModal)
    #dlg.setModal(False)
 
    dlg.queryHandlingSelector.addItem("Skip")   
    dlg.queryHandlingSelector.addItem("Run")   
    dlg.queryHandlingSelector.addItem("Run & Check") 
    dlg.queryHandlingSelector.setCurrentIndex(0)
    dlg.queryHandlingSelector.setPlaceholderText("Foo")
    return dlg


if __name__ == "__main__":
    app = QApplication()

    #dialogs = [ simpleComboDlg(), retracerDlg() ]
    dialogs = [ retracerDlg(), retracerDlgFromUiFile() ]

    prevPos = QPoint(500, 500)
    for dialog in dialogs:
        dialog.move(prevPos)
        dialog.show() 
        prevPos = prevPos + QPoint(dialog.width(), 0)
    app.exec_()
