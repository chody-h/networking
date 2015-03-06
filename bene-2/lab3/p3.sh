python ../lab2/transfer.py -l 0.0 -f "test100.txt" > outputs/output2.txt

python ../python-plotting-tcp/converter.py

python ../python-plotting-tcp/plot-sequence.py -f "../lab3/outputs/converted_output2.txt"