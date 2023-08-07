#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include "./ui_retracerdialog.h"

#include <QDialog>
#include <QDebug>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    connect(ui->actionOpen_Dialog, SIGNAL(triggered()), this, SLOT(openDialog()));
    //connect(ui->actionReplay, &QAction::triggered, this, &MainWindow::replayStart);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::openDialog()
{
    qDebug() << "Show retracer dialog";

    QDialog dlg;
    Ui_RetracerDialog dlgUi;
    dlgUi.setupUi(&dlg);

    dlgUi.doubleBufferingCB->setChecked(true);
    dlgUi.errorCheckCB->setChecked(true);
    dlgUi.singlethreadCB->setChecked(false);
    dlgUi.coreProfileCB->setChecked(false);

    dlgUi.queryHandlingSelector->addItem("Skip");
    dlgUi.queryHandlingSelector->addItem("Run");
    dlgUi.queryHandlingSelector->addItem("Run & Check");
    //dlgUi.queryHandlingSelector->setMinimumContentsLength(11);
    dlgUi.queryHandlingSelector->setCurrentIndex(0);
    dlgUi.queryCheckReportThreshold->setValue(0);

    dlg.exec();
}
