FILE="competingRTT.txt"
FILENAME="outputs/$FILE"
FILENAME2="outputs/converted_$FILE"
FILENAME3="outputs/converted_queue_$FILE"



python transfer.py -f "test1m.txt" > $FILENAME

python ../python-plotting-tcp/converter.py

python ../python-plotting-tcp/plot-rate.py -f $FILENAME2
python ../python-plotting-tcp/plot-queue.py -f $FILENAME3