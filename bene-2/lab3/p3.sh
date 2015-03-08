python ../lab2/transfer.py -l 0.0 -f "test200.txt" -n "three-nodes-queue.txt" > outputs/output3.txt

python ../python-plotting-tcp/converter.py

python ../python-plotting-tcp/plot-sequence.py -f "../lab3/outputs/converted_output3.txt"