#include <QApplication>
#include <QComboBox>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QComboBox combo;
    combo.addItem("Skip");
    combo.addItem("Run");
    combo.addItem("Run & Check");
    combo.show();

    return a.exec();
}
