Qapitrace Combobox Bug Exploration
==================================

This just holds some tests I have made to try to minimally reproduce a bug I am
seeing in qapitrace -- a gui tool that accompanies apitrace. The retracer dialog
has a combo box that has an entry with text "Run & Check". When the dialog is
shown, and the combo box is opened, the "Run & Check" entry is replaced with
"Run ...Check".

However, these tests do not seem to reproduce the behavior.

Running the Tests
-----------------

* python -m venv venv
* source venv/bin/activate
* python -m pip install -r requirements.txt
* python qapitrace-combobox-elide-bug.py

Reproducing Behavior in Qapitrace
---------------------------------

To reproduce the behavior, you must build the qapitrace tool, load a trace file,
and press `Ctrl-R` or choose menu item `Trace->Replay` to bring up the dialog in
question.

Here are steps:

* Clone the repo https://github.com/keithel/apitrace/tree/88357d3f2ee9c448b62daf4906ed03c972ab2c13
  Branch https://github.com/keithel/apitrace/commits/retracer-config-layout-fix
* Make sure you have a Qt 5.15 (I tested with 5.15.14) and/or a Qt 6.5 (I tested with 6.5.1) build available.
* Follow apitrace build instructions (not too many requirements) with -DENABLE_GUI=ON
  -DENABLE_QT6=ON is optional - both Qt 5 and Qt 6 will reproduce the issue.
* Start `qapitrace glxgears.trace`
* Press `Ctrl-R` to bring up the retracer dialog
* Open the "Handling" combo box.

Witness the `Run ...Check` elision that should not occur.
