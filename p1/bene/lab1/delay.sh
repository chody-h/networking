python delay.py -u 0.1 > outputs/qt_10.txt
python delay.py -u 0.2 > outputs/qt_20.txt
python delay.py -u 0.3 > outputs/qt_30.txt
python delay.py -u 0.4 > outputs/qt_40.txt
python delay.py -u 0.5 > outputs/qt_50.txt
python delay.py -u 0.6 > outputs/qt_60.txt
python delay.py -u 0.7 > outputs/qt_70.txt
python delay.py -u 0.8 > outputs/qt_80.txt
python delay.py -u 0.9 > outputs/qt_90.txt
python delay.py -u 0.95 > outputs/qt_95.txt
python delay.py -u 0.98 > outputs/qt_98.txt

python delayparser.py > outputs/average_queueing_delay.txt