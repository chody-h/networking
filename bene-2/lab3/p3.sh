rm -rf outputs/output1-*
rm -rf outputs/output2-*
rm -rf outputs/output3-*

python ../lab2/transfer.py -l 0.0 -f "test100.txt" > outputs/output1.txt

python ../python-plotting-tcp/converter.py

python ../python-plotting-tcp/plot-sequence.py -f "../lab3/outputs/converted_output1.txt"