#include "mainwindow.h"
#include "./ui_retracerdialog.h"

#include <QApplication>
#include <QComboBox>
#include <QTimer>

class ComboBox : public QComboBox
{
public:
    ComboBox() {
        timer.setSingleShot(true);
        connect(&timer, &QTimer::timeout, this, [this](){ showPopup(); });
    }
    void showEvent(QShowEvent *e) {
        if(!mFirstTimeShown)
        {
            timer.start(100);
            mFirstTimeShown = true;
        }
    }

private:
    QTimer timer;
    bool mFirstTimeShown = false;
};

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
//    MainWindow w;
//    w.show();

//    QDialog dlg;
//    Ui_RetracerDialog dlgUi;
//    dlgUi.setupUi(&dlg);

//    dlgUi.doubleBufferingCB->setChecked(true);
//    dlgUi.errorCheckCB->setChecked(true);
//    dlgUi.singlethreadCB->setChecked(false);
//    dlgUi.coreProfileCB->setChecked(false);

//    dlgUi.queryHandlingSelector->addItem("Skip");
//    dlgUi.queryHandlingSelector->addItem("Run");
//    dlgUi.queryHandlingSelector->addItem("Run & Check");
//    //dlgUi.queryHandlingSelector->setMinimumContentsLength(11);
//    dlgUi.queryHandlingSelector->setCurrentIndex(0);
//    dlgUi.queryCheckReportThreshold->setValue(0);

//    dlg.exec();

    ComboBox combo;
    combo.addItem("Skip");
    combo.addItem("Run");
    combo.addItem("Run & Check");
    combo.show();

    return a.exec();
}

#include "main.moc"
